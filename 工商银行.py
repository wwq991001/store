# author:jason
import random
from DBUtils import *


# from DBUtils import


class bank:
    # 银行库
    # bank = {}
    __bank_name = "中国工商银行昌平支行"
    __bank_choice = {"1": "开户", "2": "存钱", "3": "取钱", "4": "转账", "5": "查询", "6": "Bye"}  # 银行业务选项
    # 开户成功的信息模板
    __myinfo = '''
        \033[0;32;40m
        ------------账户信息------------
        账号：{account}
        姓名：{username}
        密码：{password}
        地址：
            国家：{country}
            省份：{province}
            街道：{street}
            门牌号：{door}
        账户余额：{money}
        注册时间：{registerDate}
        注册银行名：{bank_name}
        -------------------------------
        \033[0m
    '''

    # 欢迎模板
    __welcome = '''
    ***********************************
    *      中国工商银行账户管理系统       *
    ***********************************
    *               选项              *
    '''

    __welcome_item = '''*              {0}.{1}             *'''

    def get_bankname(self):
        return self.__bank_name

    def get_choice(self):
        return self.__bank_choice

    def get_myinfo(self):
        return self.__myinfo

    def print_welcome(self):
        print(self.__welcome, end="")
        keys = self.__bank_choice.keys()
        for i in keys:
            print(self.__welcome_item.format(i, self.__bank_choice[i]))
        print("**********************************")

    # 输入帮助方法：chose是打印选项
    def inputHelp(self, chose, datatype="str"):
        while True:
            print("请输入", chose, ":")
            i = input(">>>:")
            if len(i) == 0:
                print("该项不能为空！请重新输入！")
                continue
            if datatype != "str":
                return int(i)
            else:
                return i

    # 判断是否存在该银行选项
    def isExists(self, chose, data):
        if chose in data:
            return True
        return False

    # 获取随机码
    def getRandom(self):
        li = "0123456789qwertyuiopasdfghjklzxcvbnmZXCVBNMASDFGHJKLQWERTYUIOP"
        string = ""
        for i in range(8):
            string = string + li[int(random.random() * len(li))]
        return string

    # 通过账号获取账户信息
    def findByAccount(self, account):
        sql9 = "select * from user where account = %s"
        param9 = [account]
        data9 = select(sql9, param9)
        if len(data9) == 1:
            return data9
        return None

    # 银行的开户方法
    def bank_addUser(self, username, password, country, province, street, door, money):
        # 查询是否已满
        sql = "select count(*) from user"
        param = []
        data = select(sql, param)
        if len(data) >= 100:
            return 3

        # 查询是否存在
        sql1 = "select * from user where username = %s"
        param1 = [username]
        data = select(sql1, param1)
        if len(data) != 0:
            return 2

        # 插入数据
        sql2 = "insert into user value(%s,%s,%s,%s,%s,%s,%s,%s,now(),%s)"
        param2 = [self.getRandom(), username, password, country, province, street, door, money, self.__bank_name]
        update(sql2, param2)
        return 1

    # 银行的存钱方法
    def bank_saveMoney(self, ac, money):
        if self.findByAccount(ac) != None:
            user7 = self.findByAccount(ac)
            sql6 = "update user set money = money + %s where account = %s "
            param6 = [money, ac]
            update(sql6, param6)
            return True
        return False

    # 银行的查询功能
    def bank_selectUser(self, account, password):
        uname = self.findByAccount(account)
        if uname != None:
            data11 = self.findByAccount(account)
            if int(password) == int(data11[0][2]):
                user = data11
                print(self.__myinfo.format(account=account,
                                           username=user[0][1],
                                           password=user[0][2],
                                           country=user[0][3],
                                           province=user[0][4],
                                           street=user[0][5],
                                           door=user[0][6],
                                           money=user[0][7],
                                           registerDate=user[0][8],
                                           bank_name=user[0][9]
                                           ))
            else:
                print("用户密码错误！")
        else:
            print("该用户不存在！")

    # 银行的取钱功能
    def bank_takeMoney(self, account, password, money):
        uname = self.findByAccount(account)
        if uname != None:
            if int(uname[0][2]) == int(password):
                if uname[0][7] < money:
                    return 3
                else:
                    sql10 = "update user set money = money - %s where account = %s "
                    param10 = [money, account]
                    update(sql10, param10)
                    return 0
            else:
                return 2
        else:
            return 0

    # 银行的转账功能
    def bank_transformMoney(self, outputaccount, inputaccount, outputpassword, outputmoney):
        if self.findByAccount(inputaccount) != None:
            status = self.bank_takeMoney(outputaccount, outputpassword, outputmoney)
            if status == 1:
                return status
            elif status == 2:
                return status
            elif status == 3:
                return status
        else:
            return 1
        if inputaccount != None:
            self.bank_saveMoney(inputaccount, outputmoney)
            return 0
        else:
            return 1


# 开户方法
class addUser(bank):

    __username = ''
    __password = ""
    __country = ""
    __province = ''
    __street = ""
    __door = ''
    __money = 0

    def set_username(self, username):
        if username == "":
            print("用户名非法！")

        else:
            self.__username = username

    def get_username(self):
        return self.__username

    def set_password(self, password):
        if len(password) != 6:
            print("密码非法！")

        else:
            self.__password = password

    def get_password(self):
        return self.__password

    def set_country(self, country):
        if country == '':
            print("国家非法！")

        else:
            self.__country = country

    def get_country(self):
        return self.__country

    def set_province(self, province):
        if province == '':
            print("省份非法！")

        else:
            self.__province = province

    def get_province(self):
        return self.__province

    def set_street(self, street):
        if street == '':
            print("街道非法！")

        else:
            self.__street = street

    def get_street(self):
        return self.__street

    def set_door(self, door):
        if door == '':
            print("门牌号非法！")

        else:
            self.__door = door

    def get_door(self):
        return self.__door

    def set_money(self, money):
        if money < 0:
            print("余额非法！")
            self.__money = -1
        else:
            self.__money = money

    def get_money(self):
        return self.__money

    # 调用银行的开户方法完成开户操作  返回 1 2 3
    def role(self):
        status = super().bank_addUser(self.__username, self.__password, self.__country, self.__province, self.__street,
                                      self.__door, self.__money)
        # 判断1   2   3
        if status == 1:
            sql8 = "select * from user where username = %s"
            param8 = [self.__username]
            user = select(sql8, param8)
            print("恭喜开户成功！以下是您的开户信息：")
            print(super().get_myinfo().format(account=user[0][0],
                                              username=self.__username,
                                              password=user[0][2],
                                              country=user[0][3],
                                              province=user[0][4],
                                              street=user[0][5],
                                              door=user[0][6],
                                              money=user[0][7],
                                              registerDate=user[0][8],
                                              bank_name=user[0][9]
                                              ))
        elif status == 2:
            print("改用户已经存在！请携带证件到其他银行办理！谢谢！！！！！")
        elif status == 3:
            print("银行库已满！请携带证件到其他银行办理！谢谢！！！！！")


# 存钱
class saveMoney(addUser):
    # account = self.inputHelp("账号")
    # m = self.inputHelp("存入的金额", "int")
    __account = ""

    def set_account(self, account):
        if account == "":
            print("账号不能为空")
        elif super().findByAccount(account) == None:
            print("没有此账号，请去开户！")
        else:
            self.__account = account

    def get_account(self):
        return self.__account

    def flags(self):
        flag = self.bank_saveMoney(self.__account, self.get_money())
        if super().get_money() == -1:
            pass
        elif flag:
            print("存储成功!您的个人信息为：")
            uname = super().findByAccount(self.__account)
            user = uname
            print(super().get_myinfo().format(account=user[0][0],
                                              username=user[0][1],
                                              password=user[0][2],
                                              country=user[0][3],
                                              province=user[0][4],
                                              street=user[0][5],
                                              door=user[0][6],
                                              money=user[0][7],
                                              registerDate=user[0][8],
                                              bank_name=user[0][9]
                                              ))
        else:
            print("对不起，您的个人信息不存在！请先开户后再次操作！")
    #
    # # 取钱


class takeMoney(saveMoney):

    def take(self):
        f = super().bank_takeMoney(super().get_account(), super().get_password(), super().get_money())

        if f == 1:
            print("改用户不存在！")
        elif f == 2:
            print("密码错误！")
        elif f == 3:
            print("取款金额不足！")
        elif f == 0:
            print("取款成功！")
            super().bank_selectUser(super().get_account(), super().get_password())
    #
    # # 转账功能


class transformMoney(takeMoney):

    def trans(self, input):
        f = super().bank_transformMoney(super().get_account(), input, super().get_password(), super().get_money())

        if f == 1:
            print("转出或转入的账号不存在！")
        elif f == 2:
            print("输入密码错误！")
        elif f == 3:
            print("转账金额不足！")
        else:
            print("转账成功！")
            print("您的个人信息：")
            super().bank_selectUser(super().get_account(), super().get_password())
    #
    # # 查询账户方法


class selectUser(transformMoney):

    def sel(self):
        super().bank_selectUser(super().get_account(), super().get_password())

    # __username = super().inputHelp("用户名")  QOuW97cf
    # __password = super().inputHelp("密码")
    # __country = super().inputHelp("居住地址：1.国家：")
    # __province = super().inputHelp("省份")
    # __street = super().inputHelp("街道")
    # __door = super().inputHelp("门牌号")
    # __money = super().inputHelp("银行卡余额", "int")


# 核心程序

bank = selectUser()
while True:
    bank.print_welcome()
    chose = bank.inputHelp("选项")
    if bank.isExists(chose, bank.get_choice()):
        if chose == "1":
            username = bank.inputHelp("用户名")
            password = bank.inputHelp("密码")
            country = bank.inputHelp("居住地址：1.国家：")
            province = bank.inputHelp("省份")
            street = bank.inputHelp("街道")
            door = bank.inputHelp("门牌号")
            money = bank.inputHelp("银行卡余额", "int")
            bank.set_username(username)
            bank.set_password(password)
            bank.set_country(country)
            bank.set_province(province)
            bank.set_street(street)
            bank.set_province(province)
            bank.set_money(money)
            bank.role()

        elif chose == "2":
            account = bank.inputHelp("账号")
            money = bank.inputHelp("存款金额", "int")
            bank.set_account(account)
            bank.set_money(money)
            bank.flags()

        elif chose == "3":
            account = bank.inputHelp("账号")
            password = bank.inkputhelp("密码")
            money = bank.inputHelp("取款金额", "int")
            bank.set_account(account)
            bank.set_password(password)
            bank.set_money(money)
            bank.take()
        elif chose == "4":
            account = bank.inputHelp("出款账号")
            password = bank.inkputhelp("密码")
            money = bank.inputHelp("转账金额", "int")
            account1 = bank. inputHelp("收款号")
            bank.set_account(account)
            bank.set_password(password)
            bank.set_money(money)
            bank.trans(account1)
        elif chose == "5":
            account = bank.inputHelp("账号")
            password = bank.inputHelp("密码")
            bank.set_account(account)
            bank.set_password(password)
            bank.sel()
        elif chose == "6":
            print("Bye,Bye您嘞！！！！")
            break
    else:
        print("不存在改选项，别瞎弄！")


