from unicodedata import name
import requests
import json

dataset_url = "https://data.telangana.gov.in/api/1/search/facets?fulltext=&page=1&page-size=10&sort=modified&sort-order=desc&theme={sector}&facets=theme"
schemas_url = "https://data.telangana.gov.in/api/1/metastore/schemas/theme/items"

class Sectors:
    def set_identifier(self):
        try : 
            res = requests.get(schemas_url)
            for eachdata in res.json():
                if eachdata["data"] == self.name :
                    return eachdata["identifier"]
        except:
            raise "Unable to request"
        raise "datasets is not available"

    def get_all_datasets(self):
        try : 
            res = requests.get(self.url)
            data = res.json()["results"]
            return data
        except :
            raise "Unable to request"

    def __init__(self) -> None:
        self.name = self.__class__.__name__
        self.identifier = self.set_identifier()
        self.url = dataset_url.format(sector=self.name)
        self.data = self.get_all_datasets()

    def get_data():
        pass

class Administration(Sectors):
    def get_data():
        pass

class Agriculture(Sectors):
    def get_data():
        pass

class AnimalHusbandryLiveStock(Sectors):
    def get_data():
        pass

class Automobile(Sectors):
    def get_data():
        pass

class Energy(Sectors):
    def get_data():
        pass

class GTFS(Sectors):
    def get_data():
        pass

class Industries(Sectors):
    def get_data():
        pass

class Irrigation(Sectors):
    def get_data():
        pass

class TourismAndCulture(Sectors):
    def get_data():
        pass

class Transportation(Sectors):
    def get_data():
        pass

class Urban(Sectors):
    def get_data():
        pass

class WaterQuality(Sectors):
    def get_data():
        pass

class BankingAndFinanace(Sectors):
    def get_data():
        pass

class Commerce(Sectors):
    def get_data():
        pass
class Education(Sectors):
    def get_data():
        pass

class Fishers(Sectors):
    def get_data():
        pass

class Food(Sectors):
    def get_data():
        pass

class Forest(Sectors):
    def get_data():
        pass

class Handlooms(Sectors):
    def get_data():
        pass

class Health(Sectors):
    def get_data():
        pass

class HomeAffairsAndEnforcement(Sectors):
    def get_data():
        pass

class Horticulture(Sectors):
    def get_data():
        pass

class Hospitality(Sectors):
    def get_data():
        pass

if __name__ == "__main__" :
    hs = Transportation()
    print(hs.identifier)
    x = hs.data
    print(hs.data)