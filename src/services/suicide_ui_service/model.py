from src.services.mortality_data_service.model import MortalityDataService
import matplotlib.pyplot as plt
from src.commons import utils
import pandas


class SuicideUiService(object):

    def __init__(self):
        pandas.set_option('display.max_rows', None)
        pandas.set_option('display.max_columns', None)
        pandas.set_option('display.max_colwidth', -1)
        pandas.set_option('display.colheader_justify', 'left')
        self.SERVICE = MortalityDataService()
        self.OPTIONS_DEFAULT = {
            'SGrupo_CID-10': '245'
        }

    def get_most_used_method(self):
        data = self.__search({
            'Linha': 'Categoria_CID-10'
        })
        data = data.drop(25, 0)
        data = data.set_index('Categoria CID-10')
        data.index = [f'X {label[1:3]}' for label in data.index]
        data.columns = ['Total']
        return data.plot(kind='bar')

    def get_year_with_higher_x70(self):
        data = self.__search({
            'Linha': 'Ano_do_Óbito',
            'Coluna': 'Capítulo_CID-10',
            'SCategoria_CID-10': '1835'
        })
        data = data.drop(21, 0).drop(columns=['Cap XX'])
        data = data.set_index('Ano do Óbito')
        return data.plot()

    def get_sex_with_highest_index_using_x70_in_2015(self):
        data = self.__search({
            'Linha': 'Sexo',
            'Arquivos': 'obtsp15.dbf',
            'SCategoria_CID-10': '1835',
        })
        data = data.drop(2, 0)
        data.columns = ['Sexo', 'Total']
        df = pandas.DataFrame({'Sexo': data['Total'].tolist()}, index=['Masculino', 'Feminino'])
        return df.plot(kind='pie', subplots=True)

    def get_age_range_x70_in_2015(self):
        data = self.__search({
            'Linha': 'Faixa_Etária',
            'Arquivos': 'obtsp15.dbf',
            'SCategoria_CID-10': '1835',
            'SSexo': '1'
        })
        data = data.drop(10, 0)
        data.columns = ['Faixa etária', 'Total']
        data = data.set_index('Faixa etária')
        return data.plot(kind='barh')

    @staticmethod
    def get_description_x60_x84():
        content = {
            'Legenda': list(f'X {i}' for i in range(60, 85)),
            'Descrição': [
                'Analgésicos, antipiréticos e anti-reumáticos',
                'Drogas anticonvulsivantes, sedativos, hipnóticos, antiparkinsonianos e psicotrópicos',
                'Narcóticos e psicodislépticos',
                'Outras substâncias farmacológicas de ação sobre o sistema nervoso autônomo',
                'Outras drogas, medicamentos e substâncias biológicas e às não especificadas',
                'Voluntária por álcool',
                'Solventes orgânicos, hidrocarbonetos halogenados e seus vapores',
                'Outros gases e vapores',
                'Pesticidas',
                'Outros produtos químicos e substâncias nocivas não especificadas',
                'Enforcamento, estrangulamento e sufocação',
                'Afogamento e submersão',
                'Disparo de arma de fogo de mão',
                'Disparo de espingarda, carabina, ou arma de fogo de maior calibre',
                'Disparo de outra arma de fogo e de arma de fogo não especificada',
                'Dispositivos explosivos',
                'Fumaça, fogo e chamas',
                'Vapor de água, gases ou objetos quentes',
                'Objeto cortante ou penetrante',
                'Objeto contundente',
                'Precipitação de um lugar elevado',
                'Precipitação ou permanência diante de um objeto em movimento',
                'Impacto de um veículo a motor',
                'Outros meios especificados',
                'Meios não especificados'
            ]
        }
        data = pandas.DataFrame(data=content)
        data = data.style.set_properties(**{'text-align': 'left'})
        return data

    def __search(self, options):
        options.update(self.OPTIONS_DEFAULT)
        content = self.SERVICE.search(options)
        return pandas.read_csv(content, sep=';')
