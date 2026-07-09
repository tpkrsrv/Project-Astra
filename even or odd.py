def main():
    x=int(input("what's x"))
    if even(x):
        print("even")
    else :
        print("odd")

def even(n):
    if n%2==0:
        return True
    else:
        return False
main()