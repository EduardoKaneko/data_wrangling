#Gather

import pandas as pd
import zipfile as zp

with zipfile.ZipFile('armenian-online-job-postings.zip', 'r') as myzip:
    myzip.extractall()

df = pd.read_csv('online-job-postings.csv')

#Assess

df.head()
 # - Not a number
 # - StartDate: Vários modos de dizer a mesma coisa(ASAP, Immediately, as soon as possible)

df.info()
sum(df.duplicated())
 # - Títulos não descritivos
 # - 2 Colunas que mostram as mesmas informações
 # - Linhas duplicadas

 
