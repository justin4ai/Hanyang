public abstract class MyAbstractClass implements Ordered {
    private int number;
    private char grade;

    public boolean precedes(Object other) {
        if (other == null) {
            return false;
        }

        else if (!(other instanceof MyAbstractClass)) { // The same to .getClass() here
            return false;
        }

        else {
            MyAbstractClass otherOfMyAbstractClass = (MyAbstractClass) other;
            return (this.number < otherOfMyAbstractClass.number);
        }
    }

    public abstract boolean follows(Object other) ; // Since this is not defined,
                                                    // abstract keyword is added to this method and also to the class.
}
