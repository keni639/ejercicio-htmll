import pandas as pd
import matplotlib.pyplot as plt

datos = {
    'Producto': ['Televisor', 'Celular', 'Laptop', 'Tablet', 'Audífonos'],
    'Ventas': [150, 200, 250, 300, 100],
    'Precio': [750, 650, 900, 400, 120]
}

df = pd.DataFrame(datos)

html_tabla = df.to_html(index=False)
estadisticas = df.describe().to_html()

plt.bar(df['Producto'], df['Ventas'])
plt.title('Ventas por Producto')
plt.xlabel('Producto')
plt.ylabel('Ventas')
plt.xticks(rotation=30)
plt.tight_layout()
plt.savefig("grafica_ventas.png")
plt.close()

html = f"""
<html>
<head>
    <meta charset="utf-8">
    <title>Datos de Ventas</title>
</head>
<body>
<h2>Tabla de Datos:</h2>
{html_tabla}
<h2>Estadísticas Descriptivas:</h2>
{estadisticas}
<h2>Gráfica de Ventas:</h2>
<img src="grafica_ventas.png" alt="Gráfica de Ventas">
</body>
</html>
"""

with open("tabla.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Archivo 'tabla.html' creado correctamente.")
