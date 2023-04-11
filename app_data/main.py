import utils
import read_csv
import charts


def run():
    data = read_csv.read_csv('data.csv')
    
    # data = list(filter(lambda item : item['Continent'] == 'Oceania',data))
    
    # countries = list(map(lambda x: x['Country/Territory'], data))
    # percentages = list(map(lambda x: x['World Population Percentage'], data))
    # charts.generate_pie_chart(countries, percentages)

    country = input('Type country -> ')
    # print(country)
    result = utils.population_by_country(data, country)

    if len(result) > 0:
        country = result[0]
        # print(country)
        labels, values = utils.get_population(country)
        charts.generate_bar_chart(labels, values)
        # charts.generate_bar_chart(country['Country/Territory'], labels, values)


if __name__ == '__main__':
    run()