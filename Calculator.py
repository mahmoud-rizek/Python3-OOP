print("Select operation.")
print("1. Addition")
print("2. Subtract")
print("3. Multiply")
print("4. Dividu")

class myobeid:

    def myfun(self,x,y):
        value = int(input("Enter choice (1/2/3/4): "))
        if value == 1:
            result = x+y
            print(f"{x} + {y} = {result}")
            return result
        if value == 2:
            result = x- y
            print(f"{x} - {y} = {result}")
            return result
        if value == 3:
            result = x * y
            print(f"{x} * {y} = {result}")
            return result
        if value == 4:
            result = x / y
            print(f"{x} / {y} = {result}")
            return result
        if value>=5:
            print(" please choiec Number  1 To 4 ")



c1=myobeid()
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
c1.myfun(x,y)
