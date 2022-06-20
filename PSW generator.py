import random
import sys
dict={}
wordchoices='cool,nondescript,shoe,victorious,uptight,guiltless,relate,peaceful,soggy,nifty,birds,roll,drink,accurate,rend,course,throat,nurse,rind,productive,horrible,shiny,tame,typical,fluffy'
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

        pw=string1+string2+numbers+characters
        if service not in dict:
            dict[servicestring]=pw
            print(f'Your password for {servicestring} is {pw}')
        else:
            print('Password already created for this service!')
            sys.exit()
print('Type exit to exit without saving and save to exit and save dictionary of passwords.')
while True:
    service=input('What service would you like to create a password for:'  )
    servicestring=str(service)
    if servicestring.lower()=='exit':
        print('cancelling program')
        sys.exit()

    elif servicestring.lower()=='save':

        with open('PSW.txt','a') as file:
            file.write(str(dict))
            print('Password dictionary successfully saved')
            print(dict)
            sys.exit()
    else:
        service=password(service)
        service.createpw(service)


