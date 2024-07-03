import java.util.Scanner;

public class DivisionDemo {
    public static void main(String[] args) {
        try {
            Scanner keyboard = new Scanner(System.in);

            System.out.println("Enter numerator:");
            int numerator = keyboard.nextInt();

            System.out.println("Enter denominator:");
            int denominator = keyboard.nextInt();

            double quotient = safeDivide(numerator, denominator);

            System.out.println(numerator + "/" + denominator + " = " + quotient);
        }

        catch (DivisionByZeroException e) {
            System.out.println(e.getMessage());
            secondChance();
        }

        System.out.println("End of program.");
    }

    public static double safeDivide(int top, int bottom) throws DivisionByZeroException {
        if (bottom == 0) {
            throw new DivisionByZeroException();
        }

        return top / (double)bottom;
    }

    public static void secondChance() {
        try {
            Scanner keyboard = new Scanner(System.in);

            System.out.println("Enter numerator:");
            int numerator = keyboard.nextInt();

            System.out.println("Enter denominator:");
            int denominator = keyboard.nextInt();

            double quotient = safeDivide(numerator, denominator);

            System.out.println(numerator + "/" + denominator + " = " + quotient);
        }

        catch (DivisionByZeroException e) {
            System.out.println("I cannot do division by zero.");
            System.out.println("Aborting program.");
            System.exit(0);
        }
    }
}
