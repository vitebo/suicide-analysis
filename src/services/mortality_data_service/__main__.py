from model import MortalityDataService

service = MortalityDataService()
print(service.search().read())
