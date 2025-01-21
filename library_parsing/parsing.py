import requests
from bs4 import BeautifulSoup as BS

URL = 'https://www.litres.ru/'

HEADERS = {
   "Accept": "*/*",
   "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Mobile Safari/537.36",
}

def get_html(url, params=''):
   request = requests.get(url, headers=HEADERS, params=params)
   return request



def clean_text(text):
   return ' '.join(text.split())

def get_data(html):
   bs = BS(html, features="html.parser")
   items = bs.find_all('div', class_='Art_content__ituUa Art_content_full___CBpM')
   book_list = []
   for item in items:
      info = clean_text(item.find('div', class_='ArtContent_wrapper__usfAJ ArtContent_wrapper_full__KVjA9').get_text())
      href = item.find('a').get('href')
      book_list.append(
         {
            'info': info,
            'href': href
         }
      )
   return book_list



def parsing():
   response = get_html(URL)
   if response.status_code == 200:
      book_list2 = []
      for page in range(1, 2):
         response = get_html("https://www.litres.ru/popular/", params={'page': page})
         book_list2.extend(get_data(response.text))
      return book_list2
   else:
      raise Exception('Error in parsing')




try:
   data = parsing()

   for item in data:
      print(f"Информация: {item['info']}")
      print(f"Ссылка: {item['href']}")
      print("-" * 40)

except Exception as e:
   print(f"Ошибка: {e}")
