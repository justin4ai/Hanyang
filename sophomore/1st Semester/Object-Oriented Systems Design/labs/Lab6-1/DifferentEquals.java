public class DifferentEquals {

    public static boolean equalArrays(int[] a, int[] b) {
        if ((a.length) != (b.length)) {
            return false;
        }

        for (int i = 0; i < 10; i++) {
            if (a[i] != b[i]) {
                return false;
            }
        }

        return true;
    }
    public static void main(String[] args) {
        int[] c = new int[10];
        int[] d = new int[10];


        
        for (int i = 0; i < 10; i++) {
            c[i] = i;
            d[i] = i;
        }

        if (c == d) {
            System.out.println("c and d are equal by ==.");
        }

        else {
            System.out.println("c and d are not equal by ==.");
        }
        System.out.println("== only tests memory adresses.");

        if (equalArrays(c, d)) {
            System.out.println("c and d are equal by the equalArrays method.");
        }

        else {
            System.out.println("c and d are equal by the equalArrays method.");
        }

        System.out.println("An equalArryas method is usually a more useful test");


    }

}
