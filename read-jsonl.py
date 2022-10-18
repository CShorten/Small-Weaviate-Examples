import json

with open('products.jsonl', 'r') as json_file:
    json_list = list(json_file)

error_counter = 0
for json_str in json_list:
    try:
      result = json.loads(json_str)
      #short_descriptions.append(result["short_description"])
    except:
      error_counter += 1
