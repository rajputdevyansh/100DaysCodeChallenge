"""
Let's learn about list comprehensions! You are given three integers  and  representing the dimensions of a cuboid along with an integer . Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to . Here, . Please use list comprehensions rather than multiple loops, as a learning exercise.
Input Format
Four integers  and , each on a separate line.
Constraints
Print the list in lexicographic increasing order.
Sample Input 0
1
1
1
2
Sample Output 0
[[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
"""
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    abc = [];
    zbz =[];
    for x in range(x+1):
        for y in range(y+1):
            for z in range(z+1):
                if x+y+z!=n:
                    abc=[x,y,z];
                    zbz.append(abc)
print(zbz)
