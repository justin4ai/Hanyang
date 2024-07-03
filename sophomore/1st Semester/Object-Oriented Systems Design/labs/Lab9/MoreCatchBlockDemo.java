import java.util.Scanner;

public class MoreCatchBlockDemo {
    public static void main(String[] args) {
        try {
            Scanner keyboard = new Scanner(System.in);
            System.out.println("How many pencils do you have?");
            int pencils = keyboard.nextInt();

            if (pencils < 0) {
                throw new NegativeNumberException("pencils");
            }

            System.out.println("How many erasers do you have?");
            int erasers = keyboard.nextInt();

            if (erasers < 0) {
                throw new NegativeNumberException("erasers");
            }

            double pencilsPerEraser;

            if (erasers != 0) {
                pencilsPerEraser = pencils / (double)erasers;
            }

            else {
                throw new DivisionByZeroException();
            }
            System.out.println("Each eraser must last through " + pencilsPerEraser + " pencils.");
        }

        catch (NegativeNumberException e) {
            System.out.println("Cannot have a negative number of " + e.getMessage());
        }

        catch (DivisionByZeroException e) {
            System.out.println("Do not make any mistakes.");
        }

        System.out.println("End of program.");
    }
}
