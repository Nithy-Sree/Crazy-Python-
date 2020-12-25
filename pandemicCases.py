# pip install covid
from covid import Covid

cases = Covid()

def covid_worldwide():
    print(f"Active cases : {cases.get_total_active_cases()}")
    print(f"Confirmed cases : {cases.get_total_confirmed_cases()}")
    print(f"Recovered : {cases.get_total_recovered()}")
    print(f"Deaths : {cases.get_total_deaths()}")

print("WORLD WIDE CASES")
covid_worldwide()

print("------------------")

# List of countries available
# for country in covid.list_countries():
#     print(country['name'])

# in specifc country
country = input("Enter the country name: ").strip()

datas = cases.get_status_by_country_name(country)

data = {
    key: datas[key]
    for key in datas.keys() and {'confirmed', 'active', 'deaths', 'recovered'}
}

# printing the data
print(data)
