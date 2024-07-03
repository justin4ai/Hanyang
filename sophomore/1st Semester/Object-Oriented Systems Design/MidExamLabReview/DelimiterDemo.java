import java.util.Scanner;

public class DelimiterDemo {
    
    public static void main(String[] args) {
        Scanner keyboard1 = new Scanner(System.in);
        Scanner keyboard2 = new Scanner(System.in);
        keyboard2.useDelimiter("##");
        System.out.println("Enter a line of text:");

        String word1, word2;
        word1 = keyboard1.next();
        word2 = keyboard1.next();

        System.out.println("For keyboard1 the two words read are:");
        System.out.println(word1);
        System.out.println(word2);
        String junk = keyboard1.nextLine(); // *Super Important

        System.out.println("Reenter the same line of text:");
        word1 = keyboard2.next();
        word2 = keyboard2.next();

        System.out.println("For keyboard2 the two words read are:");
        System.out.println(word1);
        System.out.println(word2);

    }
    

}
