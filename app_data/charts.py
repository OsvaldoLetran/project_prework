import matplotlib.pyplot as plt


# def generate_bar_chart(name, labels, values):
def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_title('Population')
    ax.set_xlabel('Years')
    ax.set_ylabel('Count')
    plt.show()
    # plt.savefig(f'./imgs/{name}.png')   # concatenamos el nombre del pais, hacer mkdir imgs
    # plt.close()


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots(figsize=(8,8))
    ax.pie(values, labels = labels, rotatelabels = True, startangle=90, labeldistance = 0.9,   
        wedgeprops = {"linewidth": 1, "edgecolor": "white"})
    
    ax.set_title('Continent population percentage')
    ax.axis('equal')
    fig.tight_layout()
    plt.show()
    # plt.savefig('pie.png')
    # plt.close()


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 150, 85]
    generate_bar_chart(labels, values)
    # generate_pie_chart(labels, values)