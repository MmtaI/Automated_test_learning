# import unittest
# import requests
# import json
# import jsonpath
#
#
# class Testcase(unittest.TestCase):
#
#     dict1 = {}
#
#     def test_01login(self):
#         url = 'http://39.98.138.157:5000/api/login'
#         header = {"Content-Type": "application/json"}
#         data = {"username": "admin", "password": "123456"}
#         res = requests.post(url, headers=header, data=json.dumps(data))
#         self.dict1['login'] = res.json()
#         self.assertEqual('success', jsonpath.jsonpath(self.dict1['login'], '$.msg')[0])
#
#     def test_02userinfo(self):
#         url = "http://39.98.138.157:5000/api/getuserinfo"
#         header = {"token": jsonpath.jsonpath(self.dict1['login'], "$.token")[0]}
#         res = requests.get(url, headers=header)
#         self.dict1["userinfo"] = res.json()
#         self.assertEqual(200, jsonpath.jsonpath(self.dict1['userinfo'], '$.httpstatus')[0])
#
#     def test_03productinfo(self):
#         url = "http://39.98.138.157:5000/api/getproductinfo?productid=8888"
#         res = requests.get(url)
#         self.dict1["productinfo"] = res.json()
#         self.assertEqual(200, jsonpath.jsonpath(self.dict1['productinfo'], '$.httpstatus')[0])
#
#     def test_04shopcart(self):
#         url = "http://39.98.138.157:5000/api/addcart"
#         header = {"token": jsonpath.jsonpath(self.dict1["login"], "$.token")[0],
#                   "content-type": "application/json"}
#         data = {"userid": jsonpath.jsonpath(self.dict1["userinfo"], "$.data[0].userid")[0],
#                 "openid": jsonpath.jsonpath(self.dict1["userinfo"], "$.data[0].openid")[0],
#                 "productid": jsonpath.jsonpath(self.dict1["productinfo"], "$.data[0].productid")[0]}
#         res = requests.post(url, headers=header, data=json.dumps(data))
#         self.dict1["shopcart"] = res.json()
#         self.assertEqual(200, jsonpath.jsonpath(self.dict1['shopcart'], '$.httpstatus')[0])
#
#     def test_05createorder(self):
#         url = "http://39.98.138.157:5000/api/createorder"
#         header = {"token": jsonpath.jsonpath(self.dict1["login"], "$.token")[0],
#                   "content-type": "application/json"}
#         data = {"userid": jsonpath.jsonpath(self.dict1["userinfo"], "$.data[0].userid")[0],
#                 "openid": jsonpath.jsonpath(self.dict1["userinfo"], "$.data[0].openid")[0],
#                 "productid": jsonpath.jsonpath(self.dict1["productinfo"], "$.data[0].productid")[0],
#                 "cartid": jsonpath.jsonpath(self.dict1["shopcart"], "$.data[0].cartid")[0]}
#         requests.post(url, headers=header, data=json.dumps(data))
#
#
# if __name__ == '__main__':
#     unittest.main()
#
# {"userid":uservar.data[0].userid,"openid":"uservar.data[0].openid","productid":productvar.data[0].productid}
# {"cartid":$cartinfo.data[0].cartid$,"openid":"$uservar.data[0].openid$","productid":$productvar.data[0].productid$,"userid":$uservar.data[0].userid$}
# body = {"userid": "uservar.data[0].userid",
#        "openid": "uservar.data[0].openid",
#        "productid": "productvar.data[0].productid"}
body = {"token": "loginvar.token", "content-type": "application/json"}
e = []
e.append(list(body))
e = e[0]
for v in range(len(e)):
    e1 = ""
    for i in body[e[v]]:
        if i != ".":
            e1 += i
        else:
            break
    e2 = body[e[v]][len(e1):]
    print(body[e[v]])
    print(e1, "11", e2)
    try:
        # j = jsonpath.jsonpath(self.dc[e1], e2)[0]
        j = "111"
        body[e[v]] = j
    except Exception:
        pass
print(body)























