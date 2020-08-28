import openpyxl
import yaml
from ruamel import yaml


def excel():
    z = 0
    dict1 = {}
    list1 = ['url', 'body', 'header', 'method', 'methodtype', 'expect', 'jsonpath', 'dependency']
    workbook = openpyxl.load_workbook('case1.xlsx')
    sheet = workbook['Sheet1']
    value = sheet.values
    for y in value:
        if y[0] == "url":
            pass
        else:
            for x in range(len(list1)):
                dict1[list1[x]+f'{z}'] = y[x]
        z += 1
    # print(dict1)
    return dict1, z, list1


# if __name__ == '__main__':
#     r = excel()


def excel_yaml():
    dict1 = {}
    list1 = ['url', 'body', 'header', 'method', 'methodtype', 'expect', 'jsonpath', 'dependency']
    workbook = openpyxl.load_workbook('case1.xlsx')
    sheet = workbook['Sheet1']
    value = sheet.values
    with open("case.yaml", "w", encoding='utf-8')as yam:
        for y in value:
            if y[0] == "url":
                pass
            else:
                for x in range(len(list1)):
                    dict1[list1[x]] = y[x]
                # print(dict1)
                yaml.dump([dict1], yam, Dumper=yaml.RoundTripDumper)


if __name__ == '__main__':
    # r = excel()
    excel_yaml()
