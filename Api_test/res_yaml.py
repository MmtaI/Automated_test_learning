from Api_test.open_excel import excel_yaml
import requests
import json
import jsonpath


class Api_yaml:

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

    def res(self, **dc):
        if dc['body'] is not None and dc['body'].find("$") >= 0:
            dc['body'] = self.ddd(dc['body'])
        if dc['header'] is not None and dc['header'].find("$") >= 0:
            dc['header'] = self.ddd(dc['header'])
        if dc['method'] == "post":
            if dc['methodtype'] == "json":
                body = json.dumps(eval(dc['body']))
            else:
                body = eval(dc['body'])
            re = requests.post(dc['url'], data=body, headers=eval(dc['header']))
            self.dic[dc["dependency"]] = re.json()
            return re
        elif dc['method'] == "get":
            if dc['methodtype'] == "url":
                if dc['body'] is None:
                    if dc['header'] is None:
                        re = requests.get(dc['url'])
                    else:
                        re = requests.get(dc['url'], headers=eval(dc['header']))
                else:
                    if dc['header'] is None:
                        re = requests.get(dc['url'], data=eval(dc['body']))
                    else:
                        re = requests.get(dc['url'], headers=eval(dc['header']), data=eval(dc['body']))
            else:
                re = requests.get(dc['url'], headers=eval(dc['header']), data=eval(dc['body']))
            self.dic[dc["dependency"]] = re.json()
            return re

    def acc(self, **dc):
        # print(self.dic[dc['dependency']])
        d = jsonpath.jsonpath(self.dic[dc['dependency']], str(dc['jsonpath']))[0]
        return str(d)

    def jpath(self, body):
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
            # print(body[e[v]])
            # print(e1, "11", e2)
            try:
                j = jsonpath.jsonpath(self.dic[e1], e2)[0]
                body[e[v]] = j
            except Exception:
                pass
        return eval(body)


# if __name__ == '__main__':
    # m = Api_requests()
    # m.res(3)
    # m.acc(2, m.res(2))

