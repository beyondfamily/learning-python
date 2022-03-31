from control.controlclass import controlclass
from package.viewclass import view1,viewbin

class Main():
    def __init__(self):
        # 实例化视图对象
        view = view1()

        # 实例化操作控制类
        obj = controlclass()


        while True:
            # 让用户选择操作
            num = input('请输入你要选择的操作：')
            # 需要验证用户的输入是否正确
            code = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
            if num not in code:
                print('您输入的内容有误，请重新输入')
                view.showfunc()
                # 跳过本次循环
                continue

            if num == '1':  # 1.注册
                obj.register()
            elif num == '2':  # 2.查询
                obj.query()
            elif num == '3':  # 3.存钱
                obj.add_money()
            elif num == '4':  # 4.取钱
                obj.get_money()
            elif num == '5':  # 5.转账
                obj.save_money()
            elif num == '6':  # 6.改密
                obj.change_pwd()
            elif num == '7':  # 7.锁卡
                obj.lock()
            elif num == '8':  # 8.解卡
                obj.unlock()
            elif num == '9':  # 9.补卡
                obj.new_pwd()
            elif num == '0':  # 0.退出 保存  # !!!!!!!!!!!! TM的跟新数据要把原来的给删掉 还TM要改
                obj.save()
                break


            viewbin()
            s=input("请输入你的选择:")  # 此处有bug 按完任意键之后必须再按一次回车才能生效
            if s!='1':
                obj.save()
                break


if __name__ == '__main__':
    Main()