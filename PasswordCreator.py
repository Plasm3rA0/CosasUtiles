import random

numbers = [0,1,2,3,4,5,6,7,8,9]
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
caps = []
pref = []
for l in letters:
    caps.append(l.upper())

numeroDeDigitos = int(input('Cuantos digitos quieres que tenga la contraseña?'))

contraseña = ''

preferences = input('Tienes preferencias? ')
if preferences == 'si' or preferences == 'Si' or preferences == 'SI' or preferences == 'yes' or preferences == 'Yes' or preferences == 'YES' or preferences == 'sip' or preferences == 'Sip':
    p1 = input('Preferencia 1: ')
    if len(p1) == 1:
        pref.append(p1)
    p2 = input('Preferencia 2: ')
    if p2 != '':
        if len(p2) == 1:
            pref.append(p2)
        p3 = input('Preferencia 3: ')
        if p3 != '':
            if len(p3) == 1:
                pref.append(p3)
            p4 = input('Preferencia 4: ')
            if p4 != '':
                if len(p4) == 1:
                    pref.append(p4)
                p5 = input('Preferencia 5: ')
                if p5 != '':
                    if len(p5) == 1:
                        pref.append(p5)

    while len(contraseña) < numeroDeDigitos:
        contraseña += ''.join(pref[-1:])
        print(contraseña)
        try:
            pref.pop()
        except:
            print('')
        if random.randrange(2) == 0:
            contraseña += str(numbers[random.randrange(10)])
        if random.randrange(2) == 0:
            contraseña += letters[random.randrange(27)]
        if random.randrange(2) == 0:
            contraseña += caps[random.randrange(27)]



if preferences == 'no' or preferences == 'No' or preferences == 'NO' or preferences == 'NOPE' or preferences == 'nope' or preferences == 'Nope':
    while len(contraseña) < numeroDeDigitos:
        if random.randrange(2) == 0:
            contraseña += str(numbers[random.randrange(10)])
        if random.randrange(2) == 0:
            contraseña += letters[random.randrange(27)]
        if random.randrange(2) == 0:
            contraseña += caps[random.randrange(27)]

print(contraseña)
