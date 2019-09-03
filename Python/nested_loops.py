#Nested Lists
#############################
Given the names and grades for each student in a Physics class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the same grade, order their names alphabetically and print each name on a new line.

Input Format

The first line contains an integer, , the number of students. 
The  subsequent lines describe each student over  lines; the first line contains a student's name, and the second line contains their grade.

Constraints

There will always be one or more students having the second lowest grade.
Output Format

Print the name(s) of any student(s) having the second lowest grade in Physics; if there are multiple students, order their names alphabetically and print each one on a new line.
###################################

if __name__ == '__main__':
    l = []
    Idx = int(input())
    scores = {}
    for x in range(Idx):
        name = input()
        score = float(input())
        scores.update({name:score})

    #Picking 2nd smallest value of scores
    lst = list(scores.values())
    original = [] 
    for num in lst: 
        if num not in original: 
            original.append(num)
    min2 = sorted(original)[1]
    

    #Finding keys for second lowest value
    for k,v in scores.items():
        if v == min2:
            l.append(k)
        #sorting keys if multiple keys are found
        if len(l)>1:
            l = sorted(l)
    for i in range(len(l)):
        print(l[i])
