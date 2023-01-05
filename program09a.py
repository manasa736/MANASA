class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img
    def __add__(self,ob):
        temp=self.real+ob.real,self.real+ob.img
        return temp
    def __str__(self):
        return (self.real,self.img)
ob1=Complex(4,6)
ob2=Complex(1,3)
ob3=ob1+ob2
print(ob3)
    
