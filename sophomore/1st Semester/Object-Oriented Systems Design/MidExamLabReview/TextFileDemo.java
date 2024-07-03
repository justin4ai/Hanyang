import java.util.Scanner;
import java.io.FileInputStream;
import java.io.FileNotFoundException;

public class TextFileDemo {
    public static void main(String[] args) {
        Scanner FileIn = null;
        try {
            FileIn = new Scanner(new FileInputStream("player.txt"));
            
        
        }

        catch (FileNotFoundException e) {
            System.out.println("File not Found.");
            System.exit(0);
        }

        int hightscore;
        String name;

        FileIn.nextLine()
        ...
    }
}
