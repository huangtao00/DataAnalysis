import pandas as pd
from pandas import DataFrame,Series
import numpy as np


import json,os,sys,random
import matplotlib.pyplot as plt
current_dir=os.path.abspath(".")

filename=[file  for file in os.listdir(current_dir) if ".txt" in file]
fn=filename[0] if len(filename)==1 else ""

records=[json.loads(line) for line in open(fn)]


table=DataFrame(records)
# print (table)
timezoneSer=table["tz"]  #to series object
# print (timezoneSer[:10])
# print(type(timezoneSer))

# print (timezoneSer.value_counts())
a=timezoneSer.value_counts()
# print(a[:10])

clean_tz=timezoneSer.fillna("Missing") #fill NA
clean_tz[clean_tz==""]="Unknown"

tz_counts=clean_tz.value_counts()
print(tz_counts[:10])
# tz_counts[:10].plot(kind="barh",rot=0)
# print(table.c)


agent=Series([a.split()[0]  for a in table.a.dropna()])
# print(agent[:10])



realframe=table[table.a.notnull()] # remove the a field which is empty
# print (realframe.a)

os=np.where(realframe.a.str.contains("Windows"), "Windows","Not Windows")
by_tz_os=realframe.groupby(["tz",os])
agg_counts=by_tz_os.size().unstack().fillna(0)

indexer=agg_counts.sum(1).argsort()
count_subset=agg_counts.take(indexer)[-10:]

print (count_subset)
count_subset.plot(kind="barh",stacked=True)

normed_subset=count_subset.div(count_subset.sum(1),axis=0)
normed_subset.plot(kind="barh",stacked=True)