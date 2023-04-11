import csv

def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter = ',')    #-> itera con cada fila del csv
        header = next(reader)     #-> nos entrega una sola fila
        data = []
        # print(header)
        for row in reader:
            iterable = zip(header, row)
            # print(list(iterable))
            country_dict = {key: value for key, value in iterable}
            data.append(country_dict)
            # print('***' * 5)
            # print(row)
        return data 

if __name__ == '__main__':
    data = read_csv('data.csv')
    print(data[0])