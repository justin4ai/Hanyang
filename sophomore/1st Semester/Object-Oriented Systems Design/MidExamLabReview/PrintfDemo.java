public class PrintfDemo {
    public static void main(String[] args) {

        String aString = "abc";
        char oneCharacter = 'Z';
        double d = 12345.123456789;

        System.out.println("String output:");
        System.out.println("START1234567890");
        System.out.printf("START%sEND%n", aString);
        System.out.printf("START%4sEND%n", aString);
        System.out.printf("START%2sEND%n%n", aString);

        System.out.println("Character output:");
        System.out.println("START1234567890");
        System.out.printf("START%cEND%n", oneCharacter);
        System.out.printf("START%4cEND%n%n", oneCharacter);

        System.out.println("Floating-point output:");
        System.out.println("START1234567890");
        System.out.printf("START%12.8fEND%n", d);
        System.out.printf("START%12.6END%n", d);
        System.out.printf("START%12.4END%n", d);
        System.out.printf("START%8.4END%n", d);
        ..
    }
}
