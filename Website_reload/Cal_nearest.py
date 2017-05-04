import pandas as pd
import pymysql

df_LX=pd.read_table('./BC/LX.txt',delimiter=',',header=None)
LX_input=float(df_LX[[1]].max().values)

df_RX=pd.read_table('./BC/RX.txt',delimiter=',',header=None)
RX_input=float(df_RX[[1]].max().values)

df_LY=pd.read_table('./BC/LY.txt',delimiter=',',header=None)
LY_input=float(df_LY[[1]].max().values)

df_RY=pd.read_table('./BC/RY.txt',delimiter=',',header=None)
RY_input=float(df_RY[[1]].max().values)

df_LZ=pd.read_table('./BC/LZ.txt',delimiter=',',header=None)
LZ_input=float(df_LZ[[1]].max().values)

df_RZ=pd.read_table('./BC/RZ.txt',delimiter=',',header=None)
RZ_input=float(df_RZ[[1]].max().values)

conn=pymysql.connect(host='localhost',user='pennstatecompbio',passwd='',db='brain_simulation')
cur=conn.cursor()

get_data_sql='select * from brain_simulation;'
df=pd.read_sql(get_data_sql,conn)

def distance(row):
    return (abs(LX_input)*(row['LX_Max']-LX_input)**2+abs(RX_input)*(row['RX_Max']-RX_input)**2+abs(LY_input)*(row['LY_Max']-LY_input)**2+abs(RY_input)*(row['RY_Max']-RY_input)**2+abs(LZ_input)*(row['LZ_Max']-LZ_input)**2+abs(RZ_input)*(row['RZ_Max']-RZ_input)**2)**0.5

df['distance']=df.apply(distance,axis=1)

df['distance'].min()

result=df.ix[[df['distance'].idxmin()]][['Region','Severity']]

region='{:02}'.format(int(result['Region'].values[0]))
print region

severity='{:03}'.format(int(result['Severity'].values[0]))
print severity