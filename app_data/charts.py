# https://python-charts.com/es/ranking/grafico-barras-matplotlib/
# https://matplotlib.org/stable/tutorials/introductory/pyplot.html

import matplotlib.pyplot as plt

# def generate_bar_chart(name, labels, values):
def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()
    # plt.savefig(f'./imgs/{name}.png')   # concatenamos el nombre del pais, hacer mkdir imgs
    # plt.close()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis('equal')
    plt.show()
    # plt.savefig('pie.png')
    # plt.close()


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 150, 85]
    generate_bar_chart(labels, values)
    # generate_pie_chart(labels, values)