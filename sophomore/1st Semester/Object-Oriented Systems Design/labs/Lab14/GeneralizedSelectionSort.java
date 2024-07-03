public class GeneralizedSelectionSort {
    public static void sort(Comparable [] a, int numberUsed) {
        int index, indexOfNextSmallest;
        for (index  = 0; index < numberUsed - 1; index++) {
            indexOfNextSmallest = indexOfSmallest(index, a, numberUsed);
            interchange(index, indexOfNextSmallest, a);
        }

    }

    private static int indexOfSmallest(int startIndex, Comparable[] a, int numberUsed) {
        Comparable min = a[startIndex];
        int indexOfMin = startIndex;
        int index;


        for (index = startIndex + 1; index < numberUsed; index ++) {
            if ( a[index].compareTo(min) < 0 ) {
                min = a[index];
                indexOfMin = index;
            }
        }

        return indexOfMin;
    }

    private static void interchange(int i, int j, Comparable[] a) {
        Comparable temp;
        temp = a[i];
        a[i] = a[j];
        a[j] = temp;
    }
}
