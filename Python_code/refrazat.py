import requests
import json

def rearanjare(paragraf_chatgpt):
    url = 'https://app.plaraphy.com/api/rewriter'
    text = paragraf_chatgpt
    #unic => trece de testele de plagiat.
    payload = f'text={text}&mode=fluent&lang=es&unique=true'
    headers = {
        'accept': 'application/json',
        'content-type': 'application/x-www-form-urlencoded',
        'authorization': 'Bearer 24900|ftBX9jHIbiaB6VHIA5qTWi8svldy8N2Fs9MHsxpX',
        'cache-control': 'no-cache',
    }
    response = requests.post(url, data=payload, headers=headers)
    if response.ok:
        result = json.loads(response.text)
        paraphrased_text = result.get('rewrited')
    return paraphrased_text

