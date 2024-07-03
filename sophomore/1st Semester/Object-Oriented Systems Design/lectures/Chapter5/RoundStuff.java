public class RoundStuff {
    public static final double PI = 3.14159;

    public static double area(double radius) { // static keyword -> not related to object
        return(PI * radius * radius);
    }

    public static double volume(double radius) {
        return((4.0/3.0)*PI*radius*radius*radius);
    }
}