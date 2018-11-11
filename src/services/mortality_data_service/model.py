import requests
from bs4 import BeautifulSoup
from io import StringIO
from services.mortality_data_service.filters import Filters


class MortalityDataService(object):

    def __init__(self):
        self.__FILTERS = Filters()
        self.__URL = 'http://tabnet.datasus.gov.br/cgi/tabcgi.exe'
        self.__PARAMS = 'sim/cnv/obt10SP.def'
        self.__HEADERS = {
            'user-agent': 'my-app'
        }

    def search(self, options=None):
        data = self.__create_data(options)
        request = requests.post(self.__URL, params=self.__PARAMS, headers=self.__HEADERS, data=data)
        soup = BeautifulSoup(request.text, 'lxml')
        content = soup.find('pre')
        return StringIO(content.text[:-3])

    def __create_data(self, options):
        if options is None:
            options = {}
        return ''.join([self.__create_filter(options, key) for key in self.__FILTERS.default])

    def __create_filter(self, options, key):
        if key not in options:
            return self.__create_default_filter(key)
        return self.__create_custom_filter(options, key)

    def __create_default_filter(self, key):
        filter_value = self.__FILTERS.default[key]
        if type(filter_value) == str:
            return f'{key}={filter_value}&'
        return ''.join([f'{key}={value}&' for value in filter_value])

    @staticmethod
    def __create_custom_filter(options, key):
        filter_value = options[key]
        if type(filter_value) == str:
            return f'{key}={filter_value}&'
        return ''.join([f'{key}={value}&' for value in filter_value])
