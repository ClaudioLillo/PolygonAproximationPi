# -*- coding: utf-8 -*-
##################################
# Author: Claudio Lillo
## License: MIT
## Version: 1.0
## Email: cilillo@uc.cl

# Description

"""
This little piece of code allow us to estimate the pi value from a geometrical abstraction, 
where a N sides regular poligon is used to calculate a perimeter that could be near to a circle
permiter when N is great enough. 

The user must provide an x interations number, to estimate the perimeter of the corresponding
polygon of 2^x sides inscribed in a 1 unit diameter circle
"""

DEFAULT_LANGUAGE = 'en'

translated = {
    'How many iterations would you like to use ?': 'Cuántas itereaciones desea utilizar',
    '$0 sides will be used to calculations': 'Se utilizarán $0 lados para la simulación',
    'Press Y to continue, N to exit': 'Presione Y para continuar o N para salir'
}


def translate(word, lang, placeholders):
    if lang.lower() == 'es':
        out = translated[word]
    else:
        out = word
    index = 0
    for ph in placeholders:
        print('gato')
        out = out.replace(f'${str(index)}', str(ph))
        index += 1
    return out


lang_inputs = {
    '1': 'en',
    '2': 'es'
}


def get_language_input():
    print("Select a language")
    print("1. English")
    print("2. Spanish/Español")
    lang_input = (input(':'))
    return lang_inputs[lang_input]


def estimatesPi(iterations):
    m = 0.5 ** 0.5
    n = 4
    d = 2 ** 0.5
    for i in range(0, iterations):
        aux = (1-((d/2)**2))**(0.5)
        a = 1-aux
        m = ((a**2)+((d/2)**2))**(0.5)
        n = n*2
        d = m
        print(n*m/2)
    pi = (n*m)/2
    return ([pi, n])


while True:

    lang = get_language_input()
    print('lang: ', lang)

    print(f"{translate('How many iterations would you like to use ?', lang, [])}")
    iterations = int(input(': '))

    n = 2 ** iterations

    print(translate('$0 sides will be used to calculations', lang, [n]))
    print('Press Y to continue, N to exit')
    init = input(": ")

    if init == "Y" or init == "y":
        result = estimatesPi(iterations)
        if result:
            print("Estimated value of Pi using a ",
                  result[1], " sides regular polygon is ", result[0])
    else:
        print("Bye")
        break
