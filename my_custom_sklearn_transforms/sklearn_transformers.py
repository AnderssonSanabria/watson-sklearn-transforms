from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd
import numpy as np

# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primero realizamos la cópia del DataFrame 'X' de entrada
        data = X.copy()
        datos = data.drop(data[data['EXISTING_SAVINGS']=='UNKNOWN'].index)
        datos['CHECKING_BALANCE']= datos['CHECKING_BALANCE'].replace('NO_CHECKING','0')
        datos = datos.drop(datos[datos['EXISTING_SAVINGS']=='UNKNOWN'].index)
        INSTALLMENT_PLANS_CAT=pd.get_dummies(datos['INSTALLMENT_PLANS'])
        LOAN_PURPOSE_CAT=pd.get_dummies(datos['LOAN_PURPOSE'])
        OTHERS_ON_LOAN_CAT=pd.get_dummies(datos['OTHERS_ON_LOAN'])
        SEX=pd.get_dummies(datos['SEX'])
        PROPERTY_CAT=pd.get_dummies(datos['PROPERTY'])
        HOUSING_CAT=pd.get_dummies(datos['HOUSING'])
        datos['CHECKING_BALANCE'] = pd.to_numeric(datos['CHECKING_BALANCE'],errors = 'coerce')
        datos['EXISTING_SAVINGS'] = pd.to_numeric(datos['EXISTING_SAVINGS'],errors = 'coerce')
        CREDIT_HISTORY_CAT=pd.get_dummies(datos['CREDIT_HISTORY'])
        datos =pd.concat((datos,OTHERS_ON_LOAN_CAT,LOAN_PURPOSE_CAT,INSTALLMENT_PLANS_CAT), axis=1)
        datos=datos.drop(['INSTALLMENT_PLANS','LOAN_PURPOSE','OTHERS_ON_LOAN'], axis=1)
        datos =pd.concat((datos,SEX,PROPERTY_CAT,HOUSING_CAT), axis=1)
        datos=datos.drop(['PROPERTY','HOUSING','SEX'], axis=1)
        datos =pd.concat((datos,CREDIT_HISTORY_CAT), axis=1)
        datos=datos.drop(['CREDIT_HISTORY'], axis=1)
        # Retornamos um nuevo dataframe sin las colunmas indeseadas
        return datos.dropna()
