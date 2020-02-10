#Practical 3: Recursion and dynamic programming:

#Recursivley compute numbers 1-N:
def sumOf(n):
    if (n <= 1):
        return 1
    return n + sumOf(n - 1) #Recursive line

        

print("Input value for n.")
n = int(input()) #Set value for n by user
print("Sum of values from 1 - n:")
print(sumOf(n))

#Recursively compute largest value in array:
def arraySearch(arrayInp, arrayLength):
    if (arrayLength == 1):
        return arrayInp[0]   
    return max(arrayInp[arrayLength - 1], arraySearch(arrayInp, arrayLength - 1)) #Tail recursion

arrayInp = [1, 5, 15, 22, 13, 17]
print("Largest value in array:")
print(arraySearch(arrayInp, 6)) #Pass array length as int. BE CAREFUL it MUST be same as actual array's length

