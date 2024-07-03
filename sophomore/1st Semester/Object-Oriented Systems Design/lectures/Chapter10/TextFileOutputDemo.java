import java.io.PrintWriter;
import java.io.FileOutputStream;
import java.io.FileNotFoundException;

public class TextFileOutputDemo {
    public static void main(String[] args) {
        PrintWriter outputStream = null;

        try {
            outputStream = new PrintWriter(new FileOutputStream("stuff.txt", false)); // appending mode = false is default
            //PrintWriter outputStream = new PrintWriter(new FileOutputStream("stuff.txt")); is impossible
        }

        catch (FileNotFoundException e) { // won't happen since the file will be auto-created even when it didn't pre-exist
            System.out.println("Error opening the file stuff.txt.");
            System.exit(0);
        }

        System.out.println("Writing to file.");

        outputStream.println("The quick brown fox");
        outputStream.println("jumps over the lazy dog.");

        outputStream.close();

        System.out.println("End of program.");
    }
}