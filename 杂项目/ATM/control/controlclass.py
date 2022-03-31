import random
import time
from.import cardclass as Card
from.import personclass as Person

# 每次都要有一个登入函数 验证账号和密码相互匹配
# 还要完善一个数据更新的函数
# 储存数据放在最后面

class controlclass():
    # 数据存储格式
    card_message={} # {'用户名':name,'手机号':userphone,'密码':password,'身份证':userid}

    # 数据存储的url
    card_message_url='./database/card_message.txt'

    # 注册
    def register(self):
        # 获取用户输入的 用户名，身份证，手机号，密码
        name = self.getusername()
        userid = self.getuserid()
        phone = self.getuserphone()
        password = self.getuserpwdd()

        # 给用户创建一个银行卡
        cardid=str(random.randint(100,999))+str(time.time()).replace('.','')[8:]
        cardobj=Card.Card(cardid,password)

        # 创建用户对象，和银行卡进行绑定
        userphone=Person.Person(name,userid,phone,Card).phone

        # 创建需要保存的数据格式  # 银行卡丢了就只能用身份证和名字找回来
        # 考虑可以改进成 {银行卡ID:[身份证ID,用户对象,密码]} # !!!!!!!!!!!!!!!!!此处时后期改进工程
        self.card_message[cardid]={'用户名':name,'手机号':userphone,'密码':password,'身份证':userid,'余额':10}

        # 完成创建
        print(f'恭喜{name}开户成功，卡号为：{cardid} 余额为；{cardobj.money}')
        print('开卡成功')

    # 查询
    def query(self):
        cardlist = []  # 存放所有的卡号
        pwdlist = []  # 存放所以的用户密码
        locklist = []  # 存放锁定用户

        # 获取余额
        def lookmoney(cardid):
            # 获取所有的卡号和密码
            with open('./database/card_message.txt', 'a+', encoding='utf-8') as fp:
                fp.seek(0)  # 调整当前指针的位置
                res = fp.readlines()
                for i in res:
                    # 获取卡号ID
                    t = i.find(':')
                    ID = i[2:t - 1]
                    # 确认卡号
                    if ID == cardid:
                        # 获取余额
                        k1 = i.find('余额')
                        k2 = i.find('}')
                        look_money = i[k1 + 5:k2]
            return look_money

        # 获取所有的卡号和密码
        with open('./database/card_message.txt', 'a+', encoding='utf-8') as fp:
            fp.seek(0)  # 调整当前指针的位置
            res = fp.readlines()
            for i in res:
                # 获取卡号ID
                t = i.find(':')
                arr1 = i[2:t - 1]
                # 获取密码
                k1 = i.find('密码')
                k2 = i.find('身份证')
                arr2 = i[k1 + 6:k2 - 4]
                cardlist.append(arr1)
                pwdlist.append(arr2)


        # 读取锁定名单数据
        with open('./database/lockuser.txt', 'a+', encoding='utf-8') as fp:
            fp.seek(0)
            res = fp.readlines()
            for i in res:
                locklist.append(i.strip())

            # 验证卡号是否存在
            def login():
                # 定义变量 控制登录的外循环
                islogin = True
                # 定义变量 用户密码错误次数的检测
                errornum = 3
                while islogin:
                    # 获取用户输入的卡号
                    cardid = input('欢迎登录，请输入你的卡号：')
                    # 检测当前用户是否存在
                    if cardid in cardlist:
                        # 检测用户是否属于锁定状态，再黑名单中
                        if cardid in locklist:
                            print('当前用户处于锁定状态')
                        else:
                            # 定义循环，执行密码输入
                            while True:
                                # 让用户输入密码
                                pwd = input('请输入密码：')
                                # 检查用户输入的密码是否正确
                                # 获取用户名在用户列表中的索引
                                inx = cardlist.index(cardid)
                                if pwd == pwdlist[inx]:
                                    print('登录成功')
                                    # 通过卡号获取当前卡的余额信息
                                    money1=lookmoney(cardid)
                                    print(f'你的卡号为:{cardid} 余额为:{money1}')

                                    # 结束循环
                                    islogin = False  # 结束外循环变量
                                    break  # 结束内循环

                                else:
                                    # 密码错误，则修改次数变量
                                    errornum -= 1
                                    # 判断当前的密码错误次数==0
                                    if errornum == 0:
                                        print('你没机会了')
                                        # 如何锁定账户信息 把需要锁卡的用户拉入黑名单
                                        with open('./database/lockuser.txt', 'a+', encoding='utf-8') as fp:
                                            fp.write(cardid + '\n')
                                        # 结束循环
                                        islogin = False  # 结束外循环变量
                                        break  # 结束内循环
                                    else:
                                        print(f'密码输入错误，请重新输入密码,你还有{errornum}次机会')

                    else:
                        # 用户名不存在
                        print('卡号不存在，请重新输入')
            # 通过卡号获取当前卡的余额信息
            login()

    # 存钱
    def add_money(self):

        # 更新余额
        def gengxinyue(cardid,add_money):
            with open('./database/card_message.txt', 'a+', encoding='utf-8') as fp:
                fp.seek(0)  # 调整当前指针的位置
                res = fp.readlines()
                for i in res:
                    # 获取卡号ID
                    t = i.find(':')
                    ID = i[2:t - 1]
                    if ID == cardid:
                        # 获取余额
                        k1 = i.find('余额')
                        k2 = i.find('}')
                        look_money = int(i[k1 + 5:k2])
                        s = i.replace(i[k1 + 5:k2], str(add_money + look_money))
                        fp.write(f'{s}')
            with open('./database/card_message.txt', 'r', encoding='utf-8') as fp1:
                reslist = fp1.readlines()
                fp1.close()

            with open('./database/card_message.txt', 'w', encoding='utf-8') as fp2:
                fp2.seek(0)  # 调整当前指针的位置
                flag = 0
                for j in reslist:
                    t = j.find(':')
                    ID = j[2:t - 1]
                    if ID == cardid and flag == 0:
                        flag = 1
                        continue
                    fp2.write(j)
        cardid=input('请输入卡号:')
        add_money=int(input('请输入存款的金额:'))
        gengxinyue(cardid,add_money)

    # 取钱
    def get_money(self):

        # 更新余额
        def gengxinyue(cardid, add_money):
            with open('./database/card_message.txt', 'a+', encoding='utf-8') as fp:
                fp.seek(0)  # 调整当前指针的位置
                res = fp.readlines()
                for i in res:
                    # 获取卡号ID
                    t = i.find(':')
                    ID = i[2:t - 1]
                    if ID == cardid:
                        # 获取余额
                        k1 = i.find('余额')
                        k2 = i.find('}')
                        look_money = int(i[k1 + 5:k2])
                        if add_money - look_money<=0:
                            s = i.replace(i[k1 + 5:k2], str(add_money - look_money))
                        else:
                            s = i.replace(i[k1 + 5:k2], '-'+str(add_money - look_money))
                        fp.write(f'{s}')
            with open('./database/card_message.txt', 'r', encoding='utf-8') as fp1:
                reslist = fp1.readlines()
                fp1.close()

            with open('./database/card_message.txt', 'w', encoding='utf-8') as fp2:
                fp2.seek(0)  # 调整当前指针的位置
                flag = 0
                for j in reslist:
                    t = j.find(':')
                    ID = j[2:t - 1]
                    if ID == cardid and flag == 0:
                        flag = 1
                        continue
                    fp2.write(j)
        cardid = input('请输入卡号:')
        add_money = int(input('请输入要取出的金额:'))
        gengxinyue(cardid, add_money)

    # 转账
    def save_money(self):
        cardid1=input('请输入你的账号：')
        cardid2=input('请输入接收转账的账号：')
        money=int(input('请输入转账的金额：'))
        # 接收钱
        def gengxinyue1(cardid,add_money):
            with open('./database/card_message.txt', 'a+', encoding='utf-8') as fp:
                fp.seek(0)  # 调整当前指针的位置
                res = fp.readlines()
                for i in res:
                    # 获取卡号ID
                    t = i.find(':')
                    ID = i[2:t - 1]
                    if ID == cardid:
                        # 获取余额
                        k1 = i.find('余额')
                        k2 = i.find('}')
                        look_money = int(i[k1 + 5:k2])
                        s = i.replace(i[k1 + 5:k2], str(add_money + look_money))
                        fp.write(f'{s}')
            with open('./database/card_message.txt', 'r', encoding='utf-8') as fp1:
                reslist = fp1.readlines()
                fp1.close()

            with open('./database/card_message.txt', 'w', encoding='utf-8') as fp2:
                fp2.seek(0)  # 调整当前指针的位置
                flag = 0
                for j in reslist:
                    t = j.find(':')
                    ID = j[2:t - 1]
                    if ID == cardid and flag == 0:
                        flag = 1
                        continue
                    fp2.write(j)    #  #
        # 扣钱
        def gengxinyue2(cardid,add_money):
            with open('./database/card_message.txt', 'a+', encoding='utf-8') as fp:
                fp.seek(0)  # 调整当前指针的位置
                res = fp.readlines()
                for i in res:
                    # 获取卡号ID
                    t = i.find(':')
                    ID = i[2:t - 1]
                    if ID == cardid:
                        # 获取余额
                        k1 = i.find('余额')
                        k2 = i.find('}')
                        look_money = int(i[k1 + 5:k2])
                        if add_money - look_money<=0:
                            s = i.replace(i[k1 + 5:k2], str(add_money - look_money))
                        else:
                            s = i.replace(i[k1 + 5:k2], '-'+str(add_money - look_money))
                        fp.write(f'{s}')
            with open('./database/card_message.txt', 'r', encoding='utf-8') as fp1:
                reslist = fp1.readlines()
                fp1.close()

            with open('./database/card_message.txt', 'w', encoding='utf-8') as fp2:
                fp2.seek(0)  # 调整当前指针的位置
                flag = 0
                for j in reslist:
                    t = j.find(':')
                    ID = j[2:t - 1]
                    if ID == cardid and flag == 0:
                        flag = 1
                        continue
                    fp2.write(j)
        gengxinyue1(cardid=cardid2,add_money=money)
        gengxinyue2(cardid=cardid1,add_money=money)

    # 修改密码
    def change_pwd(self):
        cardid = input('请输入你的账号：')
        cardpwd=input('请输入你原来密码：')

        # 更新密码
        def gengxinyue(cardid, recardpwd):
            with open('./database/card_message.txt', 'a+', encoding='utf-8') as fp:
                fp.seek(0)  # 调整当前指针的位置
                res = fp.readlines()
                for i in res:
                    # 获取卡号ID
                    t = i.find(':')
                    ID = i[2:t - 1]
                    if ID == cardid:
                        # 获取密码
                        k1 = i.find('密码')
                        k2 = i.find('身份证')
                        pwd = i[k1 + 6:k2 - 4]
                        s = i.replace("'密码': '" + pwd, "'密码': '" + recardpwd)
                        fp.write(f'{s}')
            with open('./database/card_message.txt', 'r', encoding='utf-8') as fp1:
                reslist = fp1.readlines()
                fp1.close()

            with open('./database/card_message.txt', 'w', encoding='utf-8') as fp2:
                fp2.seek(0)  # 调整当前指针的位置
                flag = 0
                for j in reslist:
                    t = j.find(':')
                    ID = j[2:t - 1]
                    if ID == cardid and flag == 0:
                        flag = 1
                        continue
                    fp2.write(j)
        # 获取所有的卡号和密码
        pwd=''
        with open('./database/card_message.txt', 'a+', encoding='utf-8') as fp:
            fp.seek(0)  # 调整当前指针的位置
            res = fp.readlines()
            for i in res:
                # 获取卡号ID
                t = i.find(':')
                arr = i[2:t - 1]
                # 获取密码
                if arr==cardid:
                    k1 = i.find('密码')
                    k2 = i.find('身份证')
                    pwd=i[k1 + 6:k2 - 4]
        if cardpwd==pwd:
            recardpwd=input('请输入新的密码：')
            gengxinyue(cardid,recardpwd)
        else:
            print("密码输入错误，给爷爬.")

    # 锁定账号
    def lock(self):
        cardid = input('请输入你的账号：')
        flagname=0
        with open('./database/card_message.txt', 'a+', encoding='utf-8') as fp:
            fp.seek(0)  # 调整当前指针的位置
            res = fp.readlines()
            for i in res:
                # 获取卡号ID
                t = i.find(':')
                ID = i[2:t - 1]
                if ID==cardid:
                    flagname=1

        if flagname==0:
            print('锁卡失败，用户名错误')
        else:
            with open('./database/lockuser.txt', 'a+', encoding='utf-8') as fp:
                fp.write(cardid + '\n')
            print('锁卡成功')

    # 解冻账号
    def unlock(self):
        cardid = input('请输入你的账号：')
        flagname=0
        with open('./database/card_message.txt', 'a+', encoding='utf-8') as fp:
            fp.seek(0)  # 调整当前指针的位置
            res = fp.readlines()
            for i in res:
                # 获取卡号ID
                t = i.find(':')
                ID = i[2:t - 1]
                if ID==cardid:
                    flagname=1

        if flagname==0:
            print('解冻账号失败，用户名错误')
        else:
            with open('./database/lockuser.txt', 'r', encoding='utf-8') as fp1:
                reslist = fp1.readlines()
                fp1.close()

            with open('./database/lockuser.txt', 'w', encoding='utf-8') as fp2:
                fp2.seek(0)  # 调整当前指针的位置
                for j in reslist:
                    if j.strip() == cardid.strip():
                        continue
                    fp2.write(j)
            print('解冻账号成功')

    # 补卡 重置原来的数据 反正我时这么理解的
    def new_pwd(self):
        cardid = input('请输入你原来的账号：')
        flagname=0
        with open('./database/card_message.txt', 'a+', encoding='utf-8') as fp:
            fp.seek(0)  # 调整当前指针的位置
            res = fp.readlines()
            for i in res:
                # 获取卡号ID
                t = i.find(':')
                ID = i[2:t - 1]
                if ID==cardid:
                    flagname=1

        if flagname==0:
            print('补卡失败，返回主菜单')
        else:
            # 删除原来的数据
            with open('./database/card_message.txt', 'r', encoding='utf-8') as fp1:
                reslist = fp1.readlines()
                fp1.close()

            with open('./database/card_message.txt', 'w+', encoding='utf-8') as fp2:
                fp2.seek(0)  # 调整当前指针的位置
                flag = 0
                for j in reslist:
                    t = j.find(':')
                    ID = j[2:t - 1]
                    if ID == cardid and flag == 0:
                        flag = 1
                        continue
                    fp2.write(j)

            # 仿照num(1) 进行用户的注册
            # 获取用户输入的 用户名，身份证，手机号，密码
            name = self.getusername()
            userid = self.getuserid()
            phone = self.getuserphone()
            password = self.getuserpwdd()

            # 给用户创建一个银行卡
            cardid=str(random.randint(100,999))+str(time.time()).replace('.','')[8:]
            cardobj=Card.Card(cardid,password)

            # 创建用户对象，和银行卡进行绑定
            userphone = Person.Person(name, userid, phone, Card).phone

            self.card_message[cardid] = {'用户名': name, '手机号': userphone, '密码': password, '身份证': userid, '余额': 10}

    def save(self):
        # 把当前数据 写入到文件中
        with open('./database/card_message.txt', 'a+', encoding='utf-8') as fp:
            fp.seek(0)
            if self.card_message:
                fp.write(f'{self.card_message}\n')







    # 其他辅助函数
    # 获取用户名
    def getusername(self):
        while True:
            name=input('请输入您的用户名：')
            if not name:    #！！！！！！！！！！！！！！此处可以后期修改增加命名条件
                print('您输入的用户名有误，请重新输入')
                continue
            else:
                return name

    # 获取用户身份证
    def getuserid(self):
        while True:
            name = input('请输入您的身份证：')
            if not name:   #！！！！！！！！！！！！！！此处可以后期修改增加身份证条件：如长度必须13位的数字
                print('您输入的身份证有误，请重新输入')
                continue
            else:
                return name

    # 获取用户手机号
    def getuserphone(self):
        while True:
            name = input('请输入您的手机号：')
            if not name:   #！！！！！！！！！！！！！！此处可以后期修改增加身份证条件：如长度必须11位的数字
                print('您输入的手机号有误，请重新输入')
                continue
            else:
                return name

    # 获取用户密码(两次)  通常注册时使用
    def getuserpwdd(self):
        while True:
            pwd=input('请输入您的密码：')
            if not pwd:
                print('输入内容有误，请重新输入')
                continue
            else:
                # 密码正确后，输入确认密码
                repwd=input('请再次输入密码，进行确认：')
                if repwd==pwd:
                    return pwd

                else:
                    print('两次密码不一致，请重新输入密码')
                    continue

    # 跟新数据
    def gengxinyue(cardid, add_money):
        with open('./database/card_message.txt', 'a+', encoding='utf-8') as fp:
            fp.seek(0)  # 调整当前指针的位置
            res = fp.readlines()
            for i in res:
                # 获取卡号ID
                t = i.find(':')
                ID = i[2:t - 1]
                if ID == cardid:
                    # 获取余额
                    k1 = i.find('余额')
                    k2 = i.find('}')
                    look_money = int(i[k1 + 5:k2])
                    s = i.replace(i[k1 + 5:k2], str(add_money + look_money))
                    fp.write(f'{s}')
        with open('./database/card_message.txt', 'r', encoding='utf-8') as fp1:
            reslist = fp1.readlines()
            fp1.close()

        with open('./database/card_message.txt', 'w', encoding='utf-8') as fp2:
            fp2.seek(0)  # 调整当前指针的位置
            flag = 0
            for j in reslist:
                t = j.find(':')
                ID = j[2:t - 1]
                if ID == cardid and flag == 0:
                    flag = 1
                    continue
                fp2.write(j)


    # 登入系统
