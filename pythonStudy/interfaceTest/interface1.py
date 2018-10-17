import requests
url = 'http://api.douban.com/v2/movie/top250'
r = requests.get(url, params={'start': 1, 'count': 25})
print(r)
res = r.json()
for movie in res['subjects']:
    print(movie['title'])
