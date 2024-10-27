# 오늘 서울 날씨를 현재날씨 뽑아서 디코에서 /weather를 입력하면 오늘 전체 날씨를 알려주는 봇을 만들기
import requests
from bs4 import BeautifulSoup

url = 'https://www.weather.go.kr/w/weather/forecast/short-term.do?stnId=109'

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    s = soup.select('#after-dfs-forecast > div:nth-child(1) > section > div.cmp-view-content')
    today = soup.select('#after-dfs-forecast > div:nth-child(1) > section > div.cmp-view-content > p > span:nth-child(2)')
    # print(today[0].text)
else:
    print(response.status_code)


def weather(text):
    url = "https://www.weather.go.kr/w/weather/forecast/short-term.do?stnId=109"
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
        soup = BeautifulSoup(html, 'html.parser')
        cmd = {
            "today": "#after-dfs-forecast > div:nth-child(1) > section > div.cmp-view-content > p > span:nth-child(2)",
            "tomo": "#after-dfs-forecast > div:nth-child(1) > section > div.cmp-view-content > p > span:nth-child(3)",
            "dato": "#after-dfs-forecast > div:nth-child(1) > section > div.cmp-view-content > p > span:nth-child(4)"
        }
        if text in cmd.keys():
            elements = soup.select(cmd[text])
            if elements:
                return elements[0].text
            else:
                return "날씨 정보를 찾을 수 없습니다. 선택자가 맞는지 확인해주세요."
        else:
            return "올바른 명령어를 입력하세요. (예: today, tomo, dato)"
    else:
        print(response.status_code)
        return "날씨 데이터를 가져오지 못했습니다. 상태 코드: " + str(response.status_code)