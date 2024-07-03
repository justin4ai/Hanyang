import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.io.FileOutputStream;

public class HasNextIntDemo {
    public static void main(String[] args) {
        Scanner inputStream = null;

        try {
            inputStream = new Scanner(new FileInputStream("data.txt"));
        }

        catch (FileNotFoundException e) {
            System.out.println("File data.txt was not found");
            System.out.println("or could not be opened.");
            System.exit(0);
        }
        int sum = 0;
        while (inputStream.hasNextInt()) {
            sum += inputStream.nextInt();
        }

        inputStream.close();
        System.out.println("The sum of the numbers is " + sum);
    }
}
