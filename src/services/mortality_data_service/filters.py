from src.commons import utils


class Filters(object):

    def __init__(self):
        self.__FILES_YEARS_AVAILABLE = self.__make_files_years_available()
        self.__default = self.__get_filters_default()

    @property
    def default(self):
        return self.__default

    def __make_files_years_available(self):
        years = utils.get_years_available()
        return list(f'obtsp{year}.dbf' for year in years)

    def __get_filters_default(self):
        return {
            'Linha':                        'Município',
            'Coluna':                       '--Não-Ativa--',
            'Incremento':                   'Óbitos_p/Residênc',
            'Arquivos':                     self.__FILES_YEARS_AVAILABLE,
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

