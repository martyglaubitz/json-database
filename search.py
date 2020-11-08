import json

def parse_query(query: str):
    query_object = json.loads(query)

    

def make_name_matcher(propertyName: str, value): 
    if propertyName == '*':
        return lambda index_entry: index_entry['value'] == value
