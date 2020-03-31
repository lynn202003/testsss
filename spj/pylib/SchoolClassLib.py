from pprint import pprint

import requests
from cfg import g_vcode


class SchoolClassLib:
    URL = 'http://ci.ytesting.com/api/3school/school_classes'

    def __init__(self):
        self.vcode = g_vcode

    def list_school_class(self, gradeid=None):
        if gradeid is not None:
            params = {
                'vcode': self.vcode,
                'action': 'list_classes_by_schoolgrade',
                'gradeid': int(gradeid)
            }
        else:
            params = {
                'vcode': self.vcode,
                'action': 'list_classes_by_schoolgrade',
            }

        resp = requests.get(self.URL, params)
        bodyDict = resp.json()
        return bodyDict

    def add_school_class(self, grade, name, studentlimit):
        payload = {
            'vcode': self.vcode,
            'action': 'add',
            'grade': int(grade),
            'name': name,
            'studentlimit': int(studentlimit)
        }
        resp = requests.post(self.URL, data=payload)
        return resp.json()

    def delete_school_classe(self,classid):
        payload={
            'vcode': self.vcode
        }
        url=f'{self.URL}/{classid}'
        resp=requests.delete(url,data=payload)
        return resp.json()

    def delete_all_school_classes(self):
        rd=self.list_school_class()
        pprint(rd,indent=2)
        for one in rd['retlist']:
            self.delete_school_classe(one['id'])

        rd = self.list_school_class()
        pprint(rd, indent=2)

        if rd['retlist'] != []:
            raise Exception("cannot delete all school classes!")

if __name__ == '__main__':
    scm = SchoolClassLib()
    ret = scm.list_school_class(1)
    print(ret)







