import requests, time, json

t1 = time.time()
url = "http://10.115.20.101:8989/Rec"

if __name__=='__main__':
    res = requests.get(url)
    j = json.loads(res.content)
    t2 = time.time()
    print(t2 - t1)
