from sqlalchemy import create_engine
import pandas as pd
import matplotlib.pyplot as plt

# Evolución de los pedidos
engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/Northwind')

query1 = """
SELECT 
    EXTRACT(YEAR FROM Order_Date) AS Year,
    EXTRACT(MONTH FROM Order_Date) AS Month,
    COUNT(*) AS TotalOrders
FROM 
    Orders
GROUP BY 
    EXTRACT(YEAR FROM Order_Date), 
    EXTRACT(MONTH FROM Order_Date)
ORDER BY 
    Year, 
    Month;
"""

try:
    df = pd.read_sql(query1, engine)
    
    plt.figure(figsize=(10, 6))
    plt.plot(df.index, label='Pedidos por Mes', marker='o')
    plt.xlabel('Índice')
    plt.ylabel('Cantidad de Pedidos')
    plt.title('Pedidos por Mes y Año')
    plt.legend()
    plt.grid()
    plt.show()
    
except Exception as e:
    print(f"Error al conectar o ejecutar la consulta: {e}")

# Distribución geográfica
data =[
    {"Country": "Germany", "Orders": 122, "Continent": "Europe"},
    {"Country": "USA", "Orders": 122, "Continent": "America"},
    {"Country": "Brazil", "Orders": 83, "Continent": "America"},
    {"Country": "France", "Orders": 77, "Continent": "Europe"},
    {"Country": "UK", "Orders": 56, "Continent": "Europe"},
    {"Country": "Venezuela", "Orders": 46, "Continent": "America"},
    {"Country": "Austria", "Orders": 40, "Continent": "Europe"},
    {"Country": "Sweden", "Orders": 37, "Continent": "Europe"},
    {"Country": "Canada", "Orders": 30, "Continent": "America"},
    {"Country": "Italy", "Orders": 28, "Continent": "Europe"},
    {"Country": "Mexico", "Orders": 28, "Continent": "America"},
    {"Country": "Spain", "Orders": 23, "Continent": "Europe"},
    {"Country": "Finland", "Orders": 22, "Continent": "Europe"},
    {"Country": "Ireland", "Orders": 19, "Continent": "Europe"},
    {"Country": "Belgium", "Orders": 19, "Continent": "Europe"},
    {"Country": "Denmark", "Orders": 18, "Continent": "Europe"},
    {"Country": "Switzerland", "Orders": 18, "Continent": "Europe"},
    {"Country": "Argentina", "Orders": 16, "Continent": "America"},
    {"Country": "Portugal", "Orders": 13, "Continent": "Europe"},
    {"Country": "Poland", "Orders": 7, "Continent": "Europe"},
    {"Country": "Norway", "Orders": 6, "Continent": "Europe"}
]
df_countries = pd.DataFrame(data)

df_continent = df_countries.groupby('Continent')['Orders'].sum().reset_index()

plt.figure(figsize=(8, 6))
plt.bar(df_continent['Continent'], df_continent['Orders'], color=['skyblue', 'orange', 'green'])
plt.xlabel('Continente')
plt.ylabel('Total de Pedidos')
plt.title('Distribución de Pedidos por Continente')
plt.grid(axis='y')
plt.show()

#diferencia fechas
query2= """
SELECT shipped_date,
       required_date
FROM Orders
"""

try:
    df = pd.read_sql(query2, engine)
    df['shipped_date'] = pd.to_datetime(df['shipped_date'])
    df['required_date'] = pd.to_datetime(df['required_date'])
    
    df['Difference'] = (df['required_date'] - df['shipped_date']).dt.days
    df = df[df['Difference'] >= 0]

    plt.figure(figsize=(8, 6))
    plt.boxplot(df['Difference'], labels=['Diferencia en días'])
    plt.title('Boxplot de Diferencias entre Fechas')
    plt.ylabel('Diferencia (días)')
    plt.grid(axis='y')
    plt.show()
    
except Exception as e:
    print(f"Error al conectar o ejecutar la consulta: {e}")

#clientes sin pedidos
query3 = """
    SELECT c.customer_id, o.order_id 
    FROM Customers c
    LEFT JOIN Orders o ON c.customer_id = o.customer_id;
    """

try:
    df = pd.read_sql(query3, engine)
    
    null_count = df['order_id'].isnull().sum()
    valid_count = df['order_id'].notnull().sum()
    
    labels = ['Clientes sin pedidos (nulos)', 'Clientes con pedidos (válidos)']
    sizes = [null_count, valid_count]
    
    plt.figure(figsize=(8, 8))
    plt.pie(sizes, labels=labels,autopct='%1.1f%%', startangle=90,)
    plt.title('Porcentaje de Clientes con y sin Pedidos')
    plt.axis('equal')  # Para que el gráfico sea un círculo
    plt.show()

except Exception as e:
    print(f"Error al conectar o ejecutar la consulta: {e}")
          
        
#restock de productos
query4= """
    SELECT product_id, units_in_stock, units_on_order
    FROM products
    """
try:
    df = pd.read_sql(query4, engine)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(df['units_in_stock'], df['units_on_order'], color='green', marker='o')

    plt.xlabel('Unidades en Stock')
    plt.ylabel('Unidades Pedidas')
    plt.title('Relación entre Unidades en Stock y Unidades Pedidas')
    plt.grid(True)

    plt.show()
except Exception as e:
    print(f"Error al conectar o ejecutar la consulta: {e}")