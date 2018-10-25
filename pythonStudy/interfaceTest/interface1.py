import requests

url = 'http://api.douban.com/v2/movie/top250'
r = requests.get(url, params={'start': 1, 'count': 25})
print(r)
res = r.json()
for movie in res['subjects']:
    print(movie['title'])
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
'''
with open('rawtext.tiff', 'wb') as fd:
    for chunk in rs.iter_content(chunk_size=240, decode_unicode=True):
        fd.write(chunk)
'''
headers = {'user-agent': 'my-app/0.0.1'}
r = requests.get(url, headers=headers)
print(r.status_code)  # 响应状态码
print(r.status_code == requests.codes.ok)  # requests内置的状态码查询
bad_r = requests.get('http://api.douban.com/v2/movie/top250')
print(bad_r.status_code)
print(bad_r.raise_for_status())
print(r.headers)
print(r.headers['connection'])


