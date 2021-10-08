# pylint:disable=C0111,C0103

def query_orders(db):

    query_orders = """
    SELECT *
    FROM Orders
    ORDER BY orders.OrderID ASC
    """

    results = db.execute(query_orders)
    results = results.fetchall()
    return results
    # return a list of orders displaying each column
    # YOUR CODE HERE

def get_orders_range(db, date_from, date_to):

    get_orders_range = """

    SELECT *
    FROM Orders
    WHERE OrderDate > ? AND OrderDate < ?
    ORDER BY orders.OrderID ASC
    """

    results = db.execute(get_orders_range,(date_from,date_to))
    results = results.fetchall()
    return results

    # return a list of orders displaying all columns with OrderDate between date_from and date_to
    # YOUR CODE HERE

def get_waiting_time(db):

    get_waiting_time = """
    SELECT *,
    (julianday(orders.ShippedDate) - julianday(orders.OrderDate)) AS waitingtime
    FROM Orders
    ORDER BY waitingtime ASC
    """
    results = db.execute(get_waiting_time)
    results = results.fetchall()
    return results

    # get a list with all the orders displaying each column
    # and calculate an extra TimeDelta column displaying the number of days
    # between OrderDate and ShippedDate, ordered by ascending TimeDelta
    # YOUR CODE HERE
