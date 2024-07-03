import java.util.Scanner;

/**
 * IncomeTax
 */
public class IncomeTax {

    public static void main(String[] args) {
        double netIncome, tax, fivePercentTax, tenPercentTax;
        Scanner keyboard = new Scanner(System.in);

        System.out.println("Enter net Income.");
        System.out.println("Do not include a dollar sign or any commas.");
        
        netIncome = keyboard.nextDouble();

        if (netIncome <= 15000)
            tax = 0;
        else if (netIncome <= 30000)
            tax = 0.05 * (netIncome - 15000);
        else {
            fivePercentTax = 0.05 * 15000;
            tenPercentTax = 0.1 * (netIncome - 30000);
            tax = fivePercentTax + tenPercentTax;
        }
        System.out.printf("Tax due = $%.2f", tax);
    }
}