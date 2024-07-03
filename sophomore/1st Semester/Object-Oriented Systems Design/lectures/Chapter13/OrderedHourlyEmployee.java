public class OrderedHourlyEmployee extends HourlyEmployee implements Ordered {
    
    public boolean precedes(Object other) {
        if (other == null) {
            return false;
        }

        else if (!(other instanceof OrderedHourlyEmployee)) { // The same to .getClass() here
            return false;
        }

        else {
            OrderedHourlyEmployee otherOrderedHourlyEmployee = (OrderedHourlyEmployee) other;
            return (getPay() < otherOrderedHourlyEmployee.getPay());
        }
    }

    public boolean follows(Object other) {
        if (other == null) {
            return false;
        }

        else if (!(other instanceof OrderedHourlyEmployee)) { // The same to .getClass() here
            return false;
        }

        else {
            OrderedHourlyEmployee otherOrderedHourlyEmployee = (OrderedHourlyEmployee) other;
            return (otherOrderedHourlyEmployee.precedes(this));
        }
    }
}
