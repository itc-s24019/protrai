#s24019
#自分なりのコードの書き方で課題をやってみた 2024/08/05

import requests
from bs4 import BeautifulSoup

def get_population_data():
    url = "https://www.pref.okinawa.jp/toukeika/estimates/estimates_suikei.html"
    response = requests.get(url)
    
    # 文字化け対策
    response.encoding = 'shift_jis'
    
    soup = BeautifulSoup(response.text, 'lxml')
    
    # 必要なデータを抽出
    tables = soup.find_all('table', class_='table1')
    population_data = tables[0].find_all('tr')
    
    # データを辞書に格納
    data = {
        "総人口": population_data[0].find_all('td')[1].get_text().strip(),
        "男": population_data[1].find_all('td')[1].get_text().strip(),
        "女": population_data[2].find_all('td')[1].get_text().strip(),
    }
    
    return data

def main():
    data = get_population_data()
    print("沖縄県の推計人口")
    print(f"総人口: {data['総人口']}")
    print(f"男: {data['男']}")
    print(f"女: {data['女']}")

if __name__ == "__main__":
    main()
