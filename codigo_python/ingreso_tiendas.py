import matplotlib.ticker as mticker
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

URL = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
URL_2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
URL_3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
ULR_4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(URL)
tienda2 = pd.read_csv(URL_2)
tienda3 = pd.read_csv(URL_3)
tienda4 = pd.read_csv(ULR_4)

ingreso_total_tienda1 = tienda['Precio'].sum()
ingreso_total_tienda2 = tienda2['Precio'].sum()
ingreso_total_tienda3 = tienda3['Precio'].sum()
ingreso_total_tienda4 = tienda4['Precio'].sum()

# print(tienda.head())
# print(tienda['Precio'].sum())

# print(tienda.groupby('Categoría del Producto'))
# Increased figure size for better visibility
fig, ax = plt.subplots(figsize=(10, 6))

# Example data
tiendas = ('Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4')
y_pos = np.arange(len(tiendas))
ganancias = [ingreso_total_tienda1, ingreso_total_tienda2,
             ingreso_total_tienda3, ingreso_total_tienda4]

bars = ax.barh(y_pos, ganancias, align='center')
ax.set_yticks(y_pos, labels=tiendas)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Ingresos')
ax.set_title('Ingresos por tienda')

# Format x-axis labels to show values in billions
ax.xaxis.set_major_formatter(mticker.FuncFormatter(
    lambda x, p: format(x/1000000000, '.1f') + 'B'))

# Set the major tick locations to every 0.05 Billion (50 million) for clearer intervals
ax.xaxis.set_major_locator(mticker.MultipleLocator(
    100000000))  # 50,000,000 is 0.05 Billion

# Set the x-axis limits to emphasize differences
ax.set_xlim(left=1000000000)

for idx, bar in enumerate(bars):
    width = bar.get_width()
    ax.text(width - 10000000, bar.get_y() + bar.get_height()/2,    # (x,y) position
            # format to 2 decimal place
            f'{str(ganancias[idx]/1000000000)[:4] + 'B'}',
            ha='right', va='center', color='white', weight='bold')  # text alignment and style

plt.show()
