import java.util.Scanner;

public class PartiallyFilledArray {
    private int maxNumberElements;
    private double[] a;
    private int numberUsed;


    PartiallyFilledArray() {
        maxNumberElements = 10;
        a = new double[maxNumberElements];
        numberUsed = 0;
    }

    PartiallyFilledArray(int arraySize) {
        if (arraySize <= 0) {
            System.out.println("Error Array size zero or negative.");
            System.exit(0);
        }

        maxNumberElements = arraySize;
        a = new double[maxNumberElements];
        numberUsed = 0;

    }

    PartiallyFilledArray(PartiallyFilledArray original) { // Copy constructor
        if (original == null) {
            System.out.println("Fatal Error: aborting program.");
            System.exit(0);
        }

        maxNumberElements = original.maxNumberElements;
        numberUsed = original.numberUsed;
        a = new double[maxNumberElements];
        for (int i = 0; i < numberUsed; i++)
            a[i] = original.a[i];
    }

    public void add(double newElement) {
        if (numberUsed >= a.length) {
            System.out.println("Error: Adding to a full array.");
            System.exit(0);
        }

        else
            a[numberUsed++] = newElement;
    }

    public double getElement(int index) {
        if (index < 0 || index >= numberUsed) {
            System.out.println("Error: Illegal or unused index.");
            System.exit(0);
        }
        return a[index];
    }

    public void resetElement(int index, double newValue) {
        if (index < 0 || index >= maxNumberElements) {
            System.out.println("Error: Illegal index.");
            System.exit(0);
        }
        else if (index > numberUsed) {
            System.out.println("Error: Changing an index that is too large.");
            System.exit(0);  
        }
        else 
            a[index] = newValue;

    }

    public void deleteLast() {
        if (empty()) {
            System.out.println("Error: Deleting from an empty array.");
            System.exit(0);
        }
        else
            numberUsed--;
    }

    public void delete(int index) {
        if (index < 0 || index >= numberUsed) {
            System.out.println("Error: Illegal or unused index.");
            System.exit(0);
        }
        for (int i = index; i < numberUsed; i++) 
            a[i] = a[i + 1];
        numberUsed--;
    }

    public boolean empty() {
        return (numberUsed == 0);
    }

    public boolean full() {
        return (numberUsed == maxNumberElements);
    }

    public int getMaxCapacity() {
        return maxNumberElements;
    }

    public int getNumberOfElements() {
        return numberUsed;
    }

    public static int fillArray(double[] a) {
        System.out.println("Enter up to " + a.length + " nonnegative numbers.");
        System.out.println("Mark the end of the list with a negative number.");
        Scanner keyboard = new Scanner(System.in);

        double next;
        int index = 0;
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
        for (int index = 0; index < numberUsed; index++)
            total = total + a[index];
        if (numberUsed > 0) {
            return (total / numberUsed);
        }
        else {
            System.out.println("ERROR: Trying to average 0 numbers.");
            System.out.println("computeAverage returns 0.");
            return 0;
        }
    }

    public static void showDifference(double[] a, int numberUsed) {
        double average = computeAverage(a, numberUsed);
        System.out.println("Average of the " + numberUsed + " scores = " + average);
        System.out.println("The scores are:");
        for (int index = 0; index < numberUsed; index++)
            System.out.println(a[index] + " differs from average by " + (a[index] - average));
    }
}
