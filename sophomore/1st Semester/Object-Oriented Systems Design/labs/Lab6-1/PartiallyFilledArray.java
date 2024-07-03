public class PartiallyFilledArray {
    private double[] a;
    private int maxNumberElements;
    private int numberUsed;

    public PartiallyFilledArray() {
        maxNumberElements = 10;
        numberUsed = 0;
        a = new double[maxNumberElements];
    }

    public PartiallyFilledArray(int arraySize) {
        if (arraySize <= 0) {
            System.out.println("Error: Array size zero or negative.");
            System.exit(0);
        } else {
            maxNumberElements = arraySize;
            numberUsed = 0;
            a = new double[maxNumberElements];
        }
    }

    public PartiallyFilledArray(PartiallyFilledArray original) {
        if (original == null) {
            System.out.println("Fatal Error: absorting program.");
            System.exit(0);
        } 

        maxNumberElements = original.maxNumberElements;
        numberUsed = original.numberUsed;
        a = new double[maxNumberElements];
        for (int i = 0; i < numberUsed; i++) {
            a[i] = original.a[i];
        }
    }

    public void add(double newElement) {
        if (numberUsed >= a.length) {
            System.out.println("Error: Adding to a full array");
            System.exit(0);
        } else {
            a[numberUsed++] = newElement;
        }
    }

    public double getElement(int index) {
        if ((index < 0) || (index >= numberUsed)) {
            System.out.println("Error: Illegal or unused index.");
            System.exit(0);
        }
        return a[index];
    }

    public void resetElement(int index, double newValue) {
        if (index < 0 || index >= maxNumberElements) {
            System.out.println("Error: Illegal index.");
            System.exit(0);
        } else if (index >= numberUsed) {
            System.out.println("Error: Changing an index that is too large.");
            System.exit(0);
        } else {
            a[index] = newValue;
        }
    }

    public void deleteLast() {
        if (empty()) {
            System.out.println("Error: Deleting from an empty array.");
            System.exit(0);
        } else {
            numberUsed--;
        }
    }

    public void delete(int index) {
        if (index < 0 || index >= numberUsed) {
            System.out.println("Error: Illegal or unused index.");
            System.exit(0);
        } 
        for (int i = 0; i < numberUsed; i++) {
            a[i] = a[i + 1];
        }
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
}