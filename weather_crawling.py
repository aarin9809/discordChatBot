# import requests
# from bs4 import BeautifulSoup
# import discord

# url = 'https://www.weather.go.kr/w/weather/forecast/short-term.do?stnId=109'

# response = requests.get(url)

# soup = BeautifulSoup(response.content, 'html.parser')

# weather_info = soup.find('div', class_='weather_info')

# weather_status = weather_info.find('span', class_='weather_status').text

# weather_image = weather_info.find('img', class_='weather_image')['src']

# if weather_status in '맑음':
#     weather_image = 'https://i.imgur.com/e239o3t.png'
# elif weather_status in '흐림':
#     weather_image = 'https://i.imgur.com/976764c.png'
# elif weather_status in '비':
#     weather_image = 'https://i.imgur.com/758900a.png'