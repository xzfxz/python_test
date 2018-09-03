def total(a=5,*number,**phoneBook):
    print("a is",a)
    # foreach number
    for i in number:
        print("number is",i)
    # foreach phoneBook
    for first,second in phoneBook.items():
        print(first,second)
total(10,2,3,4,jack=2,tom=45)

#print(rlt)
