from Api_test.open_excel import excel
import requests
import json
import jsonpath


class Api_requests:

    z = excel()[1]
    dc = excel()[0]
    li = excel()[2]
    dic = {}

    def ddd(self, body):
        body = body.split("$")
        # print(body)
        for x in range(len(body)):
            if x % 2 != 0:
                b = body[x]
                e = b[0:b.find(".")]
                # print(e)
                h = b[b.find("."):]
                # print(h)
                o = jsonpath.jsonpath(self.dic[e], "$." + h)[0]
                # print(o)
                body[x] = str(o)
        # print(body)
        body = "".join(body)
        return body

    def res(self, i):
        method = str(self.dc['method'+f'{i}'])
        methodtype = str(self.dc['methodtype'+f'{i}'])
        url = str(self.dc['url'+f'{i}'])
        if self.dc['body' + f'{i}'] is not None and self.dc['body' + f'{i}'].find("$") >= 0:
            self.dc['body' + f'{i}'] = self.ddd(self.dc['body' + f'{i}'])
        if self.dc['header' + f'{i}'] is not None and self.dc['header' + f'{i}'].find("$") >= 0:
            self.dc['header' + f'{i}'] = self.ddd(self.dc['header' + f'{i}'])
        if method == "post":
            if methodtype == "json":
                body = json.dumps(eval(self.dc['body'+f'{i}']))
            else:
                body = eval(self.dc['body'+f'{i}'])
            re = requests.post(url, data=body, headers=eval(self.dc['header'+f'{i}']))
            self.dic[self.dc["dependency" + f'{i}']] = re.json()
            return re
        elif method == "get":
            if methodtype == "url":
                if self.dc['body'+f'{i}'] is None:
                    if self.dc['header'+f'{i}'] is None:
                        re = requests.get(url)
                    else:
                        re = requests.get(url, headers=eval(self.dc['header'+f'{i}']))
                else:
                    if self.dc['header'+f'{i}'] is None:
                        re = requests.get(url, data=eval(self.dc['body'+f'{i}']))
                    else:
                        re = requests.get(url, headers=eval(self.dc['header'+f'{i}']), data=eval(self.dc['body'+f'{i}']))
                self.dic[self.dc["dependency"+f'{i}']] = re.json()
                return re

    def acc(self, i, x):
        p = self.dc['jsonpath' + f'{i}']
        self.dc['jsonpath' + f'{i}'] = jsonpath.jsonpath(x.json(), p)[0]
        if str(self.dc['expect' + f'{i}']) == str(self.dc['jsonpath' + f'{i}']):
            # print('True')
            return True
        else:
            # print('False')
            return False


if __name__ == '__main__':
    m = Api_requests()
    m.res(3)
    # m.acc(2, m.res(2))

