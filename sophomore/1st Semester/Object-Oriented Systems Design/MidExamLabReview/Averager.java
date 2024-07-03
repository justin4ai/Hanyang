import java.util.Scanner;

import javax.swing.plaf.nimbus.NimbusLookAndFeel;

public class Averager {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Enter a list of nonnegative scores.");
        System.out.println("Mark the end with a negative number.");
        System.out.println("I will compute their average.");
        double sum = 0;
        int cnt = 0;

        double num = keyboard.nextDouble();
        while (num > 0) {
            sum += num;
            cnt++;
            num = keyboard.nextDouble();
        } 

        System.out.println(cnt + " scores read.");
        System.out.println("The average is " + (sum / cnt));
    }
}
