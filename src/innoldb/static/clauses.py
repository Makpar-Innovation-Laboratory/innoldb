EQUALS = "="
LIKE = "LIKE"
IN = "IN"


def where_equals(*columns):
    """Generates a **PartiQL** `WHERE` clause for an arbitrary number of columns.

    :param *columns: List of columns to include in the where clause.
    :type *columns: list
    :return: `WHERE` clause
    :rtype: str
    """
    clause = None
    for column in columns:
        if clause is None:
            clause = "WHERE {} {} ? ".format(column, EQUALS)
        else:
            clause += "AND {} {} ? ".format(column, EQUALS)
    return clause


def where_in(**columns):
    clause = None
    for column, n in columns.items():
        if clause is None:
            clause = "WHERE {} IN (".format(column)
        else:
            clause += "AND {} IN (".format(column)
        if n == 1:
            clause += "?) "
        else:
            clause += "?,"*(n-1) + "?) "
    return clause


def set_statement(*columns):
    clause = None
    for column in columns:
        if clause is None:
            clause = 'SET {} = ? '.format(column)
        else:
            clause += ', {} = ? '.format(column)
    return clause
