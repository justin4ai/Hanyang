public class StringComparisonDemo {

    public static void main(String[] args) {
        String s1 = "Java isn't just for breakfast.";
        String s2 = "JAVA isn't just for breakfast.";
        String s3 = "A cup of java is a joy forever.";
    
        if (s1.equals(s2))
            System.out.println("The two lines are equal.");
        else
            System.out.println("The two lines are not equal.");

        if (s2.equals(s1))
            System.out.println("The two lines are equal.");
        else
            System.out.println("The two lines are not equal.");

        if (s1.equalsIgnoreCase(s2))
            System.out.println("But the lines are equal, ignoring case.");
        else
            System.out.println("The two lines are still not equal, even ignoring case.");
        
        if (s3.compareToIgnoreCase(s1) < 0) // If s3 precedes s1 in lexicographical order
            System.out.println("\"" + s3 + "\"" + "\nprecedes\n" + "\"" + s1 + "\"" + "\nin alphabetic ordering");
        else
            System.out.println("\"" + s1 + "\"" + "\nprecedes\n" + "\"" + s3 + "\"" + "\nin alphabetic ordering");
    }

}
