public class ToyExample {
    private Date[] a;
    
    public ToyExample(int arraySize) {
        a = new Date[arraySize];
        for (int i = 0; i < a.length; i++) {
            a[i] = new Date();
        }
    }

    public ToyExample(ToyExample object) {
        int lengthOfArrays = object.a.length;
        this.a = new Date[lengthOfArrays];
        for (int i = 0; i < object.a.length; i++) {
            a[i] = new Date(object.a[i]);
        }
    }

    public Date[] getDateArray() { // Accessor method.
        Date[] temp = new Date[a.length];
        for (int i = 0; i < a.length; i++) 
            temp[i] =
            new Date(a[i]); // Copy constructor for Date
        return temp;
    }
}
