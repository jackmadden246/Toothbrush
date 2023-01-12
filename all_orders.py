import sqlalchemy
import pandas as pd
import pymysql
import dask.dataframe as dd
from sqlalchemy import exc
df = dd.read_csv("/home/ec2-user/s3fs-fuse/mystaticwebsite5/open_postcode_geo.csv", dtype={'latitude': 'object',
                                                                                           'longitude': 'object', 'easting': 'object', 'northing': 'object'})
df = df.drop(['usertype', 'easting', 'northing', 'positional_quality_indicator', 'postcode_no_space', 'postcode_fixed_width_seven', 'postcode_fixed_width_eight', 'postcode_area', 'postcode_district', 'postcode_sector', 'outcode', 'incode'], axis = 1)
df = df.loc[df['status'] == 'live']
df['latitude'] = df['latitude'].replace("'\\\\N'", 'NULL')
df['latitude'] = df['latitude'].replace('\\N', 0.0)
df['latitude'] = df['latitude'].fillna(value=0.0)
df['longitude'] = df['longitude'].replace("'\\\\N'", 'NULL')
df['longitude'] = df['longitude'].fillna(value=0.0)
df['longitude'] = df['longitude'].replace('\\N', 0.0)
maria_db_details = "mysql+pymysql://admin:Titanic55!@database-10.cvunj1yhv8uv.eu-west-2.rds.amazonaws.com:3306/Toothdata1"
engine = sqlalchemy.create_engine(maria_db_details, echo=True)
try:
    df.to_sql(name='all_orders',uri = maria_db_details, if_exists='append', chunksize = 1000, engine_kwargs = None, index='id')
except exc.IntegrityError:
    # Ignore duplicates
    pass
