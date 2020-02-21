num = int(input("Δώσε έναν αριθμό:"))
result = 0
for i in range(len(str(num))):
    num = (num * 3) + 1
    digit = num%10
    result = result + digit
    if (len(str(result))>1):
        for j in range(len(str(result))):
            digit1 = result%10
            result = result + digit1
            result = result//10
    num = num//10
        

print("το άθροισμα είναι:",result)
