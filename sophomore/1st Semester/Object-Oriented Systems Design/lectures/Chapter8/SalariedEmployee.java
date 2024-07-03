public class SalariedEmployee extends Employee {
    private double salary;

    public SalariedEmployee() {
        super();
        salary = 0;
    }

    public SalariedEmployee (String theName, Date theDate, double theSalary) {
        super(theName, theDate);
        if (theSalary >= 0) {
            salary = theSalary;
        }

        else {
            System.out.println("Fatal Error: Negative salary.");
            System.exit(0);
        }
    }

    public SalariedEmployee (SalariedEmployee originalObject) {
        super(originalObject); // copy constructor
        salary = originalObject.salary;
    }

    public double getSalary() {
        return salary;
    }

    public double getPay() {
        return salary/12;
    }

    public void setSalary(double newSalary) {
        if (newSalary >= 0) {
            salary = newSalary;
        }

        else {
            System.out.println("Fatal Erorr: Negative salary.");
            System.exit(0);
        }
    }

    public String toString() {
        return (getName() + " " + getHireDate().toString() + "\n$" + salary + " per year");

    }

    public boolean equals(Object otherObject) {

        if (otherObject == null) {
            return false;
        }

        else if (getClass() != otherObject.getClass()) {
            return false;
        }

        else {
            SalariedEmployee otherSalariedEmployee = (SalariedEmployee) otherObject;
            return (getName().equals(otherSalariedEmployee.getName())
            && getHireDate().equals(otherSalariedEmployee.getHireDate())
            && salary == otherSalariedEmployee.salary);
        }
    }
}
