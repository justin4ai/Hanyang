public class AbstractClassDemo {
    public static void showEmployee(Employee employeeObject) {
        System.out.println("Name : " + employeeObject.getName());
        System.out.println("Hire Date : " + employeeObject.getHireDate());
        System.out.println("Pay : $ " + employeeObject.getPay()); // Thanks to abstract method
        System.out.println("==============================");
    }

    public static void main(String[] args) {
        SalariedEmployee joe = new SalariedEmployee("Joe", new Date("January", 1, 2015), 100000);
        HourlyEmployee sam = new HourlyEmployee("Sam", new Date("February", 1, 2016), 50.50, 40);
        showEmployee(joe);
        showEmployee(sam);
        if (joe.getPay() == sam.getPay()) {
            System.out.println("They have the same pay.");
        }

        else {
            System.out.println("They don't have the same pay.");
        }
    }
}
