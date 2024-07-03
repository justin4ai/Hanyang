public class ParametersDemo {
    public static void main(String[] args) {
    ToyClass2 object1 = new ToyClass2();
    ToyClass2 object2 = new ToyClass2();
    object1.set("Scorpius", 1);
    object2.set("John Crichton", 2);
    System.out.println("Value of object2 before call to method:");
    System.out.println(object2);
    System.out.println("Value of object2 after call to method:");
    object1.makeEqual(object2);
    System.out.println(object2);
    int number = 42;
    System.out.println("Value of number before call to method: " + number);
    object1.tryToMakeEqual(number);
    System.out.println("Value of number after call to method: " + number);
    }
    
}
