/*
Given an integer n, return a string array answer (1-indexed) where:
answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
Example 1:
Input: n = 3
Output: ["1","2","Fizz"]
Example 2:
Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
Constraints:
1 <= n <= 104
*/
class Solution {
    public List<String> fizzBuzz(int n)
    {
        List<String>a=new ArrayList<>(n);
        for(int i=1;i<=n;i++)
        {
            boolean d3=i%3==0;
            boolean d5=i%5==0;
            if(d3 && d5)
            {
                a.add("FizzBuzz");
            }
            else if(d3)
            {
                a.add("Fizz");
            }
            else if(d5)
            {
                a.add("Buzz");
            }
            else
            {
                a.add(String.valueOf(i));
            }
        }
        return a;
    }
}

//Time Complexity= O(n);
//Space Complexity= O(1);
