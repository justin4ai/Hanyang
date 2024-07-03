import java.util.Scanner;
public class SwitchDemo {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Enter number of ice cream flavors:");
        int numberOfFlavors = keyboard.nextInt();

        switch (numberOfFlavors)
        {
            case 32 :
                System.out.println();
                break;
            case 1 :
                System.out.println("I bet it's vanilla.");
                break;
            case 2 :
            case 3 :
            case 4 :
                System.out.println(numberOfFlavors + " flavors");
                System.out.println("is acceptable."); // These two lines are executed when the case is 2 or 3 or 4.
                break;
            default:
                System.out.println("I didn't plan for");
                System.out.println(numberOfFlavors + "flavors.");
                break;
                
        }
    }
}
