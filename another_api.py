from covid.api import CovId19Data

api = CovId19Data(force=False)

latest = api.get_stats() # {'confirmed': 720117, 'recovered': 149082, 'deaths': 33925, 'last_updated': '2020-03-29 00:00:00'}

all_countries = api.get_all_records_by_country()

russia = api.filter_by_country("russia")

print(russia)
print(type(russia))