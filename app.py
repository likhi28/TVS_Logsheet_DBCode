from flask import Flask,request,jsonify,send_file,Response
import pandas as pd

from flask_cors import CORS
import sqlalchemy
from flaskext.mysql import MySQL
import pyodbc
import ast

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.types import Integer, Text, String, Date, Float, DateTime
from sqlalchemy import Table, Column, MetaData 
import urllib
import json

app = Flask(__name__)

CORS(app, support_credentials=True)

server = "DESKTOP-ODD3ODM\SQLEXPRESS"
database ="SampleData"
username = "sa"
password = "Sqlserver2008"

driver = '{SQL Server}'

conn=pyodbc.connect("DRIVER={SQL Server};SERVER=DESKTOP-ODD3ODM\SQLEXPRESS;UID=sa;PWD=Sqlserver2008;DATABASE=Requirement")
myconn = conn.cursor() 

@app.route('/Insert_Table', methods = ['GET', 'POST'])
def Insert_Table():
    # table_name=request.values.get('GetTableName')
    
    # getparams=request.values.get('ColumnNames')
    # Column_Names=ast.literal_eval(getparams)
    
    getval=request.values.get('ColumnValues')

    # getval=request.args.getlist('ColumnValues')
    # Column_Values=json.loads(getval)
    
    Column_Values=ast.literal_eval(getval)
    # getcolnames=request.values.get('ColumnValues')
    
    getdbtable=pd.DataFrame()

    # values = ', '.join(Column_Names)
    
    # SQLCommand = 'INSERT INTO '+ table_name+'(date,downTimeFrom,downTimeTo,machineName,noOfRoll,operatorName,outputMeters,reason,reasonCode,runningTimeFrom,runningTimeTo,sapDocument,shift,size,trtNo) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) OPTION (QUERYTRACEON 460);'
    SQLCommand = 'INSERT INTO CreateRequirement (date,downTimeFrom,downTimeTo,machineName,noOfRoll,operatorName,outputMeters,reason,reasonCode,runningTimeFrom,runningTimeTo,sapDocument,shift,size,trtNo) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) OPTION (QUERYTRACEON 460);'

    myconn.execute(SQLCommand,Column_Values)
    myconn.commit()
    statement='select * from CreateRequirement'
    # statement='select * from'+' '+table_name
   
    
    getdbtable=pd.read_sql(statement,conn)
    conn.close()

    return getdbtable.to_json(orient='records')


if __name__ == '__main__':
   app.run()
