
def checkEntry(money):
    if len(money)==0:
        return False
    index=money.find('.')
    if index==(-1):
        test1=money.isdigit()
        test2=True
    else:
        money1=money[:index]
        money2=money[(index+1):]
        test1=money1.isdigit()
        if test1==False:
            if len(money1)==0:
                test1=True
            elif money1.isspace()==True:
                test2=True
        test2=money2.isdigit()
        if test2==False:
            if len(money2)==0:
                test2=True
            elif money2.isspace()==True:
                test2=True
    if test1==True and test2==True:
        return True
    else:
        return False
