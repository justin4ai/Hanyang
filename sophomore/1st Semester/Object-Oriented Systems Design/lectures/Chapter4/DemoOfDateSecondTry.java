public class DemoOfDateSecondTry {
    
    public static void main(String[] args) {
        DateSecondTry date = new DateSecondTry();
        date.readInput();

        int dayNumber = date.getDay();
        // int dayNumber = date.day; // <- We cannot access since date.day is a ,,private'' variable.

        System.out.println("That is the " + dayNumber + "th day of the month.");

    }
}
