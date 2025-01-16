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
    
    query1 = """
    SELECT e.employee_id, e.first_name, e.last_name, e.city, e.country
    FROM employees e
    """
    cur.execute(query1)
    employees= cur.fetchall()

    print("Empleados en 'Global Importaciones':")
    for employee in employees:
        print(f"ID: {employee[0]}, Nombre: {employee[1]}, Apellido: {employee[2]}, Ciudad: {employee[3]}, País: {employee[4]}")

    query2 = """
    SELECT p.product_id, p.supplier_id, p.product_name, p.unit_price, p.units_in_stock, p.units_on_order, p.discontinued
    FROM products p
    """
    
    cur.execute(query2)
    products= cur.fetchall()
    
    print ("Productos en 'Global Importaciones':")
    for product in products:
        print(f"ID: {product[0]},Supplier_id: {product[1]}, Nombre: {product[2]}, Precio_unitario: {product[3]}, Unidades_en_stock: {product[4]}, Unidades_pedidas: {product[5]},Descontiuado: {product[6]}")

    query3 = """
    SELECT p.product_name, p.units_in_stock
    FROM products p
    WHERE p.discontinued = 1
    """
    
    cur.execute(query3)
    
    print ("Productos descontinuados en 'Global Importaciones':")
    for product in products:
        print (f"Nombre: {product[2]}, Unidades_en_stock: {product[4]}")
    
    query4 = """
    SELECT s.supplier_id, s.company_name, s.city, s.country
    FROM suppliers s
    """
    cur.execute(query4)
    suppliers = cur.fetchall()
    
    print ("Proveedores de 'Global Importaciones':")
    for supplier in suppliers:
        print(f"ID: {supplier[0]}, Compañía: {supplier[1]}, Ciudad: {supplier[2]}, País: {supplier[3]}")
    
    query5 = """
    SELECT o.order_id, o.customer_id, o.employee_id, o.order_date, o.required_date, o.shipped_date
    FROM orders o
    """
    
    cur.execute(query5)
    orders= cur.fetchall()
    
    print ("Pedidos de 'Global Importaciones':")
    for order in orders:
        print (f"ID: {order[0]}, Cliente: {order[1]}, Transportista: {order[2]}, Fecha_pedido: {order[3]}, Fecha_envío: {order[4]}, Fecha_llegada: {order[5]}")
    
    query6 = """
    SELECT c.customer_id, c.company_name, c.city, c.country
    FROM customers c
    """
    
    cur.execute(query6)
    customers= cur.fetchall()
    
    print ("Clientes de 'Global Importaciones':")
    for customer in customers:
        print (f"Id:{customer[0]}, Nombre:{customer[1]}, Ciudad:{customer[2]}, País:{customer[3]}")
    
    query7 = """
    SELECT s.shipper_id, s.company_name
    FROM shippers s
    """
    
    cur.execute(query7)
    shippers= cur.fetchall()
    
    print ("Transportistas de 'Global Importaciones':")
    for shipper in shippers:
        print (f"Id:{shipper[0]}, Nombre:{shipper[1]}")
    
    
    cur.close() 
    conn.close()
    
except Exception as e:
    print(f"Error al conectar o ejecutar la consulta: {e}")
    
    
    
    
    
"""
 ¿Con qué empresas de transporte trabajamos? Indica su id del transportista y 
el nombre de la compañía.
 ¿Cómo son las relaciones de reporte de resultados entre los empleados?
"""