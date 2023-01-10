import sqlalchemy
import pandas as pd
import pymysql
import boto3
import json
from sqlalchemy import exc

def lambda_handler(event, context):
    s3 = boto3.client ( "s3" )
    bucket = "mystaticwebsite5"
    key = "null_order_data.csv"
    file = s3.get_object( Bucket=bucket, Key=key)
    df = pd.read_csv(file['Body']) 
    df["Order Date"] = df["Order Date"].astype('datetime64')
    df['Order Date'] = df['Order Date'].dt.date
    df['Delivery Postcode'] = df['Delivery Postcode'].str.replace("%", " ")
    df["Dispatched Date"] = df["Dispatched Date"].astype('datetime64')
    df['Dispatched Date'] = df['Dispatched Date'].dt.date
    df.drop(["is_first", "Delivery Status", "Delivery Date"], axis=1, inplace=True)
    df.rename(columns ={'Dispatched Date':'Dispatch_Date', 'Order Date': 'Order_Date' , 'Delivery Postcode': 'Delivery_Postcode', 'Order Number': 'Order_Number', 'Toothbrush Type': 'Toothbrush_Type', 'Customer Age': 'Customer_Age', 'Order Quantity':'Order_Quantity', 'Delivery Postcode' : 'Delivery_Postcode', 'Billing Postcode': 'Billing_Postcode', 'Dispatch Status': 'Dispatch_Status'}, inplace=True)
    maria_db_details = "mysql+pymysql://admin:Titanic55!@database-10.cvunj1yhv8uv.eu-west-2.rds.amazonaws.com:3306/Toothdata1"
    engine = sqlalchemy.create_engine(maria_db_details, echo=True)
    for i in range(len(df)):
        try:
            df.iloc[i:i+1].to_sql(name='null_orders', con=engine, if_exists='append', index = 'id')
        except exc.IntegrityError:
            #Ignore duplicates
            pass
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
