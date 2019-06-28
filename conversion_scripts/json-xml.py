from json2xml import json2xml, readfromurl

#converting json to xml
data = readfromurl("https://coderwall.com/vinitcool76.json")
data = json2xml.Json2xml(data).to_xml()
print(data)

