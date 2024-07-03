public class BillingDialog {
    public static void main(String[] args) {
        System.out.println("Welcome to the law offices of");
        System.out.println("Bewey, Cheatham, and Howe.");
        Bill yourBill = new Bill();
        yourBill.inputTimeWorked();
        yourBill.updateFee();
        yourBill.outputBill();
        System.out.println("We have a placed a lien on your house.");
        System.out.println("It has been our pleasure to serve you.");
    }
}
