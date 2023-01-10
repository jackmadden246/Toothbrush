import sqlalchemy
import pandas as pd
import pymysql

df = pd.read_csv("/home/ec2-user/s3fs-fuse/mystaticwebsite5/open_postcode_geo.csv")
df = df.loc[df['status'] == 'live']
df = df.drop(['usertype', 'easting', 'northing', 'positional_quality_indicator', 'postcode_no_space', 'postcode_fixed_width_seven',
                 'postcode_fixed_width_eight', 'postcode_area', 'postcode_district', 'postcode_sector', 'outcode', 'incode'], axis = 1)
df['latitude'].replace("\\N", 'NULL', inplace= True)
df['longitude'].replace("\\N", 'NULL', inplace= True)
maria_db_details = "mysql+pymysql://admin:Titanic55!@database-10.cvunj1yhv8uv.eu-west-2.rds.amazonaws.com:3306/Toothdata1"
engine = sqlalchemy.create_engine(maria_db_details, echo=True)
df.to_sql(name='all_orders', con=engine, if_exists='append', index='id')                                    
