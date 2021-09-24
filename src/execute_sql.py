import MySQLdb

from config import mysql


def query_handler_fetch(query: str, values: tuple = ()) -> tuple:
    """
    :param query: It is a of type str mysql query
    :param values: It is a tuple whose values is used for substituting in query

    cursor object is created and first 'values' presence is checked if present we pass values for
    executing sql query else only query is passed.
    Fetching is done and cursor in closed

    :return: tuple of fetched data
    """
    cur = mysql.connection.cursor()
    if values:
        cur.execute(query, values)
        results = cur.fetchall()
        cur.close()
        return results
    else:
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        return results


def query_handler_no_fetch(query: str, values: tuple = ()) -> str:
    """
    :param query: It is a of type str mysql query
    :param values: It is a tuple whose values is used for substituting in query
    cursor is created and query is executed. Then the changes is committed and finally cursor is closed
    :raise raises an Exception MySQLdb._exceptions.DataError: if data passed is larger than sql table predefined limit
    :return: str
    """
    cur = mysql.connection.cursor()
    try:
        cur.execute(query, values)
        mysql.connection.commit()
        cur.close()
    except Exception:
        return "We can't perform the operation due to overload on database"
