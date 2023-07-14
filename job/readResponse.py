from utils.httpUtil import WebRequests
from bs4 import BeautifulSoup



if __name__ == '__main__':
    response = WebRequests.get('https://www.autohome.com.cn/news/1/#liststart')
    soup = BeautifulSoup(response[1], 'lxml')
    div1 = soup.find(class_='article-wrapper')
    div_tags = soup.div
    for a_tag in div_tags:
        print(a_tag)
