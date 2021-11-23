listM = []
listP = []
start = True

while start:
    s = input("hello. nu or lo ? ")
    if s == 'nu':
        m = input("enter mail ")
        if m not in listM:
            listM.append(m)
        else:
            continue
        p = input("enter password ")
        p1 = input("check password ")
        while p != p1:
            p1 = input("check password ")
        listP.append(p)

    elif s == 'lo':
        if len(listM) == 0:
            print("sorry, you need to register")
            continue
        m = input("mail ")
        while m not in listM:
            m = input("mail ")
        p = input("enter password ")
        while p not in listP:
            p = input("repeat password ")
        print("welcome ")


    else:
        start = False

print(listM)
print(listP)
