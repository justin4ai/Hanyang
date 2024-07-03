import java.util.Scanner;

public class IncomeTax {
    public static void main(String[] args) {
        double netIncome, tax;
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Enter net income");
        System.out.println("Do not include a dollar sign or any commas.");  

        netIncome = keyboard.nextDouble();

        if (netIncome < 15000) {
            tax = 0;
        } else if ( (15001 <= netIncome) && (netIncome < 30000) ) {
            tax = netIncome * 0.05;
        } else {
            tax = (netIncome - 30000) * 0.1 + (15000 * 0.05);
        }


        System.out.printf("Tax due = %f", tax);
    }
}
