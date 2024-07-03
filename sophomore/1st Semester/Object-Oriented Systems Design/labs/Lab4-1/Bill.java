import java.util.Scanner;

/**
 * Bill
 */
public class Bill {

    public static double RATE = 150.00;

    private int hours;
    private int minutes;
    private double fee;

    public void inputTimeWorked() {
        System.out.println("Enter number of full hours worked");
        System.out.println("followed by number of minutes:");
        Scanner keyboard = new Scanner(System.in);
        hours = keyboard.nextInt();
        minutes = keyboard.nextInt();
    }

    private double computeFee(int hoursWorked, int minutesWorked) {
        minutesWorked = hoursWorked * 60 + minutesWorked;
        int quarterHours = minutesWorked / 15;
        return quarterHours * RATE;
    }

    public void updateFee() {
        fee = computeFee(hours, minutes);
    }

    public void outputBill() {
        System.out.println("Time worked: ");
        System.out.printf("%shours and %s minutes%n", hours, minutes);
        System.out.printf("Rate: $%s per quarter hour.%n", RATE);
        System.out.printf("Amount due: $%s.%n", fee);
    }
}