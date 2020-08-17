from sklearn.base import BaseEstimator, TransformerMixin


# All sklearn Transforms must have the `transform` and `fit` methods
class DropColumns(BaseEstimator, TransformerMixin):
    def __init__(self, columns):
        self.columns = columns

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        # Primeiro realizamos a cópia do dataframe 'X' de entrada
        data = X.copy()
        # Retornamos um novo dataframe sem as colunas indesejadas
        return data.drop(labels=self.columns, axis='columns')

class RemoveZeros(BaseEstimator, TransformerMixin):
    def fit(self, df, y=None):
        return self
    
    def transform(self, df):
        ndf = df.loc[df["NOTA_DE"]!=0]
        ndf = df.loc[df["NOTA_EM"]!=0]
        ndf = df.loc[df["NOTA_MF"]!=0]
        ndf = df.loc[df["NOTA_GO"]!=0]
        return ndf
