import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# =========================
# 1. CARGA DEL DATASET
# =========================
# Se lee el archivo CSV con los datos de ventas
df = pd.read_csv("ventas_dataset.csv")

# Se crea una nueva columna llamada "Ventas"
# Fórmula: Precio * Cantidad
df["Ventas"] = df["Precio"] * df["Cantidad"]


# =========================
# 2. MOSTRAR DATAFRAME
# =========================
print("=" * 60)
print("DATAFRAME COMPLETO")
print("=" * 60)
print(df)


# =========================
# 3. ESTADÍSTICAS CON PANDAS
# =========================
promedio_ventas = df["Ventas"].mean()
venta_maxima = df["Ventas"].max()
venta_minima = df["Ventas"].min()
suma_ventas = df["Ventas"].sum()

print("\n" + "=" * 60)
print("ESTADÍSTICAS DE VENTAS CON PANDAS")
print("=" * 60)
print(f"Promedio de ventas: {promedio_ventas}")
print(f"Venta máxima: {venta_maxima}")
print(f"Venta mínima: {venta_minima}")
print(f"Suma total de ventas: {suma_ventas}")


# =========================
# 4. FILTROS DE DATOS
# =========================

# Filtro 1: ventas realizadas en Lima
ventas_lima = df[df["Ciudad"] == "Lima"]

print("\n" + "=" * 60)
print("VENTAS REALIZADAS EN LIMA")
print("=" * 60)
print(ventas_lima)

# Filtro 2: productos con ventas mayores a 1000
ventas_mayores_1000 = df[df["Ventas"] > 1000]

print("\n" + "=" * 60)
print("PRODUCTOS CON VENTAS MAYORES A 1000")
print("=" * 60)
print(ventas_mayores_1000)

# Filtro 3: productos con cantidad vendida mayor a 5
cantidad_mayor_5 = df[df["Cantidad"] > 5]

print("\n" + "=" * 60)
print("PRODUCTOS CON CANTIDAD MAYOR A 5")
print("=" * 60)
print(cantidad_mayor_5)


# =========================
# 5. CÁLCULOS CON NUMPY
# =========================
# Convertir la columna "Ventas" en un array de NumPy
ventas_array = df["Ventas"].to_numpy()

media_numpy = np.mean(ventas_array)
desviacion_numpy = np.std(ventas_array)
maximo_numpy = np.max(ventas_array)
minimo_numpy = np.min(ventas_array)

print("\n" + "=" * 60)
print("CÁLCULOS CON NUMPY")
print("=" * 60)
print(f"Media: {media_numpy}")
print(f"Desviación estándar: {desviacion_numpy}")
print(f"Máximo: {maximo_numpy}")
print(f"Mínimo: {minimo_numpy}")


# =========================
# 6. GRÁFICOS CON MATPLOTLIB
# =========================

# Gráfico de barras: ventas por producto
ventas_producto = df.groupby("Producto")["Ventas"].sum()

plt.figure(figsize=(10, 5))
plt.bar(ventas_producto.index, ventas_producto.values)
plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Ventas")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de línea: cantidad vendida por producto
cantidad_producto = df.groupby("Producto")["Cantidad"].sum()

plt.figure(figsize=(10, 5))
plt.plot(cantidad_producto.index, cantidad_producto.values, marker="o")
plt.title("Cantidad Vendida por Producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Gráfico de pastel: distribución de ventas por ciudad
ventas_ciudad = df.groupby("Ciudad")["Ventas"].sum()

plt.figure(figsize=(8, 8))
plt.pie(ventas_ciudad.values, labels=ventas_ciudad.index, autopct="%1.1f%%")
plt.title("Distribución de Ventas por Ciudad")
plt.show()

# Histograma de ventas
plt.figure(figsize=(8, 5))
plt.hist(df["Ventas"], bins=10)
plt.title("Histograma de Ventas")
plt.xlabel("Ventas")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.show()

# Gráfico de dispersión: Precio vs Cantidad
plt.figure(figsize=(8, 5))
plt.scatter(df["Precio"], df["Cantidad"])
plt.title("Precio vs Cantidad")
plt.xlabel("Precio")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.show()


# =========================
# 7. ANÁLISIS DE RESULTADOS
# =========================
producto_mayor_ventas = ventas_producto.idxmax()
ciudad_mayor_ventas = ventas_ciudad.idxmax()

print("\n" + "=" * 60)
print("ANÁLISIS DE RESULTADOS")
print("=" * 60)
print(f"Producto que genera mayores ventas: {producto_mayor_ventas}")
print(f"Ciudad con mayor volumen de ventas: {ciudad_mayor_ventas}")
print(f"Promedio de ventas: {promedio_ventas}")
print(f"Desviación estándar de ventas: {desviacion_numpy}")

print("\nConclusión:")
print(
    "Existe variación en las ventas porque la desviación estándar es alta "
    "en comparación con el promedio."
)
print(
    "Los productos con menores ventas podrían promocionarse más para "
    "incrementar su participación en el mercado."
)