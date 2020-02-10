# Given a .txt file that has a list of a bunch of names, count how many of each 
# name there are in the file, and print out the results to the screen. I have a 
# .txt file for you, if you want to use it!

# Extra:

# Instead of using the .txt file from above (or instead of, if you want the 
# challenge), take this .txt file, and count how many of each category of each 
# image there are. This text file is actually a list of files corresponding to 
# the SUN database scene recognition database, and lists the file directory 
# hierarchy for the images. Once you take a look at the first line or two of 
# the file, it will be clear which part represents the scene category. To do 
# this, youre going to have to remember a bit about string parsing in Python 3. 
# I talked a little bit about it in this post.

filename = 'nameslist.txt'
with open(filename, 'r') as fw:
    count_names = dict()
    line = fw.readline().strip()
    while line:
        if line in count_names.keys():
            count_names[line] += 1
        else:
            count_names[line] = 1
        line = fw.readline().strip()

    # display the count
    for key in count_names.keys():
        print(f'{key}, {count_names[key]}')

with open('Training_01.txt', 'r') as fw:
    count_names = dict()
    line = fw.readline().strip()[3:-25]
    while line:
        if line in count_names.keys():
            count_names[line] += 1
        else:
            count_names[line] = 1
        line = fw.readline().strip()[3:-25]

    # display the count
    for key in count_names.keys():
        print(f'{key}, {count_names[key]}')


