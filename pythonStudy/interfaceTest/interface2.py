import requests


url = "https://sdfw.rrkd.cn/api/incidentally/shoptripbrand/brandShopDetail"
data = {"brandId": "1", "lat": "22.547000", "lng": "114.085947", "cityName": "深圳市"}
r = requests.post(url, json=data, verify=False)

print(r.status_code)
print(r.text)
#print(r.headers)
res = r.json()
#print(r.request.headers)
for addr in res['result']['jsonObject']['selectiveShop']:
    print(addr['destAddress'])
