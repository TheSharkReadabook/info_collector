import requests
import json
from json import JSONEncoder
import numpy


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, numpy.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)


def kakaotalk(db_result):
    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'

    headers = {"Authorization": "Bearer <token>"}

    post = {
        "object_type": "text",
        "text": db_result,
        "link": {
                "web_url": "https://developers.kakao.com",
                "mobile_web_url": "https://developers.kakao.com"
            },
        "button_title": "submit"
    }

    data = {"template_object": json.dumps(post, cls=NumpyArrayEncoder)}

    print(url)
    print(headers)
    print(data)

    response = requests.post(url, headers=headers, data=data)

    print(response)

    if response.json().get('result_code') == 0:
        print('success')
        print(json.dumps(post))
    else:
        print('error: ' + str(response.json()))

    return 1
