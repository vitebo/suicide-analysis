from model import MortalityDataService

service = MortalityDataService()
options_default = {
    'Linha': 'Categoria_CID-10',
    'SGrupo_CID-10': '245'
}
print(service.search(options_default).read())
