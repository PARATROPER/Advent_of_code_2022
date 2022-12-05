#Here I learened how a file can be:
# read
# stripped
# splitted for every new line
# change a string into a number value with int
# how to add two or more int with += until \n occurs.


#Getting data
with open('day1.in') as file: #Open the input with list of numbers
    input = [i for i in file.read().strip().split("\n")] #list is called input, and each string is read, stripped of eventual whitespaces and splits each string into it's own value including stings with only whitespaces.
    

max = 0
max2 = 0
max3 = 0
count = 0

for item in input:
#Who got the most calories?
    if item == '': #if a string is whitespace, set the count to 0. 
        count = 0
    else:   
        num = int(item)    #convert/traverse(?) the string into int 
        count += num        #add the first converted int to the next until whitespace.

    if count > max:
        max3 = max2
        max2 = max
        max = count
    elif count > max2:
        max3 = max2
        max2 = count
    elif count > max3:
        max3 = count

print(max)
print(max,max2,max3)
print(max+max2+max3)