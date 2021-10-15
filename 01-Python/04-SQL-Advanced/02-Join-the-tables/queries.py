# pylint:disable=C0111,C0103

def detailed_orders(db):
    query = """
    SELECT
    orders.OrderID,
    customers.ContactName,
    employees.FirstName
    FROM Orders
    JOIN Customers ON customers.CustomerID = orders.CustomerID
    JOIN Employees ON employees.EmployeeID = orders.EmployeeID
    ORDER BY order_id
    """
    results = db.execute(query)
    results = results.fetchall()
    return results

    '''return a list of all orders (order_id, customer.contact_name,
    employee.firstname) ordered by order_id'''
    # YOUR CODE HERE

def spent_per_customer(db):

    query = """
    SELECT
	Orders.CustomerID,
	Customers.ContactName,
	OrderDetails.UnitPrice,
	OrderDetails.Quantity,
	OrderDetails.Quantity * OrderDetails.UnitPrice
    FROM orders
    JOIN Customers on Customers.customerID = Orders.customerID
    JOIN OrderDetails on Orders.OrderID = OrderDetails.OrderID
    ORDER BY orders.OrderID ASC

    """
    results = db.execute(query)
    results = results.fetchall()
    return results

    '''return the total amount spent per customer ordered by ascending total
    amount (to 2 decimal places)
    SELECT

    Exemple :
        Jean   |   100
        Marc   |   110
        Simon  |   432
        ...
    '''
    # YOUR CODE HERE

def best_employee(db):
    query = """
    SELECT
	Employees.FirstName,
	Employees.LastName,
  	OrderDetails.UnitPrice,
	OrderDetails.Quantity,
    (OrderDetails.Quantity * OrderDetails.UnitPrice) as price,
    sum(OrderDetails.Quantity * OrderDetails.UnitPrice)
    FROM OrderDetails
    JOIN Employees on employees.employeeID = Orders.employeeID
    JOIN Orders on Orders.orderID = OrderDetails.OrderID
    GROUP BY Employees.EmployeeID
    ORDER BY sum(OrderDetails.Quantity * OrderDetails.UnitPrice) DESC

    """
    results = db.execute(query)
    results = results.fetchone()
    return results
    '''Implement the best_employee method to determine who’s the best employee! By “best employee”, we mean the one who sells the most.
    We expect the function to return a tuple like: ('FirstName', 'LastName', 6000 (the sum of all purchase)). The order of the information is irrelevant'''
    # YOUR CODE HERE

def orders_per_customer(db):

    query = """"
    SELECT
    Customers.ContactName,

    """


    '''TO DO: return a list of tuples where each tupe contains the contactName
    of the customer and the number of orders they made (contactName,
    number_of_orders). Order the list by ascending number of orders'''
    # YOUR CODE HERE
