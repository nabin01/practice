# Given two .txt files that have lists of numbers in them, find the numbers that 
# are overlapping. One .txt file has a list of all prime numbers under 1000, and 
# the other .txt file has a list of happy numbers up to 1000.
# 
# (If you forgot, prime numbers are numbers that cant be divided by any other
# number. And yes, happy numbers are a real thing in mathematics - you can look
# it up on Wikipedia. The explanation is easier with an example, which I will 
# describe below.)

with open('happynumbers.txt', 'r') as rh,  open('primenumbers.txt', 'r') as rp:
    happy_numbers = rh.read().split('\n')
    prime_numbers = rp.read().split('\n')
    for i in happy_numbers:
        if i in prime_numbers:
            print(i)
    # print(sorted(list(set(prime_numbers).intersection(set(happy_numbers)))))

