a = input("Enter the number:")
Total = 0
for i in a:
    i = int(i)
    Total += i ** len(a)
if Total == int(a):
    print("Armstrong number")
else:
    print("Not a armstrong number")
