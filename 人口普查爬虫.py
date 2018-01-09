import requests
from bs4 import BeautifulSoup

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 '
                      'Safari/537.36 '
    }


def get_url(url):
    web_data = requests.get(url=url, headers=headers)
    Soup = BeautifulSoup(web_data.content, 'lxml')
    data = Soup.find('ul')
    data = data.findAll('a')
    data_url = []
    data_name = []
    for item in data:
        data_url.append('http://www.stats.gov.cn/tjsj/pcsj/rkpc/6rp/{}'.format(item['href']))
        data_name.append(item.get_text())
    return data_url, data_name


def Download_data(url, name):
    for url_item, name_item in zip(url, name):
        print('正在下载{}。。。'.format(name_item))
        with open(r'data\{}.xls'.format(name_item), 'ab') as fl:
            fl.write(requests.get(url_item, headers=headers).content)

if __name__ == '__main__':
    url, name = get_url('http://www.stats.gov.cn/tjsj/pcsj/rkpc/6rp/lefte.htm')
    Download_data(url, name)