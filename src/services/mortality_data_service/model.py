from io import StringIO

import requests
from bs4 import BeautifulSoup
from filters import get_filters_default


class MortalityDataService:

    def __init__(self):
        self.__URL = 'http://tabnet.datasus.gov.br/cgi/tabcgi.exe'
        self.__PARAMS = 'sim/cnv/obt10SP.def'
        self.__HEADERS = {
            'user-agent': 'my-app'
        }
        self.__filters_default = get_filters_default()

    def search(self, options=None):
        data = self.__create_data(options)
        request = requests.post(self.__URL, params=self.__PARAMS, headers=self.__HEADERS, data=data)
        soup = BeautifulSoup(request.text, 'lxml')
        content = soup.find('pre')
        return StringIO(content.text[:-3])

    def __create_filter(self, options, key):
        if key not in options:
            return f'{key}={self.__filters_default[key]}&'
        if type(options[key]) == str:
            return f'{key}={options[key]}&'
        return ''.join([f'{key}={value}&' for value in options[key]])

    def __create_data(self, options=None):
        if options is None:
            options = {}
        return ''.join([self.__create_filter(options, key) for key in self.__filters_default])
