
import numpy as np
import pandas as pd
import csv
with open ('african_crises.csv')as f:
   # tunisie = open ('newTunisie')
    df = pd.read_csv(f)
    tunisie = df.loc[df["case"]==63]
    print(df)
    print (tunisie)
    tunisie.to_csv('crisestunisie.csv')





