from read_csv import read_csv
from charts import generate_bar_chart as chart


country=input('Ingrese el pais que desea buscar: ')
def generate_population_chart_by_country(country):
    #Get data of Population history for countries
    data=read_csv('app/data.csv')
    try:
        #We filter the country to consult in a list with a single dictionary
        data_country=list(filter(lambda x:x['Country/Territory']==country,data))[0]
        #We get only the keys we need, which have the values of the population in years
        dic_final={key[0:4:]:data_country[key] for key in data_country if ('Population' in key and 'World' not in key)}
        #We invert the dictionary so that the population is seen in ascending order
        dic_final = dict(reversed(list(dic_final.items())))
        chart(dic_final.keys(),dic_final.values())
    except:
        print('The country has not been found')

generate_population_chart_by_country(country)

