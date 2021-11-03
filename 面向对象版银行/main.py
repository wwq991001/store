from data.Address import  Address
from data.Bank  import  Bank
from data.User import  User
from data.welcome import  Welcome
from data.Utils import  Utils


# 初始化必要对象
welcome = Welcome()
utils = Utils()
address = Address()
user = User()
bank = Bank()


# 必要的初始化方法
# 开户方法
def addUser():
    username = utils.inputHelp("用户名")
    password = utils.inputHelp("密码")
    country = utils.inputHelp("居住地址，1.国家：")
    province = utils.inputHelp("省份")
    street = utils.inputHelp("街道")
    door = utils.inputHelp("门牌号")
    money = int(input("银行卡存款余额"))

    n = bank.bank_addUser(username, password, country, province, street, door, money)

    if n == 2:
        print("该用户已存在！")
    elif n == 3:
        print("用户库已满！请携带证件到其他地方办理！谢谢！")
    elif n == 1:
        print("注册成功！以下是您的开户信息：")
        user = bank.bank[username]
        print(bank.myinfo.format(account=user["account"],
                            username=username,
                            password=user["password"],
                            country=user["country"],
                            province=user["province"],
                            street=user["street"],
                            door=user["door"],
                            money=user["money"],
                            bank_name=user["bank_name"]
        ))

def saveMoney(self):
    account = self.inputHelp("账号")
    saveMoney = self.inputHelp("存储金额")
    while True:
        if saveMoney.isdigit():
            saveMoney = int(saveMoney)
            break
        else:
            print("余额输入错误，请重新输入！")
    flag = self.bank_saveMoney(account, saveMoney)
    if flag:
        print("存储成功!")

def takeMoney(self):
    # 取钱由你们自己来开发
    account = self.inputHelp("账号")
    money = self.inputHelp("要取金额")
    while True:
        if money.isdigit():
            money = int(money)
            break
        else:
            print("输入要取金额有误，请重新输入！")
    flag = self.bank_money(account, money)
    if flag:
        print("取钱成功！")
    else:
        print("取钱失败！")

    # pass

def transMoney(self):
    # 转账由你们自己来开发了
    account = self.inputHelp("账号")
    money = self.inputHelp("要转账金额")
    while True:
        if money.isdigit():
            money = int(money)
            break
        else:
            print("输入要取金额有误，请重新输入！")
    flag = self.bank_money(account, money)
    account = self.inputHelp("账号")
    flag1 = self.bank_saveMoney(account, money)
    if flag and flag1:
        print("转账成功！")
    else:
        print("转账失败！")


def selectUser(self):
    username = self.inputHelp("用户名")
    if username in bank:
        user = bank[username]
        print(bank.myinfo.format(account=user["account"],
                            username=username,
                            password=user["password"],
                            country=user["country"],
                            province=user["province"],
                            street=user["street"],
                            door=user["door"],
                            money=user["money"],
                            bank_name=user["bank_name"]))
while True:
    # 欢迎页面
    welcome.print_welcome()

    #用户选择:程序入口
    chose = utils.inputHelp("选项")
    if bank.isExists(chose,bank.bank_choose):
        if chose == "1":
            addUser()
        elif chose == "2":
            saveMoney()
        elif chose == "3":
            takeMoney()
        elif chose == "4":
            transMoney()
        elif chose  == "5":
            selectUser()
        elif chose == "6":
            print("Bye!欢迎下次光临！")
            break
    else:
        print("不存在改选项，被瞎弄！")