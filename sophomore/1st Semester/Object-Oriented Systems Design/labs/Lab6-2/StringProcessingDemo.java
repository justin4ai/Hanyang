import java.util.Scanner;

public class StringProcessingDemo {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        
        System.out.println("What did you eat for dinner?");
        String sentence = keyboard.nextLine();
        System.out.println("You would be healthier if you could answer:");
        
        sentence = Utility2.censor(sentence, "candy","french fries", "salt", "beer");
        sentence = Utility2.censor(sentence, " ,");
        System.out.println(sentence);
    }
}
