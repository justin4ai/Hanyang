import java.util.Scanner;

public class GolfScores {

    public static final int MAX_NUMBER_SCORES = 10;

    public static int fillArray(double[] a) {
        System.out.println("Enter up to " + a.length + " nonnegative numbers.");
        System.out.println("Mark the end of the list with a negative number.");

        double next;
        int index = 0;
        Scanner keyboard = new Scanner(System.in);
        next = keyboard.nextDouble();


        while (next >= 0 && index < a.length) {
            a[index++] = next;
            next = keyboard.nextDouble();
        }
        
        if (next >= 0)
            System.out.println("Could only read in " + a.length + " input values.");
        return index;
    }

    public static double computeAverage(double[] a, int numberUsed) {
        double total = 0;

        if (numberUsed > 0) {
            for (int i = 0; i < numberUsed; i++) {
                total += a[i];
            }

            return (total / numberUsed);
        }

        else {
            System.out.println("ERROR: Trying to average 0 nunbers.");
            System.out.println("computeAverage returns -1.");
            return -1;
        }
    }

    public static void showDifference(double[] a, int numberUsed) {
        double average = computeAverage(a, numberUsed);
        System.out.println("Average of the 3 scores = " + average);
        System.out.println("The scores are:");
        for (int i = 0; i < numberUsed; i++) {
            System.out.println(a[i] + " differs from average by " + (a[i] - average));
        }
    }
    public static void main(String[] args) {
        double[] score = new double[MAX_NUMBER_SCORES];
        int numberUsed = 0;
        System.out.println("This program reads golf scores and shows");
        System.out.println("how much each differs from the average.");
        System.out.println("Enter golf scores:");
        numberUsed = fillArray(score);
        showDifference(score, numberUsed);




    }
}
