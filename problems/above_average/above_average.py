lines = int(input())

aal = []
for _ in range(lines):
    # all grades for that line
    grades = list(map(int, input().split()))[1:]

    # average for grades
    average = sum(grades)/len(grades)
    
    # number of people above average
    aa = 0 

    for grade in grades:
        if grade > average:
            aa += 1
    aa /= len(grades) 
    aal.append(aa * 100)    

for grade in aal:
    print("{:.3f}%".format(grade))
