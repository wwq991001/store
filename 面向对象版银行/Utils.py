# 此类是工具类：包括输入帮助和获取8位随机码
import random
class Utils:
    def inputHelp(self, chose, datatype="str"):
        while True:
            print("请输入" + chose + ":")
            i = input(">>>")
            if len(i.strip()) == 0:
                print("该项不能为空，请重新输入！")
                continue
            if datatype != "str":
                return int(i)
            else:
                return i

        # 随机生成8位随机号

    def getRandom(self):
        # a~z : 97 ~ 122    A~Z:65~90
        list = [chr(i) for i in range(97, 123)]
        for i in range(65, 91):
            list.append(chr(i))
        for i in range(10):
            list.append(str(i))
        string = ""
        for i in range(8):
            string += list[int(random.random() * len(list))]
        return string
