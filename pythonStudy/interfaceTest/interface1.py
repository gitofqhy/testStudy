import requests
import json
url = 'http://api.douban.com/v2/movie/top250'
r = requests.get(url, params={'start': 1, 'count': 25})
print(r)
print(r.url)
res = r.json()
for movie in res['subjects']:
    print(movie['title'])
'''
rp = requests.post(url, data={'start': 1, 'count': 25})
print(rp.url)  # post
print(r.url)   # get
print(r.text)  # 响应内容
print(r.encoding)  # 响应文本编码
r.encoding = 'ISO-8859-1'  # 修改编码
print(r.encoding)
r.encoding = 'utf-8'
print(r.content)  # 二进制响应内容
print(r.json())   # json响应内容
print(r.raise_for_status())  # 检查请求是否成功
print(r.status_code)  # 检查请求是否成功

rs = requests.get(url, stream=True)
print(rs.raw)   # 原始响应内容
print(rs.raw.read(10))


headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(r.status_code)  # 响应状态码
print(r.status_code == requests.codes.ok)  # requests内置的状态码查询
bad_r = requests.get('http://api.douban.com/v2/movie/top250')
print(bad_r.status_code)
print(bad_r.raise_for_status())
print(r.headers)
print(r.headers['connection'])

'''
dict_a = {"k1":"v1", "k2":"v2"}
x = json.dumps(dict_a)
print(x)
print(type(x))
y = json.loads(x)
print(y)
print(type(y))
x1 = json.dumps(y)
print(x1)
print(type(x1))