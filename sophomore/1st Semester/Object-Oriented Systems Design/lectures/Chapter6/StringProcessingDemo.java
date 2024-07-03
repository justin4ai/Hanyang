import java.util.Scanner;

public class StringProcessingDemo {
    public static void main(String[] args) {
        System.out.println("What did you eat for dinner?");
        Scanner keyboard = new Scanner(System.in);
        String sentence = keyboard.nextLine();
        sentence = Utility2.censor(sentence, "candy", "french fries", "salt", "beer");
        sentence = Utility2.censor(sentence, " ,"); // Since french fries has been eliminated
        System.out.println(sentence);
    }   
}
