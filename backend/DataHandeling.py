import app
import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer
from backend import slicingData



def fillna(df):
    num,cat=slicingData.slice(df)

    imputer1=SimpleImputer(missing_values=np.nan,strategy='mean',fill_value=float)
    imputer1.fit_transform(df[num])

    imputer2=SimpleImputer(missing_values=np.nan,strategy="most_frequent",fill_value=str)
    imputer2.fit_transform(df[cat])

    return df
