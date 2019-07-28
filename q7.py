import sys

class Charactercount :
    x = 0

    def myfunc1(self):
        n = input("please type String: ")
        a = False
        for a in n:
            if a.isdigit():
                a = True
        if a == True:
            print("invalid String!")
            sys.exit()
        self.x = n

    def myfunc2(self):
        count = 0
        for a in self.x:
            if a.isalpha() == True:
                count += 1
        print(count)


p1 = Charactercount ()
p1.myfunc1()
p1.myfunc2()