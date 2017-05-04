
# coding: utf-8

# # calculate closest point

import pandas as pd
import sqlite3
from flask import Flask, render_template, request, url_for, json
app = Flask(__name__)




@app.route('/')

def home():
   	print "Ok"

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

	conn=conn = sqlite3.connect('Brain_Sim.db')
	cur=conn.cursor()

	get_data_sql='select * from brain_simulation;'
	df=pd.read_sql(get_data_sql,conn)

	def distance(row):
	    return (abs(LX_input)*(row['LX_Max']-LX_input)**2+abs(RX_input)*(row['RX_Max']-RX_input)**2+abs(LY_input)*(row['LY_Max']-LY_input)**2+abs(RY_input)*(row['RY_Max']-RY_input)**2+abs(LZ_input)*(row['LZ_Max']-LZ_input)**2+abs(RZ_input)*(row['RZ_Max']-RZ_input)**2)**0.5

	df['distance']=df.apply(distance,axis=1)

	result=df.ix[[df['distance'].idxmin()]][['Region','Severity']]

	region='{:02}'.format(int(result['Region'].values[0]))

	severity='{:03}'.format(int(result['Severity'].values[0]))


   	return render_template('Brain_Results_v6.html',regionID=region,severityID=severity)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)


