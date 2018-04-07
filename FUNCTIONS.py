def add():
    x = 45
    y = 78
    z = 56
    ans = x+y+z
    print = ("YOUR SUM IS ", ans)



def mysum(x,y,z):
    answer = x+y+z
    print ("SUM OF 3 IS", answer)

mysum(45,56,56)

# Functions can accept parameneters or arguments
# Funtions are added inside the funtions parenthesis

def mysum(x,y,z,name):
    answer = x+y+z
    print ("SUM OF 3 IS", answer)
    print("YOUR NAME WAS ", name)

mysum(45,56,56,"Joseph")

# CREATE A FUNCTION THAT ACCEPTS 7 parameters, CALL IT PAYROLL
# NAMELY BS, HA, WA, TAX, NHIF, NSSF, NAME
# FIND AND PRINT NET PAY
# FUNTIONS CAN RETURN VALUES

def payroLL(BS,HA,WA,TAX,NHIF,NSSF,NAME):
    netpay = BS+HA+WA-TAX-NHIF-NSSF
    print("YOUR SALARY IS", netpay)
    print("YOUR NAME IS", NAME)

payroLL(60000,5000,4000,7000,1300,400,"Ann")

def payroLL(BS,HA,WA,TAX,NHIF,NSSF,NAME):
    netpay = BS+HA+WA-TAX-NHIF-NSSF
    return netpay
# Here we receive the returned value
# we store it in a variable

netpay = payroLL(60000,5000,4000,7000,1300,400,"Ann")
print("YOUR NETPAY IS", netpay)