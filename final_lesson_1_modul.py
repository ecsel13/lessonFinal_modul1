grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(students)
S = list(students)
sr1 = sum(grades[0]) / len(grades[0])
sr2 = sum(grades[1]) / len(grades[1])
sr3 = sum(grades[2]) / len(grades[2])
sr4 = sum(grades[3]) / len(grades[3])
sr5 = sum(grades[4]) / len(grades[4])
srbal = {S[0]: sr1, S[1]: sr2, S[2]: sr3, S[3]: sr4, S[4]: sr5}
print(srbal)
