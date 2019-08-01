import re
import requests


def get_ip():
    ip_url = "http://192.168.1.111:8008/random"
    ip_response = requests.get(ip_url)
    ip_content = ip_response.text
    proxies = {
        "http": "http://%s"%ip_content,
        "https": "https://%s"%ip_content,
    }
    return proxies

def get_page(url):
    headers = {
        'User-Agent': 'Mozilla/5.0(Linux;Android8.0.0;SM-N9500Build/R16NW;wv)AppleWebKit/537.36(KHTML,like Gecko)Version/4.0Chrome/66.0.3359.126MobileSafari/537.36 MicroMessenger/7.0.3.1400(0x27000334)Process/appbrand0NetType/WIFILanguage/zh_CN',
        'referer': 'http://www.pplive114.com/',
        'Upgrade-Insecure-Requests': '1',
    }
    ip = get_ip()
    print(ip)
    try:
        response = requests.get(url, headers=headers, timeout=5)
        content = response.content.decode('utf-8')
    except:
        content = None

    if content:
        return content
    else:
        get_page(url)


def pplive114():
    province_url = 'http://www.pplive114.com/Bank/1/anhui/'
    province = get_page(province_url)
    print(province)
    bank_types = re.findall(r'<li><a href="(.*?)" title="(.*?)" ><span>(.*?)</span></a></li>',province)
    for bank_type in bank_types:
        print(bank_type)
    citys = re.findall(r'<li><a title="(.*?)" href="/(.*?)/1.html">(.*?)</a></li>', province)
    for city in citys:
        print(city)
    city_banks = re.findall(r'<li><a title="(.*?)" href="(.*?)">(.*?)</a></li>', province)
    for city_bank in city_banks:
        print(city_bank)




if __name__ == '__main__':
    pplive114()