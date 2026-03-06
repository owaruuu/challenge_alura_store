import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.ticker as mticker

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

producto_mas_vendido1 = tienda.groupby(
    'Producto')['Producto'].count().sort_values(ascending=False)
producto_mas_vendido2 = tienda2.groupby(
    'Producto')['Producto'].count().sort_values(ascending=False)
producto_mas_vendido3 = tienda3.groupby(
    'Producto')['Producto'].count().sort_values(ascending=False)
producto_mas_vendido4 = tienda4.groupby(
    'Producto')['Producto'].count().sort_values(ascending=False)

# Increased figure size for better visibility
fig, axs = plt.subplots(nrows=2, ncols=2, figsize=(15, 6))
ax, ax2, ax3, ax4 = axs.flat

# Example data
productos = pd.concat([producto_mas_vendido1.tail(
    5).sort_values(), producto_mas_vendido1.head(5).sort_values()])
nombres_productos = productos.index
puntuaciones = productos.values

productos2 = pd.concat([producto_mas_vendido2.tail(
    5).sort_values(), producto_mas_vendido2.head(5).sort_values()])
nombres_productos2 = productos2.index
puntuaciones2 = productos2.values

productos3 = pd.concat([producto_mas_vendido3.tail(
    5).sort_values(), producto_mas_vendido3.head(5).sort_values()])
nombres_productos3 = productos3.index
puntuaciones3 = productos3.values

productos4 = pd.concat([producto_mas_vendido4.tail(
    5).sort_values(), producto_mas_vendido4.head(5).sort_values()])
nombres_productos4 = productos4.index
puntuaciones4 = productos4.values

y_pos = np.arange(len(nombres_productos))

bars = ax.barh(y_pos, puntuaciones, align='center')
ax.set_yticks(y_pos, labels=nombres_productos)
ax.set_xlabel('Ventas')

bars2 = ax2.barh(y_pos, puntuaciones2, align='center')
ax2.set_yticks(y_pos, labels=nombres_productos2)
ax2.set_xlabel('Ventas')

bars3 = ax3.barh(y_pos, puntuaciones3, align='center')
ax3.set_yticks(y_pos, labels=nombres_productos3)
ax3.set_xlabel('Ventas')

bars4 = ax4.barh(y_pos, puntuaciones4, align='center')
ax4.set_yticks(y_pos, labels=nombres_productos4)
ax4.set_xlabel('Ventas')

ax.set_xlim(left=20)
ax2.set_xlim(left=20)
ax3.set_xlim(left=20)
ax4.set_xlim(left=20)

ax.set_title('Productos mas y menos vendidos Tienda 1')
ax2.set_title('Productos mas y menos vendidos Tienda 2')
ax3.set_title('Productos mas y menos vendidos Tienda 3')
ax4.set_title('Productos mas y menos vendidos Tienda 4')


# Add the values of each bar inside the bar
for idx, bar in enumerate(bars):
    width = bar.get_width()
    ax.text(width - 1, bar.get_y() + bar.get_height()/2,    # (x,y) position
            f'{str(puntuaciones[idx])[:4]}',
            ha='right', va='center', color='white', weight='bold')  # text alignment and style

for idx, bar in enumerate(bars2):
    width = bar.get_width()
    ax2.text(width - 1, bar.get_y() + bar.get_height()/2,    # (x,y) position
             f'{str(puntuaciones2[idx])[:4]}',
             ha='right', va='center', color='white', weight='bold')  # text alignment and style

for idx, bar in enumerate(bars3):
    width = bar.get_width()
    ax3.text(width - 1, bar.get_y() + bar.get_height()/2,    # (x,y) position
             f'{str(puntuaciones3[idx])[:4]}',
             ha='right', va='center', color='white', weight='bold')  # text alignment and style

for idx, bar in enumerate(bars4):
    width = bar.get_width()
    ax4.text(width - 1, bar.get_y() + bar.get_height()/2,    # (x,y) position
             f'{str(puntuaciones4[idx])[:4]}',
             ha='right', va='center', color='white', weight='bold')  # text alignment and style

plt.tight_layout()  # Adjust layout to prevent labels from being cut off
plt.show()
