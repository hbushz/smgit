#! /usr/bin/python3

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
            'user_mac': '',
            'url': ''
        }
        response = requests.post(self.loginUrl, data=postdata)
        ind = response.text.find('网络已连接')
        if (ind != -1):
            print('Connected successfully.')
        else:
            print('Connected faild, maybe somthing wrong!')


def main():
    username = '123456'
    password = '654321'
    mylog = Loginer(username, password)
    mylog.login()


if __name__ == '__main__':
    main()
    print('Done')
