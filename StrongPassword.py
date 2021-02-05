numbers = [0,1,2,3,4,5,6,7,8,9]
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
special = ['(',')','^','*','+','-','*','/','+','-','_',',',';','.',':','?','¿','¡','=','/','&','%','$','·','"','!','º','ª','¨','[',']','<','>']
caps = []
pref = []
for l in letters:
    caps.append(l.upper())

password = input('Contraseña: ')
passwordInList = list(password)

CNumber = False
CLetter = False
CCaps = False
CSpecial = False

for x in passwordInList:
    if x in str(numbers) and CNumber == False:
        CNumber = True
    elif x in letters and CLetter == False:
        CLetter = True
    elif x in caps and CCaps == False:
        CCaps = True
    elif x in special and CSpecial == False:
        CSpecial = True

missing = 0
weakPoints = 'You should add:'
if CNumber == False:
    missing += 1
    weakPoints = weakPoints + 'Numbers, '
if CLetter == False:
    missing += 1
    weakPoints = weakPoints + 'Letters, '
if CCaps == False:
    missing += 1
    weakPoints = weakPoints + 'Cap letters, '
if CSpecial == False:
    missing += 1
    weakPoints = weakPoints + 'Special characters '
if len(passwordInList) <8:
    missing += 1
    weakPoints = weakPoints + 'More characters'

if missing == 0:
    print('You have a perfect password')
elif missing > 0:
    print(weakPoints)




