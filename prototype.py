##処理確認用のファイル##
import CCsMsc

##関数##
#メッセージ送信者の名前を表示
def prompt(obj):
    return obj.get_name() + ' : ' + obj.get_responder_name() + '> '

##処理##
print('CS_MSC System prototype: msc_operator')
msc_operator = CCsMsc.CCsMsc('msc_operator')

#入力に応じてシステムが返答する
while True:
    inputs = input(' > ')
    #何も入力がない時に処理終了
    if not inputs:
        print('See you...')
        break
    #入力があった場合、システムが返信する
    else:
        response = msc_operator.dialogue(inputs)
        print(prompt(msc_operator), response)