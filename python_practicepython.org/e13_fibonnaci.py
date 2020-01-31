# Write a program that asks the user how many Fibonnaci numbers to generate and
# then generates them. Take this opportunity to think about how you can use
# functions. Make sure to ask the user to enter the number of numbers in the
# sequence to generate.(Hint: The Fibonnaci seqence is a sequence of numbers
# where the next number in the sequence is the sum of the previous two numbers in
# the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def genFibonnaci(limit):
    if limit <= 0:
        return []
    if limit == 1:
        return [0]
    if limit == 2:
        return [0, 1]
    if limit > 2:
        fib = [0, 1]
        while len(fib) != limit:
            fib.append(fib[-1] + fib[-2])
        return fib

limit = int(input("How many Fibonnaci numbers? "))
print(genFibonnaci(limit))
