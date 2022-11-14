"""
Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
Input Format
The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.
Output Format
Print the name(s) of any student(s) having the second lowest grade in. If there are multiple students, order their names alphabetically and print each one on a new line.
"""
r = []
scorel = []

if __name__ == '__main__':
    for _ in range(int(input())):
        name = input()
        score = float(input())
        r += [[name,score]]
        scorel += [score]
    a = sorted(list(set(scorel)))[1]
    for b,c in sorted(r):
        if c == a:
            print(b)
"""
Compiler Message
Success

Input (stdin)

5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39

Expected Output

Berry
Harry
"""
