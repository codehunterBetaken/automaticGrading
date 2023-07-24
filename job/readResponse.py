from utils.httpUtil import WebRequests
from bs4 import BeautifulSoup
import json
import ast



if __name__ == '__main__':

    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "Token": ""
    }
    cookies = {
        'edu_collect_sdk_idxId&devIdBRN44YaIO73': ''
    }
    data = {'pageIndex': 1}
    response = WebRequests.post('',headers=headers, cookies=cookies, data=data)

    # soup = BeautifulSoup(response[1], 'lxml')
    print(response[1])
    json_dumps = json.loads(json.dumps(response[1]))
    print(json.loads(json_dumps['message']))
    # div1 = soup.find(class_='article-wrapper')
    # div_tags = soup.div
    # for a_tag in div_tags:
    #     print(a_tag)
