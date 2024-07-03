import java.util.Scanner;

public class SwitchDemo {
    public static void main(String[] args) {
        int numberOfFlavors;
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Enter number of ice cream flavors:");
        numberOfFlavors = keyboard.nextInt();

        switch (numberOfFlavors) {
            case 1:
                System.out.println("I bet it's vanilla.");
                break; // Still don't know why I need this break line

            case 32:
                System.out.println("Nice selection.");
                break;

            case 2:
            case 4:
            case 3:
                System.out.printf("%d flavors%n",numberOfFlavors); // %s also works. Why?
                System.out.println("is acceptable.");
                break;
            
            case 9:
                System.out.println("I didn't plan for");
                System.out.println("9 flavors.");
                break;
            default:
                System.out.println("I didn't plan for");
                System.out.printf("%d flavors.", numberOfFlavors);  
                break;           


        }
    }
}
