from 工商银行完整版 import *
from unittest import TestCase
from ddt import ddt
from ddt import data
from ddt import unpack
import xlrd,time
import xlwt
from xlutils.copy import copy
# from mail1 import send_mail

# username,password,country,province,street,door,money
wb = xlrd.open_workbook('bank.xls', encoding_override=True)
st = list()
ws = list()
da1 = list()
da2 = list()
da3 = list()
da4 = list()
da5 = list()
data2 = list()
col = list()

newwb = copy(wb)
for i in range(len(wb.sheet_names())):
    st.append(wb.sheet_by_index(i))
    ws.append(newwb.get_sheet(i))
    row = st[i].nrows
    col.append(st[i].ncols)
    for j in range(1, row):
        data1 = st[i].row_values(j)
        if i == 0:
            da1.append(data1)
        if i == 1:
            da2.append(data1)
        if i == 2:
            da3.append(data1)
        if i == 3:
            da4.append(data1)
        if i == 4:
            da5.append(data1)
        ws[i].write(j, col[i]-1, j)
        newwb.save('bank.xls')

# ws1 = newwb.get_sheet(0)

# for i in range(1, row):
#     data1 = st1.row_values(i)
#     da.append(data1)
#     ws1.write(i, 8, i)
#     newwb.save('bank.xls')
@ddt
class TestBank(TestCase):
    global newwb, ws, st

    # def add(self,result,y,r):
    #     if result == y:
    #         x = "通过！"
    #         ws[i].write(r, col[i]-1,x)
    #         print(x)
    #         newwb.save('bank.xls')
    #     else:
    #         x = "不通过！"
    #         ws[i].write(r,col[i]-1,x)
    #         print(x)
    #         newwb.save('bank.xls')
    #
    #     i += 1

    @data(*da1)
    @unpack
    def testAddUser(self, a, b, c, d, e, f, g, h, k):
        result = bank_addUser(a, b, c, d, e, f, g)
        if result == h:  # 让程序自动将测试结果写到excel表里。
            x = "通过！"
            ws[0].write(k, col[0]-1, x)
            print(x)
            newwb.save('bank.xls')
        else:
            x = "不通过！"
            ws[0].write(k, col[0]-1, x)
            print(x)
            newwb.save('bank.xls')

        # 断言
        self.assertEqual(result, h)

    @data(*da2)
    @unpack
    def testSave(self,a,b,c,d):
        result1 = bank_saveMoney(a,b)
        if result1 == c:
            x = "通过！"
            ws[1].write(d, col[1]-1,x)
            print(x)
            newwb.save('bank.xls')
        else:
            x = "不通过！"
            ws[1].write(d,col[1]-1,x)
            print(x)
            newwb.save('bank.xls')

        self.assertEqual(result1,c)

    @data(*da3)
    @unpack
    def testTake(self,a,b,c,d,e):
        result2 = bank_takeMoney(a,b,c)
        if result2 == d:
            x = "通过！"
            ws[2].write(e, col[2]-1,x)
            print(x)
            newwb.save('bank.xls')
        else:
            x = "不通过！"
            ws[2].write(e,col[2]-1,x)
            print(x)
            newwb.save('bank.xls')

        self.assertEqual(result2, d)

    @data(*da4)
    @unpack
    def testTrans(self,a,b,c,d,e,f):
        result3 = bank_transformMoney(a,b,c,d)
        if result3 == e:
            x = "通过！"
            ws[3].write(f, col[3]-1,x)
            print(x)
            newwb.save('bank.xls')
        else:
            x = "不通过！"
            ws[3].write(f,col[3]-1,x)
            print(x)
            newwb.save('bank.xls')

        self.assertEqual(result3, e)

    @data(*da5)
    @unpack
    def testSelect(self,a,b,c,d):
        result4 = bank_selectUser(a,b)
        if result4 == c:
            x = "通过！"
            ws[4].write(d, col[4]-1,x)
            print(x)
            newwb.save('bank.xls')
        else:
            x = "不通过！"
            ws[4].write(d,col[4]-1,x)
            print(x)
            newwb.save('bank.xls')

        self.assertEqual(result4, c)

#
# class Mail:
#
#     send_address = "1942936605@qq.com"
#     send_password = 'xlklojkmgdwlfbfe'
#     receive_address = "wwq991001@outlook.com"
#     title = "工商银行的综合测试"
#     content = "Hi，你好！这封邮件是python发送的"
#     attachfilepath = "bank.xls"
#
#     def mail(self):
#
#         send_mail(self.send_address, self.send_password, self.receive_address, self.title, self.content, file=self.attachfilepath)
#         print('成功')
#
# Mail().mail()




















