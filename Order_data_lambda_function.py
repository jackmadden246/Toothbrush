import sqlalchemy
import pymysql
from sqlalchemy import exc
import dask.dataframe as dd

df = dd.read_csv("/home/ec2-user/s3fs-fuse/mystaticwebsite5/order_data.csv")
df["Order Date"] = df["Order Date"].astype('datetime64')
df['Order Date'] = df['Order Date'].dt.date
df['Delivery Postcode'] = df['Delivery Postcode'].str.replace("%", " ")
df = df.drop(["is_first"], axis=1)
df["Delivery Date"] = df["Delivery Date"].astype('datetime64')
df['Delivery Date'] = df['Delivery Date'].dt.date
df['Delivery Status'] = df['Delivery Status'].fillna(value='Unknown')
df['Delivery Date'] = df['Delivery Date'].dropna()
df['Dispatched Date'] = df['Dispatched Date'].astype('datetime64')
df['Dispatched Date'] = df['Dispatched Date'].dt.date
df = df.rename(columns={'Dispatched Date': 'Dispatch_Date', 'Order Date': 'Order_Date',
                           'Delivery Postcode': 'Delivery_Postcode', 'Order Number': 'Order_Number',
                           'Toothbrush Type': 'Toothbrush_Type', 'Customer Age': 'Customer_Age',
                           'Order Quantity': 'Order_Quantity','Billing Postcode': 'Billing_Postcode',
                           'Delivery Date': 'Delivery_Date', 'Delivery Status': 'Delivery_Status',
                           'Dispatch Status': 'Dispatch_Status'})
maria_db_details = "mysql+pymysql://admin:Titanic55!@database-10.cvunj1yhv8uv.eu-west-2.rds.amazonaws.com:3306/Toothdata1"
engine = sqlalchemy.create_engine(maria_db_details, echo=True)
try:
        df.to_sql(name='current_orders', uri = maria_db_details, if_exists='append', chunksize = 1000, engine_kwargs = None, index='id')
except exc.IntegrityError:
        # Ignore duplicates
        pass
