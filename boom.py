import itchat
itchat.auto_login(hotReload=True)

def send_onegroup(msg, grame):
    # msg:要发送的信息
    contact = itchat.get_friends(update=True) 
    # 获得联系人的列表
    contact = itchat.search_friends(grame)
    if contact is not None:
        print("The person is found.")
        for i in range(10):
            username = contact[0]['UserName']
            itchat.send(msg,toUserName=username)
    else:
        print("不存在")

if __name__ =='__main__':
    send_onegroup("如果你看到这条消息，说明我正在运行程序", "WW")