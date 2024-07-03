import java.util.Scanner;

public class Averager {
    public static void main(String[] args) {
        
        Scanner keyboard = new Scanner(System.in);
        int count = 0; // Why this should be initialized with a specific value
        Double sum = 0.0; // This as well
        Double score;


        System.out.println("Enter a list of nonnegative scores.");
        System.out.println("Mark the end with a negative number.");
        System.out.println("I will compute their average.");
        
        score = keyboard.nextDouble();
        while (score >= 0) {
            sum += score;
            count++;
            score = keyboard.nextDouble();
        }

        if (count == 0) {
            System.out.println("No scores entered.");
            System.exit(0);
        }

        System.out.println(count + " scores read.");
        System.out.println("The average is " + (sum / count) + ".");
        
        
        

    }    
}
