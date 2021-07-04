import pandas as pd
from core import models as core_models
from store import models as store_models
from itertools import islice

def uploadcity():
    csv_file = "/mnt/d/Django/CRM/DATA/city.csv"

    csv = pd.read_csv(csv_file)
    city = csv["city"]
    state = csv["state"]
    country_obj = core_models.Country.objects.get_or_create(name="India",mobile_code = "+91")[0]
    for row in range(700):
        core_models.Cities.objects.create(
            state=core_models.State.objects.get_or_create(country = country_obj,name=state[row].title())[0],
            name=city[row].title(),
            display_name=city[row].title() + ", " + state[row].title(),
        )

    print(core_models.Cities.objects.all().count())

# def uploadstore():
csv_file = "/mnt/d/Django/CRM/DATA/Gorakhpur_CS.csv"

reader = pd.read_csv(csv_file, encoding="latin-1")
# reader = reader.dropna()

phone_numbers = reader["contact"]
name = reader["storage_name"]
fulladdr = reader["address"]
district = reader["city"]
manager_name = reader["manager_name"]

for row in range(len(phone_numbers)):
    city_obj = core_models.Cities.objects.get_or_create(name=district[row])[0]
    
    store = store_models.Store.objects.create(
        name = name[row].title(),
        # query = query[row],
        # latitude = latitude[row],
        # logitude = logitude[row],
        phone_number = phone_numbers[row],
        city = city_obj,
        fulladdr = fulladdr[row],
        # categories = categories[row],
        # url = url[row],
        # addr1 = addr1[row],
        # addr2 = addr2[row],
        # addr3 = addr3[row],
        # addr4 = addr4[row],
        district = district[row].title(),
        manager = manager_name[row]
    )
    print(city_obj,store)

# uploadstore()