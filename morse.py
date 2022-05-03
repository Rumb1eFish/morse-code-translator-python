from os import system

alpha = {'a' : '.-',
'b' : '-...',
'c' : '-.-.',
'd' : '-..',
'e' : '.',
'f' : '..-.',
'g' : '--.',
'h' : '....',
'i' : '..',
'j' : '.---',
'k' : '-.-',
'l' : '.-..',
'm' : '--',
'n' : '-.',
'o' : '---',
'p' : '.--.',
'q' : '.-.',
'r' : '.-.',
's' : '...',
't' : '-',
'u' : '..-',
'v' : '...-',
'w' : '.--',
'x' : '-..-',
'y' : '-.--',
'z' : '--..'}

morse = {'.-' : 'a',
'-...' : 'b',
'-.-.' : 'c',
'-..' : 'd',
'.' : 'e',
'..-.' : 'f',
'--.' : 'g',
'....' : 'h',
'..' : 'i',
'.---' : 'j',
'-.-' : 'k',
'.-..' : 'l',
'--' : 'm',
'-.' : 'n',
'---' : 'o',
'.--.' : 'p',
'--.-' : 'q',
'.-.' : 'r',
'...' : 's',
'-' : 't',
'..-' : 'u',
'...-' : 'v',
'.--' : 'w',
'-..-' : 'x',
'-.--' : 'y',
'--..' : 'z'}

ed = ''
while ed != 'e' and ed != 'd':
    system('cls')
    ed = input('[E]ncrypt [D]ecrypt~ ')
    ed = ed.lower()

if ed == 'e':
    message = input('message~ ')
    for letter in message:
        for char in alpha:
            if letter == char:
                print(alpha[letter], end=' ')
elif ed == 'd':
    print('(put spaces between each letter)')
    message = input('message~ ')
    string = ''
    msgLen = len(message)
    msgLen -= 1
    for letter in message:
        if letter == ' ':
            print(morse[string], end='')
            string = ''
        else:
            string += letter
