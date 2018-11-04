import requests
from bs4 import BeautifulSoup


class SuicideDataService:

    def __init__(self):
        self.URL = 'http://tabnet.datasus.gov.br/cgi/tabcgi.exe'
        self.PARAMS = 'sim/cnv/obt10SP.def'
        self.HEADERS = {
            'user-agent': 'my-app'
        }
        self.filters_default = {
            'Linha':                        'Município',
            'Coluna':                       '--Não-Ativa--',
            'Incremento':                   'Óbitos_p/Residênc',
            'Arquivos':                     'obtsp16.dbf',
            'SMunicípio':                   'TODAS_AS_CATEGORIAS__',
            'SRegião_de_Saúde_(CIR)':       'TODAS_AS_CATEGORIAS__',
            'SMacrorregião_de_Saúde':       'TODAS_AS_CATEGORIAS__',
            'SDivisão_administ_estadual':   'TODAS_AS_CATEGORIAS__',
            'SMicrorregião_IBGE':           'TODAS_AS_CATEGORIAS__',
            'SRegião_Metropolitana_-_RIDE': 'TODAS_AS_CATEGORIAS__',
            'SCapítulo_CID-10':             'TODAS_AS_CATEGORIAS__',
            'SGrupo_CID-10':                'TODAS_AS_CATEGORIAS__',
            'SCausa_-_CID-BR-10':           'TODAS_AS_CATEGORIAS__',
            'SCausa_mal_definidas':         'TODAS_AS_CATEGORIAS__',
            'SFaixa_Etária':                'TODAS_AS_CATEGORIAS__',
            'SFaixa_Etária_OPS':            'TODAS_AS_CATEGORIAS__',
            'SFaixa_Etária_det':            'TODAS_AS_CATEGORIAS__',
            'SFx.Etária_Menor_1A':          'TODAS_AS_CATEGORIAS__',
            'SSexo':                        'TODAS_AS_CATEGORIAS__',
            'SCor/raça':                    'TODAS_AS_CATEGORIAS__',
            'SEscolaridade':                'TODAS_AS_CATEGORIAS__',
            'SEstado_civil':                'TODAS_AS_CATEGORIAS__',
            'SLocal_ocorrência':            'TODAS_AS_CATEGORIAS__',
            'formato':                      'prn'
        }

    def search(self, options=None):
        if options is None:
            options = {}
        request = requests.post(self.URL, params=self.PARAMS, data=self._create_data(options), headers=self.HEADERS)
        soup = BeautifulSoup(request.text, 'lxml')
        return soup.find('pre')

    def _create_categories(self):
        return ''.join([f'SCategoria_CID-10={i}&' for i in range(125, 150)])

    def _create_filter(self, options, key):
        if key in options:
            return f'{key}={options[key]}&'
        return f'{key}={self.filters_default[key]}&'

    def _create_data(self, options=None):
        if options is None:
            options = {}
        data = [self._create_filter(options, key) for key in self.filters_default]
        data = ''.join(data)
        return data + self._create_categories()
