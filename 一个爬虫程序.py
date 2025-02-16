import requests

url = "http://www.tianmao.com"
resp = requests.get(url)
#with open("aqiyi.html",mode="w",encoding="utf-8") as faa:
 #   faa.write(resp.text)
resp.encoding = "utf-8"
with open("tianmao.html",mode="w") as fff:
    fff.write(resp.text)
print('bye')