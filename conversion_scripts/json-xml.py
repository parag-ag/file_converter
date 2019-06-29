from json2xml import json2xml,readfromjson

data = readfromjson("/home/spider/Downloads/example_2.json")

data=json2xml.Json2xml(data).to_xml()

with open('output.txt', 'w+') as f:
    f.write(data)
os.remove("url")
