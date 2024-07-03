public class PrintDemo {
    public static void main(String[] args) {
        String aString = "abc";

        System.out.println("String output:");
        System.out.println("START1234567890");
        System.out.printf("START%sEND %n", aString);
        System.out.printf("START%4sEND %n", aString);
        System.out.printf("START%2sEND %n", aString); // Be careful about this format specifier
        System.out.println();

        char oneCharacter = 'Z';
        System.out.println("Character output:");
        System.out.println("START1234567890");
        System.out.printf("START%cEND %n", oneCharacter); // Just one z
        System.out.printf("START%4cEND %n", oneCharacter); // Three spaces & one z
        System.out.println();

        double d = 12345.123456789;

        System.out.println("Floating-point output:");
        System.out.println("START1234567890");
        System.out.printf("START%fEND %n", d); // 6 digits for floating points by default
        System.out.printf("START%.4fEND %n", d); // Truncated (by rounding)
        System.out.printf("START%.2fEND %n", d);
        System.out.printf("START%12.4fEND %n", d);
        System.out.printf("START%eEND %n", d);
        System.out.printf("START%12.5eEND %n", d);

    }
}
