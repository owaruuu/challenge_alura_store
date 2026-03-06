import matplotlib.pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_1%20.csv"
url2 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_2.csv"
url3 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_3.csv"
url4 = "https://raw.githubusercontent.com/alura-es-cursos/challenge1-data-science-latam/refs/heads/main/base-de-datos-challenge1-latam/tienda_4.csv"

tienda = pd.read_csv(url)
tienda2 = pd.read_csv(url2)
tienda3 = pd.read_csv(url3)
tienda4 = pd.read_csv(url4)

calificacion_promedio1 = tienda['Calificación'].mean()
calificacion_promedio2 = tienda2['Calificación'].mean()
calificacion_promedio3 = tienda3['Calificación'].mean()
calificacion_promedio4 = tienda4['Calificación'].mean()

fig, ax = plt.subplots()

tiendas = ('Tienda 1', 'Tienda 2', 'Tienda 3', 'Tienda 4')
puntuaciones = [calificacion_promedio1, calificacion_promedio2,
                calificacion_promedio3, calificacion_promedio4]
bar_colors = ['tab:blue', 'tab:orange', 'tab:red', 'tab:blue']

bars = ax.bar(tiendas, puntuaciones, color=bar_colors)

ax.set_ylabel('Promedio Puntuacion')
ax.set_title('Promedio Puntuacion por Tienda')
ax.set_ylim(bottom=3, top=5)

# Add the values of each bar inside the bar
for idx, bar in enumerate(bars):
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height - 0.1,    # (x,y) position
            f'{str(puntuaciones[idx])[:4]}',
            ha='center', va='center', color='white', weight='bold')  # text alignment and style


plt.show()
