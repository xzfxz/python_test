i=5
print(i)
i=i+1
print(i)
s='''
    this is a good test program
    so happy now!
'''
print(s)

length=5
breadth=2
area=length*breadth
print("area is",area)
print("perimeter is",2*(length+breadth))

number=23

guess=int(input("enter an integer:"))
if guess==number:
    print("good")
elif guess>=number:
    print("bigger ")
else:
    print("smaller")
print("Done")
