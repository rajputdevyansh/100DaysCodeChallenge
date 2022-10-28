class Sports 
{

    String getName() 
    {
        return "Generic Sports";
    }
    void getNumberOfTeamMembers() 
    {
        System.out.println("Each team has n players in " +getName());
    }
}

class Soccer extends Sports 
{
    String getName() 
    {
        return "Soccer Class";
    }
    void getNumberOfTeamMembers () 
    {
       System.out.println( "Each team has 11 players in " +getName() );
    }

}

public class Solution
{
    public static void main(String[] args) 
    {
        Sports A1 = new Sports();
        Soccer A2 = new Soccer();
        System.out.println(A1.getName());
        A1.getNumberOfTeamMembers();
        System.out.println(A2.getName());
        A2.getNumberOfTeamMembers();
    }
}
