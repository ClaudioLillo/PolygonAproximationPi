# -*- coding: utf-8 -*-
##################################
## Author: Claudio Lillo
## License: MIT
## Version: 1.0
## Email: cilillo@uc.cl



def estimatesPi(iter):
    m=(0.5)**0.5
    n=4
    d=2**(0.5)
    for i in range(0,iter):
        aux=(1-((d/2)**2))**(0.5)
        a=1-aux
        m=((a**2)+((d/2)**2))**(0.5)
        n=n*2
        d=m
    pi=(n*m)/2
    return([pi,n])

while True:
    print("================================================")
    iter = int(input("Number of iterations of algorithm: "))
    init = input("Press Y to continue, N to exit: ")

    if init=="Y" or init=="y":
        result=estimatesPi(iter)
        if result:
            print("Estimated value of Pi using a ",result[1]," sides regular polygon is ",result[0])
    else:
        print("Bye")




    
