import requests

url = 'http://api.map.baidu.com/geocoder/v2/'
def getlocation(addr, city='贵阳'):
    try:
        params = {'output': 'json', 'ak': '0ZqFawNu58dvih0zpLvBNKDdSLGX6wGC', 'address': addr, 'city': city }
        r = requests.get(url, params)
        print(r.url)
        if r.status_code == 200 or r.status_code == 304:
            print(r.json()['result']['location'])
            return r.json()['result']['location']
        else:
            print(r.status_code)
            return r.status_code	
    except Exception as e:
        print("ERROR:", e)
        return 404

if __name__ =='__main__':
    while True:
        addr = input("please input your address:").strip()
        if len(addr) == 0: break
        location = getlocation(addr)
        if isinstance(location, int):
            print("error",location)
        else:
            print(location['lng'], location['lat'])
