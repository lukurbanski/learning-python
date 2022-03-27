import logging

import azure.functions as func

import os
import pyodbc

logger = logging.getLogger('akshay')
logger.setLevel(logging.DEBUG)
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
logger.addHandler(sh)
logger.debug('TestLogger')

#Function for inserting data with HTTP trigger
#Database as parameter
#Name and surname in the body (json)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.') #not working
    logger.debug('Starting main function')


    server="proveit.database.windows.net"
    
    database = req.params.get('database')

    if not database:
        try:
            req_body = req.get_json()
        except ValueError:
            return func.HttpRequest('Name or surname not provided', status_code = 400)
        else:
            database = req_body.get('database')

    driver="{ODBC Driver 17 for SQL Server}"

    try:
        req_body = req.get_json()
    except ValueError:
        return func.HttpRequest('Name or surname not provided', status_code = 400)
    else:
        name = req_body.get('name')
        surname = req_body.get('surname')

    logger.debug(f'{name}, {surname}')

    

    connection_string = 'DRIVER='+driver+';SERVER='+server+';DATABASE='+database
    logger.debug('Trying to connect')
    conn = pyodbc.connect(connection_string+';Authentication=ActiveDirectoryMsi')
    logger.debug('Connection successful')

    cursor = conn.cursor()

    logger.debug('Trying to execute stored procedure')

    #not working, probably not enough priviliges.
    # sql = """
    # SET NOCOUNT ON;
    # EXEC dbo.insert_employee 'Lukasz','Test' ; """


    sql = """
    SET NOCOUNT ON;
    INSERT INTO [dbo].[employee] (first_name,  last_name) VALUES (?, ?); """
    
    values = (name,surname)


    cursor.execute(sql,values)
    conn.commit()

    
    logger.debug('Procedure executed successfully')

    #row = cursor.fetchone()

    return func.HttpResponse(
            f"This HTTP triggered function executed successfully. New person added to the database" , status_code=200
    )
 
