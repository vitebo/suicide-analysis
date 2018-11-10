import requests
from bs4 import BeautifulSoup


class SuicideDataService:

    def __init__(self, options):
        self.__URL = 'http://tabnet.datasus.gov.br/cgi/tabcgi.exe'
        self.__PARAMS = 'sim/cnv/obt10SP.def'
        self.__HEADERS = {
            'user-agent': 'my-app'
        }
        self.__filters_default = {
            'Linha': 'Município',
            'Coluna': '--Não-Ativa--',
            'Incremento': 'Óbitos_p/Residênc',
            'Arquivos': 'obtsp16.dbf',
            'SMunicípio': 'TODAS_AS_CATEGORIAS__',
            'SRegião_de_Saúde_(CIR)': 'TODAS_AS_CATEGORIAS__',
            'SMacrorregião_de_Saúde': 'TODAS_AS_CATEGORIAS__',
            'SDivisão_administ_estadual': 'TODAS_AS_CATEGORIAS__',
            'SMicrorregião_IBGE': 'TODAS_AS_CATEGORIAS__',
            'SRegião_Metropolitana_-_RIDE': 'TODAS_AS_CATEGORIAS__',
            'SCapítulo_CID-10': 'TODAS_AS_CATEGORIAS__',
            'SGrupo_CID-10': 'TODAS_AS_CATEGORIAS__',
            'SCausa_-_CID-BR-10': 'TODAS_AS_CATEGORIAS__',
            'SCausa_mal_definidas': 'TODAS_AS_CATEGORIAS__',
            'SFaixa_Etária': 'TODAS_AS_CATEGORIAS__',
            'SFaixa_Etária_OPS': 'TODAS_AS_CATEGORIAS__',
            'SFaixa_Etária_det': 'TODAS_AS_CATEGORIAS__',
            'SFx.Etária_Menor_1A': 'TODAS_AS_CATEGORIAS__',
            'SSexo': 'TODAS_AS_CATEGORIAS__',
            'SCor/raça': 'TODAS_AS_CATEGORIAS__',
            'SEscolaridade': 'TODAS_AS_CATEGORIAS__',
            'SEstado_civil': 'TODAS_AS_CATEGORIAS__',
            'SLocal_ocorrência': 'TODAS_AS_CATEGORIAS__',
            'formato': 'prn'
        }
        print(self.__create_data(options))

    def search(self, options=None):
        data = self.__create_data(options)
        request = requests.post(self.__URL, params=self.__PARAMS, headers=self.__HEADERS, data=data)
        soup = BeautifulSoup(request.text, 'lxml')
        return soup.find('pre')

    @staticmethod
    def __create_filter_categories():
        return ''.join([f'SCategoria_CID-10={i}&' for i in range(125, 150)])

    def __create_filter(self, options, key):
        if key not in options:
            return f'{key}={self.__filters_default[key]}&'
        if not isinstance(options[key], list):
            return f'{key}={options[key]}&'
        return ''.join([f'{key}={value}&' for value in options[key]])

    @staticmethod
    def __format_to_two_decimal_place(number):
        return f'0{number}' if number < 10 else number

    def __create_data(self, options=None):
        if options is None:
            options = {}
        data = ''.join([self.__create_filter(options, key) for key in self.__filters_default])
        return data + self.__create_filter_categories()
