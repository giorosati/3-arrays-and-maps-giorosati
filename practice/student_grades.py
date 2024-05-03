# ADDITIONAL PRACTICE
# This code can help you deepen your understanding
# of how dictionaries, lists, and files can be used
# together to calculate basic statistics about data.
#
# Approach: walk through the code, writing down what
# you think happens on every line & what is output.
# Then, run it! Were your answers correct? If so,
# GREAT! If not, where do you think the gaps in
# your understanding are?

import csv
from statistics import mean, median, stdev

data = {} # data dictionary
# stores a list of grades for each semester
# key = semester, value = list of grades

f = open("sample_grades.csv")
reader = csv.reader(f)
# optional: get first line
for row in reader:
    # student, semester, grade
    #print(row[1], "--", row[2])
    list = data.get(row[1], []) # get the semester's list of grades
    list.append(eval(row[2]))   # add the new grade
    data[row[1]] = list         # store updated list back in dictionay
f.close()

for key in data:
    print(key, data[key])       # data[key] OR data.get(key)
print()

fall = "Fall 2016"
spring = "Spring 2016"

print("\t\t", spring, "\t", fall)
print("Mean\t", round(mean(data[spring]), 2), \
        "\t" * 3, round(mean(data[fall]), 2))

print("Median\t", round(median(data[spring]), 2), \
        "\t" * 3, round(median(data[fall]), 2))

print("Std Dev\t", round(stdev(data[spring]), 2), \
        "\t" * 3, round(stdev(data[fall]), 2))