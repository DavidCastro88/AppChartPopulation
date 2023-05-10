import matplotlib.pyplot as plt

def generate_bar_chart(labels,valores):
    fig,ax=plt.subplots()
    ax.bar(labels,valores)
    plt.show()


if __name__=='__main__':
    labels=['a','b','c']
    valores=[100,200,80]
    generate_bar_chart(labels,valores)