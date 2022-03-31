def outer(func):
    def inner(who,name,*args,**kwargs):
        print('约到妹子，聊微信')
        func(who,name,*args,**kwargs)
        print('天色一晚，怎么办')
    return inner

@outer
def love(who,name,*args,**kwargs):
    print(f'{who}跟{name}畅谈人生')
    print('完事去吃了好多没事',args)
    print('看了一场电影',kwargs)

love('三多','思思','火锅','辣条','麻辣烫',movie='唐山大地震')
'''
love() ==> inner()
    love(...) ==> inner(...)
       inner(...) ==> love(...)
       
约到妹子，聊微信
三多跟思思畅谈人生
完事去吃了好多没事 ('火锅', '辣条', '麻辣烫')
看了一场电影 {'mov': '唐山大地震'}
天色一晚，怎么办    
'''
