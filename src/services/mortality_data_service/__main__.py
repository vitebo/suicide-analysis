from model import MortalityDataService

service = MortalityDataService()
options_default = {
    'Coluna': 'Ano_do_Óbito',
    'Linha': 'Faixa_Etária',
    'SGrupo_CID-10': '245'
}
print(service.search(options_default).read())
