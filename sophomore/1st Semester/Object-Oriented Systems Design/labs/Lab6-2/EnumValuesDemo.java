import java.util.Scanner;

public class EnumValuesDemo {
    enum WorkDay {MONDAY, TUESDAY, WEDNESDAY, THURSDAY, FRIDAY};

    public static void main(String[] args) {
        WorkDay[] day = WorkDay.values();
        double hours = 0;
        double sum = 0;

        Scanner keyboard = new Scanner(System.in);

        for (int i = 0; i < day.length; i++) {
            System.out.println("Enter hours worked for " + day[i]);
            hours = keyboard.nextDouble();
            sum += hours;
        }

        System.out.println("Total hours work = " + sum);
    }
}
