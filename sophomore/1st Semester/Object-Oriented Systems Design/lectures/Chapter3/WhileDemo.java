public class WhileDemo {
    public static void main(String[] args) {
        int countDown;
        System.out.println("First while loop:");
        countDown = 3;
        while (countDown > 0) {
            System.out.println("Hello");
            countDown -= 1;
        }
        System.out.println("Second while loop:");
        countDown = 0;
        while (countDown > 0) {
            System.out.println("Hello");
            countDown -= 1;
        }

        // do-while : this executes the loop body at least once even when the condition is not met.
        System.out.println("First do-while loop:");
        countDown = 3;
        do {
            System.out.println("Hello");
            countDown -= 1;
        } while (countDown > 0); // do-while requires the semi-colon after while expression.

        System.out.println("Second do-while loop:");
        countDown = 0;
        do {
            System.out.println("Hello");
            countDown -= 1;
        } while (countDown > 0); // do-while requires the semi-colon after while expression.

    }
}
