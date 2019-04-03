import requests
from bs4 import BeautifulSoup
import pandas as pd
from pandas import ExcelWriter

def get_web_info(url):
    # Get a copy of the default headers that requests would use
    headers = requests.utils.default_headers()
    headers.update(
        {
            'User-Agent': 'My User Agent 1.0'
        }
    )
    resp = requests.get(url=url, headers=headers)

    if resp.status_code != 200:
        print('Invalid url:', resp.url)
        return None
    else:
        return resp.text

def get_591_first(dom):
    soup = BeautifulSoup(dom, 'html.parser')

    rows = soup.find('table').find_all('tr')

    data_df = pd.DataFrame()

    for index, row in enumerate(rows):
        if index == 0:
            row.text.strip()
            total = row.find('em')
            total = total.text.strip()

        elif index == 1:
            column_list = row.text.split()
            data_df = pd.DataFrame(columns=column_list)

        else:
            data_df.loc[str(index - 1)] = row.text.strip().split()

    return data_df, total


def get_591_info(dom):
    soup = BeautifulSoup(dom, 'html.parser')

    rows = soup.find('table').find_all('tr')

    data_df = pd.DataFrame()

    for index, row in enumerate(rows):
        if index == 0:
            row.text.strip()

        elif index == 1:
            column_list = row.text.split()
            data_df = pd.DataFrame(columns=column_list)

        else:
            # 大部分在執行中的錯誤，interpreter會以發起exception的方式來中斷程式，但我們其實常須控制產生例外的狀況。
            try:
                data_df.loc[str(index - 1)] = row.text.strip().split()
            # 若發生例外，後面的error型態會有很多種，如果沒有指定except後的物件型態，則他會捕捉所有引發的物件。
            # 像我們在程式中若發生錯誤，就會引發(raise)ValueError物件。
            except ValueError:
                continue
    return data_df


num_1 = 'https://www.591.com.tw/webService-market-1.html?firstRow='
num_2 = '&totalRows='
num_3 = '&type=1&sectionid=1&kind=1&orderType=desc&orderField=refreshtime'


def manage_url(n, total):
    return num_1 + n + num_2 + total + num_3

if __name__ == '__main__':
    writer = ExcelWriter('591_中正區.xlsx')
    first_page_url = 'https://www.591.com.tw/webService-market.html?regionid=1&sectionid=1&streetid=&kind=1&shape=0&year=0&type=1'
    first_web_info = get_web_info(first_page_url)
    data_df, total = get_591_first(first_web_info)
    appended_data = []
    appended_data.append(data_df)

    print(data_df)
    print('--------------------------------------------------------------------------------------')

    n = 20
    total = int(total)

    while(n < total):
        n = str(n)
        total = str(total)
        url = manage_url(n, total)

        page_info = get_web_info(url)
        page_df = get_591_info(page_info)

        appended_data.append(page_df)
        print(page_df)
        print('--------------------------------------------------------------------------------------')

        n = int(n)
        n += 20
        total = int(total)


    appended_data = pd.concat(appended_data, axis=0)
    appended_data.index = pd.RangeIndex(1, 1 + len(appended_data))
    print(appended_data)

    appended_data.to_excel(writer, '整層住家')
    writer.save()
