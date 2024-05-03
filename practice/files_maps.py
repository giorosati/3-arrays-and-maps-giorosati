# PREDICT ME!
# What do you think is output by this program?

data = {} # data dictionary

file = open("sample_grades.csv") # open a file for reading
for line in file:
    row = line.rstrip().split(",")
    # [0] student, [1] semester, [2] grade
    x = eval(row[2]) # NOTE: x IS NOT a good variable name!
    if len(row) == 3 and x == 100:
        if row[1] in data:
            data[row[1]] += x
        else:
            data[row[1]] = x
file.close()

for key in data:
    print(key, ":", data[key])   # data[key] OR data.get(key)
print()

'''
# File contents of "sample_grades.csv":
Paul McCartney,Fall 2016,77
John Lennon,Fall 2016,80
George Harrison,Fall 2016,75
Ringo Starr,Fall 2016,89
Penny Hofstadter,Fall 2016,84
JJ Abrams,Spring 2016,71
Tom Brady,Spring 2016,100
Astrid Farnsworth,Spring 2016,87
Daniel Drew,Fall 2016,100
Jamie Hyneman,Spring 2016,98
Adam Savage,Spring 2016,85
Grant Imahara,Spring 2016,96
'''

# OUTPUT
# Fall 2016 : 100
# Spring 2016 : 100