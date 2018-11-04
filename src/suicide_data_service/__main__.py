from src.suicide_data_service.suicide_data_service import SuicideDataService

service = SuicideDataService()
data = service.search()
print(data)
