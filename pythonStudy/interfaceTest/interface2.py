import requests


#url = "https://sdfw.rrkd.cn/api/incidentally/shoptripbrand/brandShopDetail"
url = "https://sdfw.rrkd.cn/api/incidentally/shoptripbrand/shopDetail"

#data = {"brandId": "1", "lat": "22.547000", "lng": "114.085947", "cityName": "深圳市"}
data = {"shopId":172,"tripId":11479,"userId":31}
'''
r = requests.post(url, json=data, verify=False)

print(r.status_code)
print(r.text)
#print(r.headers)
res = r.json()
#print(r.request.headers)
for addr in res['result']['jsonObject']['selectiveShop']:
    print(addr['destAddress'])

with requests.post(url, json=data, verify=False, stream=True) as r:

    res = r.json()
    for addr in res['result']['jsonObject']['selectiveShop']:
        print(addr['destAddress'])
'''
with requests.post(url, json=data, verify=False) as r:
    res = r.json()
    for addr in res['result']['jsonObject']['shopDetailGood']:
        print(addr['brandName'])

