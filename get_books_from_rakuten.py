import requests
import json
import time

URL = "https://app.rakuten.co.jp/services/api/BooksTotal/Search/20170404"

payload = {
    'format':'json',
    'applicationId':'[Rakuten App ID]',
    'booksGenreId':'000',
    'keyword':'Python',
    'page':1
}

books = []
while True:
    response = requests.get(URL,params=payload)
    data = json.loads(response.text)
    books.extend(data['Items']) # extend => 配列に要素を追加
    if data['pageCount'] == data['page']:
        break
    payload['page'] = data['page'] + 1
    time.sleep(1)

'''
APIから返ってくるJSONデータ：こんな感じ
  "count": 244,
  "page": 1,　1度のリクエストで30件しか返ってこない。244件あるので全部で9ページになる。
  "first": 1,
  "last": 30,
  "hits": 30,
  "carrier": 0,
  "pageCount": 9, 全ページ数
  "Items": [
      "Item": {
          "titel": ...,
          "subtitle": ...,
          ...,
          ...,
      }
      ]
'''

with open('rakuten_books.json','w') as f:
    json.dump(books,f)
