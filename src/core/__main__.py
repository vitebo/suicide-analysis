from src.core.suicide_data_service import SuicideDataService

service = SuicideDataService()
content = service.search()
print(content)
