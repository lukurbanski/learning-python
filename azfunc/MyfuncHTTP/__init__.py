import logging

import azure.functions as func

import os
import pyodbc

logger = logging.getLogger('akshay')
logger.setLevel(logging.INFO)
sh = logging.StreamHandler()
sh.setLevel(logging.INFO)
logger.addHandler(sh)
logger.info('TestLogger')


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.') #not working
    logger.info('Starting main function')


    server="proveit.database.windows.net"
    
    database = req.params.get('database')

    if not database:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            database = req_body.get('database')

    driver="{ODBC Driver 17 for SQL Server}"
    query="select count(1) from [dbo].[employee]"

    connection_string = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+database
    logger.info('Trying to connect')
    conn = pyodbc.connect(connection_string+';Authentication=ActiveDirectoryMsi')
    logger.info('Connection successful')

    cursor = conn.cursor()
    nrrows = cursor.execute(query).fetchval()
    #row = cursor.fetchone()

    logger.info(nrrows)

    return func.HttpResponse(
            f"This HTTP triggered function executed successfully. Connected to database.{nrrows}" , status_code=200
    )
 