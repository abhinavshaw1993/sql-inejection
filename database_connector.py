import pandas as pd

# Create a connection with SQL server to get data.
def exec_sql_query(query, param=None):

    from sqlalchemy import create_engine
    import urllib
    params = urllib.parse.quote_plus(
    "DRIVER={SQL Server Native Client 11.0};SERVER=LAPTOP-C3LFVOFI;DATABASE=student_life;UID=web_usr;PWD=26592385")
    engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % params)
    connection = engine.raw_connection()

    try:
        cursor = connection.cursor()
        if(param):
            cursor.execute(query, param)
        else :
            cursor.execute(query)

        results = cursor.fetchall()
        columns = [column[0] for column in cursor.description]
        df = pd.DataFrame.from_records(results, columns=columns)
        cursor.close()
        connection.commit()
    finally:
        connection.close()

    del engine
    return df
