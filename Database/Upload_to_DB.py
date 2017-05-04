import sqlite3, csv
import pandas as pd
conn = sqlite3.connect('Brain_Sim.db')
print "Opened database successfully";

#drop table brain_simulation;

cur=conn.cursor()
sql_create="""
create table if not exists brain_simulation(
ID			INT				,
RX_Max		float			,
RY_Max		float			,
RZ_Max		float			,
LX_Max		float			,
LY_Max		float			,
LZ_Max		float			,
Region		float			,
Strain		float			,
Severity    float			,
PRIMARY KEY	(ID)
);
"""
cur.execute(sql_create)

df_new=pd.read_csv('brain_simulation.csv')
column=df_new.columns.values.tolist()
df_new

sql='Insert into ' + 'brain_simulation'+ ' ('+ ','.join(column)+') values (' + ','.join(['?']*len(column)) + ')'
print sql

values=[]
for i in range(len(df_new)):
    values.append(map(str,df_new.ix[i].tolist()))


cur.executemany(sql,values)    

conn.commit()

conn.close()

