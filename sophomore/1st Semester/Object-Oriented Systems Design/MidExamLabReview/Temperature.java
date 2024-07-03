import java.util.Scanner;

public class Temperature {
    private double degrees;

    public Temperature() {
        degrees = 0;
    }

    public Temperature(double degrees) {
        this.degrees = degrees;
    }

    public void setDegrees(double degrees) {
        this.degrees = degrees;
    }

    public double getDegrees() {
        return degrees;
    }

    public String toString() {
        return degrees + "C";
    }

    public boolean equals(Temperature otherTemperature) {
        return (this.degrees == otherTemperature.degrees);
    }

    public static double toCelsius(double degreesF) {
        return 5*(degreesF - 32) / 9;
    }

    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);
        System.out.println("Enter degrees Fahrenheit");
        double degree = keyboard.nextDouble();
        System.out.println("Equivalent Celsius temperature is " + toCelsius(degree) + 'C');
        
    }


}
