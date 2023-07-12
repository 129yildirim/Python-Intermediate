import json


# JSON string to dict
with open('example_file2.json') as f:
    dict_2 = json.load(f)
    print('type of dict2:', type(dict_2))
    print('dict2: ', dict_2)
    print('searcing in dict_2 as a dict: ', dict_2['quiz']['sport']['q1']['options'])
    
print('\n')
# dict to JSON 
#  since dict_2 now is a dict. We can try to convert it to str(dumps) or json(dump)
# dict to str
dict_1 = json.dumps(dict_2)
print('type of dict1: ', type(dict_1))
print('dict1: ', dict_1)

#dict to json file
with open('example_file1.json', 'w') as f:
    json.dump(dict_2, f, indent=4, sort_keys=True)

    
    

