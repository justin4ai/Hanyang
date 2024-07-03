import java.util.Scanner;

public class RoundStuff2 {


    public static double area(double radius) {
        return(Math.PI * radius * radius);
    }

    public static double volume(double radius) {
        return((4.0/3.0)*Math.PI*radius*radius*radius);
    }
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Enter radius:");
        double radius = keyboard.nextDouble();

        System.out.println("A circle of radius " + radius + " inches");
        System.out.println("has an area of " + area(radius) + " square inches."); // thanks to static method
        System.out.println("A sphere of radius " + radius + " inches");
        System.out.println("has a volume of " + volume(radius) + "cubic inches.");
    }
}
