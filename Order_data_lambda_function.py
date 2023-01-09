import sqlalchemy
import pandas as pd
import pymysql
import boto3
import json


def lambda_handler(event, context):
        s3 = boto3.client("s3")
        bucket = "mystaticwebsite5"
        key = "order_data_20230106_1530.csv"
        file = s3.get_object(Bucket=bucket, Key=key)
        df = pd.read_csv(file['Body'])
        df["Order Date"] = df["Order Date"].astype('datetime64')
        df['Order Date'] = df['Order Date'].dt.date
        df['Delivery Postcode'] = df['Delivery Postcode'].str.replace("%", " ")
        df.drop(["is_first"], axis = 1, inplace = True)
        df["Delivery Date"] = df["Delivery Date"].astype('datetime64')
        df['Delivery Date'] = df['Delivery Date'].dt.date
        df['Delivery Status'] = df['Delivery Status'].fillna(value="Unavailable")
        df['Delivery Date'] = df['Delivery Date'].fillna(value="Unknown")
        df['Dispatched Date'] = df['Dispatched Date'].astype('datetime64')
        df['Dispatched Date'] = df['Dispatched Date'].dt.date
        df.rename(columns={'Dispatched Date': 'Dispatch_Date', 'Order Date': 'Order_Date',
                           'Delivery Postcode': 'Delivery_Postcode', 'Order Number': 'Order_Number',
                           'Toothbrush Type': 'Toothbrush_Type', 'Customer Age': 'Customer_Age',
                           'Order Quantity': 'Order_Quantity', 'Delivery Postcode': 'Delivery_Postcode',
                           'Billing Postcode': 'Billing_Postcode', 'Dispatch Status': 'Dispatch_Status'}, inplace=True)
        maria_db_details = "mysql+pymysql://admin:Titanic55!@database-10.cvunj1yhv8uv.eu-west-2.rds.amazonaws.com:3306/Toothdata1"
        engine = sqlalchemy.create_engine(maria_db_details, echo=True)
        df.to_sql(name='order_details', con=engine, if_exists='append')
    
        return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
