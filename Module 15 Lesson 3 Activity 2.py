n=int(input("Enter a number: "))
g=input("How many times does countdown call itself for the number " + str(n) + "? ")

input("Recursion - Watch each call- Press Enter to continue...")
def c(num):
    print("Call - n", num)
    if num>0:
        c(num-1)
c(n)
print("The number of calls for the countdown is", n+1, "and the number of calls you predicted is", g)