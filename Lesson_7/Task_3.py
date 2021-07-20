import requests
import json
import datetime


def get_data_meteo():
    r = requests.get("http://api.openweathermap.org/data/2.5/forecast/daily?q=Odessa&cnt=5&units=metric&appid=f9ada9efec6a3934dad5f30068fdcbb8", params={'adwd': 'requests'})
    return r.json()
    #print(r.text)
# get_data_meteo()
# print(r.json())
#date = datetime.datetime.fromtimestamp(1600419600)

def save_data(data, filename='default'):
    with open(f'{filename}.text', 'w') as file:
        file.write(str(data))

# def get_file_name(data):
#     return '-'.join([f'{k}-{v}' for k, v in data['args'].items()])

def collect_data_meteo() -> list:
    return list(enumerate(range(100, 1000, 10)))

def data_preparation(data) -> list:
    return [str(i) for i in data]


def daytime_meteo():
    ....
    print(now.strftime('%d-%m-%Y')


def text_colomns():
    text_words = text_meteo.split()
    with open('default', 'w') as file:
        for line in text_words:
            justified_line = line.ljust(20) + line + '\n'
            file.write(justified_line + '\n')


def main():
    data = get_data_meteo()
    filename = get_file_name(data)
    print(collect_data_meteo())
    save_data(data_preparation(data), filename=filename)
    text_colomns()



main()
# print(r.json())
# print(r.headers)
# print(r.content)
# print(dir(r))