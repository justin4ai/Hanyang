import java.util.Scanner;

public class Temperature {
    private double degrees; // instance variable
    
    public Temperature() {
        degrees = 0;
    }

    public Temperature(double initialDegrees) {
        degrees = initialDegrees;
    }

    public void setDegrees(double newDegrees) {
        degrees = newDegrees;
    }

    public double getDegrees() {
        return degrees;
    }
    
    public String toString() {
        return (degrees + " C");
    }

    public boolean equals(Temperature otherTemperature) {
        return (degrees == otherTemperature.degrees);
    }

    public static double toCelcius(double degreesF) {
        return 5*(degreesF - 32)/9;
    }

    public static void main(String[] args) {
        double degreesF, degreesC;
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Enter degrees Fahrenheit:");
        degreesF = keyboard.nextDouble();
        degreesC = toCelcius(degreesF); // equivalent to Temperature.toCelcius()
        Temperature temperatureObject = new Temperature(degreesC);
        System.out.println("Equivalent Celsius temperature is " + temperatureObject.toString());

        

    }
}
