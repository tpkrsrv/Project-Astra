#take input age from user
age=int(input("the age is : "))
if age<18 :
    print("teen")
elif 18<= age <=25 :
    print("child")
elif age >25:
    print("adult")