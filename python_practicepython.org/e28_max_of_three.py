# Implement a function that takes as input three variables, and returns the largest 
# of the three. Do this without using the Python max() function!

def max_of_three(x, y, z):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    else:
        return z
    # return sorted([x, y, z])[-1] # this one line does the job

    
print(max_of_three(5,0,1))
