import matplotlib.pyplot as plt

convert_number = lambda number: int(str(number)[0] + ((len(str(number)) - 1) * '0'))

def generate_bar_chart(labels, valores, country=None):
    fig = plt.figure(figsize=(10, 5))
    plt.bar(labels, valores, edgecolor='black', linewidth=1.5)
    plt.title(f'Population in {country} in the last 50 years')
    plt.xlabel('Year')
    plt.ylabel('Population(People)')
    plt.rcParams['font.family'] = 'monospace'
    plt.legend(['Population'])
    plt.ticklabel_format(style='plain', axis='y') # Desactiva notación científica en el eje Y
    plt.ylim(convert_number(list(valores)[0]))
    plt.show()


if __name__=='__main__':
    labels=['a','b','c']
    valores=[100,200,80]
    generate_bar_chart(labels,valores)