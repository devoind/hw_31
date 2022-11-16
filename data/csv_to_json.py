import csv
import json

DATA_ADS = "ad.csv"
JSON_ADS = "ads.json"

DATA_CATEGORIES = "category.csv"
JSON_CATEGORIES = "categories.json"

DATA_LOC = 'location.csv'
JSON_LOC = 'locations.json'

DATA_USER = 'user.csv'
JSON_USER = 'users.json'


def run_convert(csv_file, json_file, model_name):
    result = []

    with open(csv_file, encoding='utf-8') as csv_f:
        for value in csv.DictReader(csv_f):
            to_add = {'model': model_name, 'pk': int(value['Id'] if 'Id' in value else value['id'])}
            if 'Id' in value:
                del value['Id']
            else:
                del value['id']
            if "location" in value:
                value['location'] = [int(value['location'])]

            if 'is_published' in value:
                if value['is_published'] == 'TRUE':
                    value['is_published'] = True
                else:
                    value['is_published'] = False
            if 'price' in value:
                value['price'] = int(value['price'])
            to_add['fields'] = value
            result.append(to_add)
    with open(json_file, 'w', encoding='utf-8') as json_f:
        json_f.write(json.dumps(result, ensure_ascii=False))


# run_convert(DATA_CATEGORIES, JSON_CATEGORIES, 'ads.category')
# run_convert(DATA_ADS, JSON_ADS, 'ads.ad')
# run_convert(DATA_LOC, JSON_LOC, 'users.location')
# run_convert(DATA_USER, JSON_USER, 'users.user')
