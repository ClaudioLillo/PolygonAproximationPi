# -*- coding: utf-8 -*-
##################################
## Author: Claudio Lillo
## License: MIT
## Version: 1.0
## Email: cilillo@uc.cl



def estimatesPi(sides):
    if sides < 4:
        return (0)
    m=1
    n=4
    d=2**(0.5)
    for i in range(0,sides-4):
        aux=(1-((d/2)**2))**(0.5)
        a=1-aux
        m=((a**2)+((d/2)**2))**(0.5)
        n=n*2
        d=m
    pi=(n*m)/2
    return(pi)


print("================================================")
sides = int(input("Number of sides of polygon (>=4): "))
init = input("Press Y to continue, N to exit: ")

if init=="Y" or init=="y":
    result=estimatesPi(sides)
    if result:
        print("Estimated value of Pi using a ",sides," sides regular polygon is ",estimatesPi(sides))
    else:
        print("Please use a number equal or bigger than 4")
else:
    print("Bye")




    
