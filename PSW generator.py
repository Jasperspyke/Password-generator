import sys
import random
try:
    old_dict = eval(str(open('PSW.txt','r').read()))
except SyntaxError:
    old_dict = {'Foo': 'Bar'}
wordchoices='cool,nondescript,shoe,gangster,victorious,uptight,guiltless,relate,peaceful,soggy,nifty,birds,roll,drink,accurate,rend,course,throat,nurse,rind,productive,horrible,shiny,tame,typical,fluffy'
words=wordchoices.split(',')

characters='!@#$%^&*()'
splitchar=[char for char in characters]
numbers='1234567890'
digits=[num for num in numbers]

class password:
    def __init__(self,string1=None,string2=None,numbers=None, characters=None):
        self.string1=string1
        self.string2=string2
        self.numbers=numbers
        self.characters=characters

    def createpw(self,service):
        string1=random.choice(words)
        string2=random.choice(words)
        numbers=[random.choice(digits) for i in range(1,5)]
        numbers=''.join(numbers)
        characters=[random.choice(splitchar) for i in range (1,5)]
        characters=''.join(characters)

        pw=string1.upper()+string2+numbers+characters

        return pw



print('Type exit to exit without saving. Otherwise, type the name of the service to create password for')
def main():
    global old_dict
    service=input('What service would you like to create a password for:'  )
    servicestring=str(service)
    if servicestring.lower()=='exit':
        print('cancelling program')
        sys.exit()

    elif servicestring in old_dict.keys():
        service = password(service)
        old_dict[servicestring] = service.createpw(service)
        print('dictionary rewritten with new value')

    else:
        service = password(service)
        old_dict[servicestring] = service.createpw(service)
        print('new password created')
    if 'Foo' in old_dict.keys():
        del old_dict['Foo']

    with open('PSW.txt', 'w') as f:

        f = f.write(str(old_dict))
        print('done')
main()
