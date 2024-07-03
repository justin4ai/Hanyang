import java.util.Scanner;

public class ScannerDemo2 {
    public static void main(String[] args) {
        

        Scanner scannerObject = new Scanner(System.in);
        int n1, n2;
        System.out.println("Enter two whole numbers");
        System.out.println("seperated by one or more spaces:");

        n1 = scannerObject.nextInt();
        n2 = scannerObject.nextInt(); // If the scanner object takes more than two consecutive user inputs, both typing one by one
                                      // and typing all of them at once are okay. 

        System.out.println("You entered " + n1 + " and " + n2);

        System.out.println("Next enter two numbers.");
        System.out.println("A decimal point is OK.");

        double d1, d2;
        d1 = scannerObject.nextDouble();
        d2 = scannerObject.nextDouble();
        System.out.println("You entered " + d1 + " and " + d2);


        System.out.println("Next enter two words:");

        String word1 = scannerObject.next();
        String word2 = scannerObject.next();
        System.out.println("You entered \"" + word1 + "\" and \"" + word2 + "\"");

        String junk = scannerObject.nextLine(); // *SUPER IMPORTANT! If we delete this line of code, line variable takes an "\n" of the previous input (in this case, the second scannerObject.next())..

        System.out.println("Next enter a line of text:");
        String line = scannerObject.nextLine();
        System.out.println("You entered: \"" + line + "\"");
    }
}
