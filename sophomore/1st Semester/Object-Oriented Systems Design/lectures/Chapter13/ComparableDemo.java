public class ComparableDemo {
    public static void main(String[] args) {
        Double[] d = new Double[10]; // Wrapper class !
        
        for (int i = 0; i < d.length; i ++) {
            d[i] = Double.valueOf(d.length - i); // IMPORTANT : Regarding this as a enumerate data - better than using new Double() constructor
        }
        System.out.println("before sorting:");
        int i;
        for (i = 0; i < d.length; i++) {
            System.out.print(d[i].doubleValue() + " ");
        }
        System.out.println();
    
        GeneralizedSelectionSort.sort(d, d.length);
        System.out.println("After sorting.");
        for (i = 0; i < d.length; i++) {
            System.out.print(d[i].doubleValue() + ", ");
        }
        System.out.println();


        String[] a = new String[10];
        a[0] = "dog";
        a[1] = "cat";
        a[2] = "cornish game hen";
        int numberUsed = 3;

        System.out.println("Before sorting");
        for(i = 0; i < numberUsed; i++) {
            System.out.print(a[i] + ", ");
        }
        System.out.println();
        GeneralizedSelectionSort.sort(a, numberUsed);
        for(i = 0; i < numberUsed; i++) {
            System.out.print(a[i] + ", ");
        }
        System.out.println();

    }

}
