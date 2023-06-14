import utils
import read_csv
import charts
import pandas as pd


def run():
    data = read_csv.read_csv('data.csv')

    country = input('Type country -> ')
    # print(country)
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        # print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)
        # charts.generate_bar_chart(country['Country/Territory'], labels, values)


    # data = list(filter(lambda item : item['Continent'] == 'Oceania',data))    
    # countries = list(map(lambda x: x['Country/Territory'], data))
    # percentages = list(map(lambda x: x['World Population Percentage'], data))
    # charts.generate_pie_chart(countries, percentages)


    df = pd.read_csv('data.csv')
    df = df[df['Continent'] == 'Africa']
    # """reasigna el valor de df a una versión filtrada que solo contiene
    #    las filas donde la columna ‘Continent’ tiene el valor ‘Africa’
    # """
    countries = df['Country/Territory'].values
    percentages = df['World Population Percentage'].values
    charts.generate_pie_chart(countries, percentages)


if __name__ == '__main__':
    run()