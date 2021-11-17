from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = data.drop(data[data['EXISTING_SAVINGS']=='UNKNOWN'].index)
        data['CHECKING_BALANCE']= data['CHECKING_BALANCE'].replace('NO_CHECKING','0')
        data = data.drop(data[data['EXISTING_SAVINGS']=='UNKNOWN'].index)
        INSTALLMENT_PLANS_CAT=pd.get_dummies(data['INSTALLMENT_PLANS'])
        LOAN_PURPOSE_CAT=pd.get_dummies(data['LOAN_PURPOSE'])
        OTHERS_ON_LOAN_CAT=pd.get_dummies(data['OTHERS_ON_LOAN'])
        SEX=pd.get_dummies(data['SEX'])
        PROPERTY_CAT=pd.get_dummies(data['PROPERTY'])
        HOUSING_CAT=pd.get_dummies(data['HOUSING'])
        data['CHECKING_BALANCE'] = pd.to_numeric(data['CHECKING_BALANCE'],errors = 'coerce')
        data['EXISTING_SAVINGS'] = pd.to_numeric(data['EXISTING_SAVINGS'],errors = 'coerce')
        CREDIT_HISTORY_CAT=pd.get_dummies(data['CREDIT_HISTORY'])
        data =pd.concat((data,OTHERS_ON_LOAN_CAT,LOAN_PURPOSE_CAT,INSTALLMENT_PLANS_CAT), axis=1)
        data=data.drop(['INSTALLMENT_PLANS','LOAN_PURPOSE','OTHERS_ON_LOAN'], axis=1)
        data =pd.concat((data,SEX,PROPERTY_CAT,HOUSING_CAT), axis=1)
        data=data.drop(['PROPERTY','HOUSING','SEX'], axis=1)
        data =pd.concat((data,CREDIT_HISTORY_CAT), axis=1)
        data=data.drop(['CREDIT_HISTORY'], axis=1)
        # Retornamos um nuevo dataframe sin las colunmas indeseadas
        return data.dropna()
