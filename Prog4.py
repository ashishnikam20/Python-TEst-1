class A():
    def __int__(self, iNo1, iNo2):
        self.i = iNo1
        self.j = iNo2

    def fun(self):
        self.i = 1111
        self.j = 2222
        print(self.i, self.j)

class B():
    def Fetch(self):
        self.i = 1122
        self.j = 2233
        i_string = str(self.i)
        j_string = str(self.j)
        a_length = len(i_string)
        #a_length = len(a_string)
        self.i = int(i_string[a_length - 2: a_length])
        self.j = int(j_string[a_length - 2: a_length])

        print("Fetches the last digits of the number is : ", self.i, self.j)
        self.iMult = self.i * self.j
        print("Multiplicaton of last two digits is : ", self.iMult)

obj1 = A()
obj2 = B()

obj1.fun()
obj2.Fetch()
