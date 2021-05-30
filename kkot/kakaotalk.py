import json
import requests
import keys as key


def kakaotalk(datas):
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    # text 전송
    # title = list()
    # for i in range(len(datas)):
    #     title.append(datas[i]['title'])
    # title = "\n".join(title)

    headers = {
        "Authorization": "Bearer " + key.token
    }

    # data = {
    #     "template_object" : json.dumps({ "object_type" : "text",
    #                                      "text" : str(title),
    #                                      "link" : {
    #                                                  "web_url" : "www.naver.com"
    #                                               }
    #     })
    # }
    template = {
        "object_type": "list",
        "header_title": "Today's news",
        "header_link": {
            "web_url": "www.naver.com",
            "mobile_web_url": "www.naver.com"
        },
        "contents": [
            {
                "title": datas[0]['title'],
                "description": datas[0]['description'],
                "image_url": datas[0]['urlToImage'],
                "image_width": 50, "image_height": 50,
                "link": {
                    "web_url": datas[0]['url'],
                    "mobile_web_url": datas[0]['url']
                }
            },
            {
                "title": datas[1]['title'],
                "description": datas[1]['description'],
                "image_url": datas[1]['urlToImage'],
                "image_width": 50, "image_height": 50,
                "link": {
                    "web_url": datas[1]['url'],
                    "mobile_web_url": datas[1]['url']
                }
            },
            {
                "title": datas[3]['title'],
                "description": datas[3]['description'],
                "image_url": datas[3]['urlToImage'],
                "image_width": 50, "image_height": 50,
                "link": {
                    "web_url": datas[3]['url'],
                    "mobile_web_url": datas[3]['url']
                }
            },
        ],
        "buttons": [
            {
                "title": "웹으로 이동",
                "link": {
                    "web_url": "google.com",
                    "mobile_web_url": "google.com"
                }
            }
        ]

    }
    data = {"template_object": json.dumps(template)}
    response = requests.post(url, headers=headers, data=data)
    print(response.status_code)
    if response.json().get('result_code') == 0:
        print('success')
    else:
        print('failed : ' + str(response.json()))
