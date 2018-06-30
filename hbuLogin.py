#! /usr/bin/python3

import urllib
import requests


class Loginer(object):
    def __init__(self, username, password):
        self.loginUrl = 'http://202.206.1.231:804/srun_portal_pc.php?ac_id=1&'
        self.username = username
        self.password = password

    def login(self):
        postdata = {
            'username': self.username,
            'password': self.password,
            'action': 'login',
            'ac_id': '1',
            'use_ip': '',
            'nas_ip': '',
            'url': ''
        }
        postdata = urllib.urlencode(postdata)
        myRequest = urllib2.Request(url=self.loginUrl, data=postdata)

        result = self.openner.open(myRequest).read()
        resStr = str(result)
        ind = resStr.find('font-weight:bold;color:orange')
        if (ind != -1):
            print 'connected successfully'
        else:
            print 'connected faild, maybe somthing wrong'


def main():
    username = '14546'
    password = 'a8070639'
    mylog = Loginer(username, password)
    mylog.login()


if __name__ == '__main__':
    main()
    print 'Done'
