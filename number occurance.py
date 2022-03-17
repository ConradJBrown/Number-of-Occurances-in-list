#number occurance
import random

def main():
    #create list
    lst = []
    for i in range(20):
        lst.append(random.randint(0,100))
    

    #output list
    print(lst)

    #count the number occurance
    for i in lst:
        count = lst.count(i)
        if count > 1:
            print(i,"occurs", count,"times")
        else:
            print(i,"occurs", count,"time")


main()
