import random
Upper ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
lower='abcdefghijklmnopqrstuvwxyz'
symbol='(){}@#%&:*'
number='0123456789'
all=lower+Upper+symbol+number
length=8
password = "".join(random.sample(all,length))
print("the password generated is",password)