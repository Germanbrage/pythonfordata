import psycopg2
import pandas

dbname = "Northwind"
user = "postgres"
password = "admin"
host = "localhost"
port = "5432"

try:
    conn = psycopg2.connect(
        dbname=dbname,
        user=user,
        password=password,
        host=host,
        port=port
    )

    cur = conn.cursor()
    
    query1= """
        SELECT 
            p.category_id,
            MAX(o.order_date) AS ultima_fecha_pedido
        FROM 
            products p
        JOIN 
            order_details od ON p.product_id = od.product_id
        JOIN 
            orders o ON od.order_id = o.order_id
        GROUP BY 
            p.category_id;
        """
    cur.execute(query1)
    products= cur.fetchall()

    print("Último pedido por categoría:")
    for product in products:
        print(f"categorie: {product[0]}, fecha: {product[1]}")
        
        
    query2= """
    SELECT DISTINCT product_id
FROM order_details
WHERE product_id NOT IN (
    SELECT product_id
    FROM order_details
    WHERE discount = 0
);
"""
    cur.execute(query2)
    order_details= cur.fetchall()
    if not order_details:
        print("No existe ningún producto que haya sido vendido siempre con descuento.")
    else: 
        print("Productos que nunca se hayan vendido a precio original:")
        for product in products:
          print(f"Product_id: {product[0]}")
    
    query3="""
    SELECT p.product_id, p.product_name, p.category_id, c.category_name
FROM products p
JOIN categories c ON p.category_id = c.category_id
WHERE p.category_id = 3;
"""
    cur.execute(query3)
    products= cur.fetchall()

    print("Productos de 'Confections':")
    for product in products:
        print(f"Product_id: {product[0]}, Nombre:{product[1]}, Category_id{product[2]}, Nombre compañía:{product[3]}")
    
    query4= """
    SELECT DISTINCT supplier_id
FROM products
WHERE supplier_id NOT IN (
    SELECT supplier_id
    FROM products
    WHERE discontinued = 0
);
"""
    cur.execute(query4)
    products= cur.fetchall()

    print("Proveedores con totalidad de productos descontinuados:")
    for product in products:
        print(f"Supplier_id: {product[0]}")
        
    query5= """
        SELECT DISTINCT c.customer_id, o.order_id, od.product_id, od.quantity
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
JOIN order_details od ON o.order_id = od.order_id
WHERE od.quantity = 30
  AND od.product_id = 1;
"""

    cur.execute(query5)
    orders= cur.fetchall()

    print("Pedidos de 30 unidades de Chai:")
    for order in orders:
        print(f"Customer: {order[0]}, Order: {order[1]}, Product: {order[2]}, Quantity:{order[3]}")
    
    query6= """
SELECT  o.customer_id, 
    SUM (od.quantity) AS total_quantity
FROM orders o
JOIN order_details od ON o.order_id = od.order_id
GROUP BY o.customer_id
  HAVING 
  SUM (od.quantity)>1000
"""
    
    cur.execute(query6)
    orders= cur.fetchall()

    print("Clientes con más de 1000 unidades pedidas:")
    for order in orders:
        print(f"Customer_id: {order[0]}, Quantity: {order[1]}")

    query7 = """
SELECT city
FROM employees
GROUP BY city
HAVING COUNT(employee_id) > 5; 
"""

    try:
      cur.execute(query7)
      employees = cur.fetchall()

      if not employees:
          print("No hay ninguna ciudad con más de 5 empleados.")
      else:
          print("Ciudades con más de 5 empleados:")
          for employee in employees:
              print(f"Ciudad: {employee[0]}")

    except Exception as e:
      print(f"Error al ejecutar la consulta: {e}")


    cur.close() 
    conn.close()
    
except Exception as e:
    print(f"Error al conectar o ejecutar la consulta: {e}")
    
    