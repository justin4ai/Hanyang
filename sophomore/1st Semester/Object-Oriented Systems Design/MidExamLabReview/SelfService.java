import java.util.Scanner;

public class SelfService {
    public static void main(String[] args) {
        int count;
        double price;
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Enter number of items purchased");
        System.out.println("followed by the cost of one item.");
        System.out.println("Do not use a dollar sign.");
        count = keyboard.nextInt();
        price = keyboard.nextDouble();
        System.out.printf("%d items at $%f each.%n", count, price);
        double total = count * price;
        System.out.printf("Total amount due $%f.", total);
        System.out.println("Please take your merchandise.");
        System.out.printf("Place $%f in an envelope%n", total);
        System.out.println("and slide it under the office door.");
        System.out.println("Thank you for using the self-serving line.");
    }
}
