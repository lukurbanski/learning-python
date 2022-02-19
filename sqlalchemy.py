# import pyodbc
# from sqlalchemy import create_engine
# from unicodedata import ucnhash_CAPI
from urllib import parse as prs
import sqlalchemy

print(sqlalchemy.__package__)


params = prs.quote_plus \
    (r'Driver={ODBC Driver 13 for SQL Server};Server=tcp:yourDBServerName.database.windows.net,1433;Database=dbname;Uid=username@dbserverName;Pwd=xxx;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;')
conn_str = 'mssql+pyodbc:///?odbc_connect={}'.format(params)

# print(params)