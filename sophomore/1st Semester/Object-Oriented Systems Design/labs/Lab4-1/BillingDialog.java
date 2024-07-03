import java.util.Scanner;

public class BillingDialog {
    public static void main(String[] args) {

        Scanner keyboard = new Scanner(System.in);
        Bill myBill = new Bill();
        
        System.out.println("Welcome to the law offices of");
        System.out.println("Dewey, Cheatham, and Howe.");
        myBill.inputTimeWorked();
        
        myBill.updateFee();
        myBill.outputBill();
        System.out.println("We have placed a line on your house.");
        System.out.println("It has been our pleasure to serve you.");
    }    
}
