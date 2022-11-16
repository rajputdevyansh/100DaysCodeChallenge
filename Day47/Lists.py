"""
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
"""
if __name__ == '__main__':
    N = int(input())
    A =[]
    for i in range(0, N):
        comd = input().split();
        if comd[0] == "insert":
            A.insert(int(comd[1]), int(comd[2]))
        elif comd[0] == "append":
            A.append(int(comd[1]))
        elif comd[0] == "pop":
            A.pop()
        elif comd[0] == "print":
            print(A)
        elif comd[0] == "remove":
            A.remove(int(comd[1]))
        elif comd[0] == "sort":
            A.sort()
        else:
            A.reverse()
"""
Compiler Message
Success

Input (stdin)

12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Expected Output

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
"""
