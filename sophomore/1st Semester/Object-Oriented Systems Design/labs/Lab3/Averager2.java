import java.util.Scanner;

public class Averager2 {
    public static void main(String[] args) {
        
        Scanner keyboard = new Scanner(System.in);
        int count; // Why this should be initialized with a specific value
        Double sum = 0.0; // This as well
        Double score;

        System.out.println("Enter the number of nonnegative scores.");
        count = keyboard.nextInt();

        System.out.printf("Enter a list of %s nonnegative scores.%n", count);
        System.out.println("I will compute their average.");
        

        for (int i = 0; i < 4; i++) {
            score = keyboard.nextDouble();
            sum += score;
            
        }

        if (count == 0) {
            System.out.println("No scores entered.");
            System.exit(0);
        }

        System.out.println("The average is " + (sum / count) + ".");
        
        
        

    }    
}