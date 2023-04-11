import matplotlib.pyplot as plt


def generate_pie_chart():
    labels = ['A', 'B', 'C']
    values = [200, 55, 120]

    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    plt.show()
    # plt.savefig('pie.png')    # para guardar el pie chart en una imagen png
    # plt.closse()