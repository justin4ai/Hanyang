public class ShowInterest {

    public static final double INTEREST_RATE = 2.5;
    public static void main(String[] args) {
        
        double balance = 100.0;
        double interest = balance * (INTEREST_RATE/100.0);
        

        System.out.printf("On a balance of $%.1f%n", balance);
        System.out.printf("you will earn interest of $%.1f%n", interest);
        System.out.println("All in just one short year");
    }
}
