from services.mortality_data_service.model import MortalityDataService
import pandas


class SuicideUiService(object):

    def __init__(self):
        pandas.set_option('display.max_rows', None)
        pandas.set_option('display.max_columns', None)
        pandas.set_option('display.max_colwidth', -1)
        self.SERVICE = MortalityDataService()
        self.OPTIONS_DEFAULT = {
            'SGrupo_CID-10': '245'
        }

    def get_year_with_higher_index(self):
        data = self.__search({
            'Linha': 'Ano_do_Óbito',
            'Coluna': 'Capítulo_CID-10'
        })
        table = data.drop(21, 0).drop(columns=['Cap XX'])
        return table.plot(x='Ano do Óbito', kind='bar', title='Hitórico de suicidios por ano')

    def get_most_used_method_in_2015(self):
        data = self.__search({
            'Linha': 'Categoria_CID-10',
            'Coluna': 'Ano_do_Óbito',
            'Arquivos': 'obtsp15.dbf'
        })
        table = data.drop(24, 0).drop(columns=['Total'])
        return table.plot(x='Categoria CID-10', y='2015', kind='barh')

    def get_sex_with_highest_index_using_x70_in_2015(self):
        data = self.__search({
            'Linha': 'Sexo',
            'Arquivos': 'obtsp15.dbf',
            'SCategoria_CID-10': '1835',
        })
        table = data.drop(2, 0)
        table.columns = ['Sexo', 'Total']
        return table.plot(kind='bar', x='Sexo')

    def __search(self, options):
        options.update(self.OPTIONS_DEFAULT)
        content = self.SERVICE.search(options)
        return pandas.read_csv(content, sep=';')
