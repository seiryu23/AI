import CCsMsc

def prompt(obj):
    return obj.get_name() + ' : ' + obj.get_responder_name() + '> '

print('CS_MSC System prototype: msc_operator')
msc_operator = CCsMsc.CCsMsc('msc_operator')

while True:
    inputs = input(' > ')
    if not inputs:
        print('See you...')
        break
    else:
        response = msc_operator.dialogue(inputs)
        print(prompt(msc_operator), response)