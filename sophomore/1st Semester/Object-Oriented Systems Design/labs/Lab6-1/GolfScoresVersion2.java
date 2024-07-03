import java.util.Scanner;

public class GolfScoresVersion2 {
    public static final int MAX_NUMBER_SCORES = 10;
    public static void main(String[] args) {
        PartiallyFilledArray score = new PartiallyFilledArray(MAX_NUMBER_SCORES);

        System.out.println("This program reads golf scores and shows");
        System.out.println("how much each differs from the average.");
        System.out.println("Enter golf scores.");
        fillArray(score);
        showDifference(score);
    }

    public static void fillArray(PartiallyFilledArray a) {
        System.out.println("Enter up to " + a.getMaxCapacity() + " nonnegative numbers.");
        System.out.println("Mark the end of the list with a negative number.");
        Scanner keyboard = new Scanner(System.in);

        double next = keyboard.nextDouble();

        while ((next >= 0) && (!a.full())) {
            a.add(next);
            next = keyboard.nextDouble();
        }
        
        if (a.full())
            System.out.println("Could only read in " + a.getMaxCapacity() + " input values.");
    }

    public static double computeAverage(PartiallyFilledArray a) {
        double total = 0;
        for (int index = 0; index < a.getNumberOfElements(); index++) {
            total  += a.getElement(index);
        }

        if (a.getNumberOfElements() > 0) {
            return (total / a.getNumberOfElements());
        }
        else {
            System.out.println("ERROR: Trying to average 0 numbers.");
            System.out.println("computeAverage returns 0.");
            return 0;
        }
    }

    public static void showDifference(PartiallyFilledArray a) {
        double average = computeAverage(a);
        System.out.println("Average of the " + a.getNumberOfElements() + " scores = " + average);
        System.out.println("The scores are:");
        for (int index = 0; index < a.getNumberOfElements(); index++)
            System.out.println(a.getElement(index) + " differs from average by " + (a.getElement(index) - average));
    }
    
}
