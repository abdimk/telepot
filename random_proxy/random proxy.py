try:
    import requests
    from bs4 import BeautifulSoup
    import random
except Exception as e:
    print('some thing went wrong{}'.format(e))

def get_proxy():
    url = 'https://www.sslproxies.org/'
    r = requests.get(url)
    soup = BeautifulSoup(r.content,'lxml')
    return {'https':random.choice(list(map(lambda x:x[0]+':'+x[1],list(zip(map(lambda x:x.text, soup.findAll('td')[::8]),map(lambda x:x.text, soup.findAll('td')[1::8]))))))}



get_proxy()


def proxy_request(request_type,url,data,**kwargs):
    while 1:
        try:
            proxy = get_proxy()
            r = requests.request(request_type ,url , proxies = proxy, timeout=5, **kwargs)
            break
        except:
            pass
        
    return r

proxy = get_proxy()

#testing the proxy by sending free sms using textbelt
resp = requests.post('https://textbelt.com/text',{
    'phone': '+2510939167494',
    'message': 'hey abdisa',
    'key': "textbelt",
},proxies = proxy)
print(resp.json())
