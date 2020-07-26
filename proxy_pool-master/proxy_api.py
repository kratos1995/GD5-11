import requests
def getLocalProxyIP()->str:      # 每次提取可用代理ip中的一个代理ip
    return requests.get("http://127.0.0.1:5010/get/").text

print(getLocalProxyIP())