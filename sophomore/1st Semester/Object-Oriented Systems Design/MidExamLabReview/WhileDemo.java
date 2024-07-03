public class WhileDemo {
    public static void main(String[] args) {
        int countDown = 3;
        System.out.println("First");
        while (countDown > 0) {
            System.out.println("Hello");
            countDown--;
        }

        countDown = 0;
        System.out.println("Second");
        do {
            System.out.println("Hello");
            countDown--;
        } while (countDown > 0);
    }
}
