/**
 * Java2nd5th
 */
public class Java2nd5th {

    public static void main(String[] args) {
        double price = 19.8;
        double value = 12.123;
        String name = "magic apple";
        // System.out.print("$"); // Does not create a new line
        System.out.printf("Start%8.2fEnd%n", value); // *Right justification
        System.out.printf("Start%-8.2fEnd%n", value); // *Left justification, line breaks can be included using %n
        // System.out.printf("$%6.2f for each %s.", price, name);
        // System.out.printf("%6.2f", price); // Does not create a new line
        // System.out.println(" each");
    }
}