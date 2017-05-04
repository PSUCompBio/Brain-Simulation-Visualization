import flask
import pandas as pd
import pymysql
conn=pymysql.connect(host='localhost',user='pennstatecompbio',passwd='',db='brain_simulation')
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

sql='Insert into ' + 'brain_simulation'+ ' ('+ ','.join(column)+') values (' + ','.join(['%s']*len(column)) + ')'

values=[]
for i in range(len(df_new)):
    values.append(map(str,df_new.ix[i].tolist()))

cur.executemany(sql,values)

conn.commit()

conn.close()
