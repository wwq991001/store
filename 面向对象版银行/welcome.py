from data.Bank import Bank
welcome = '''\033[0;32;40m
*******************************
*    中国工商银行账户管理系统    *
*******************************
*           选项              *\033[0m
'''
welcome_item ='''\033[0;32;40m*           {0}.{1}           *\033[0m'''
# 欢迎类
class Welcome:

    def print_welcome(self):
        print(welcome)
        keys = Bank.bank_choose.keys()
        for key in keys:
            print(welcome_item.format(key,Bank.bank_choose.get(key)))
        print("\033[0;32;40m******************************\033[0m")