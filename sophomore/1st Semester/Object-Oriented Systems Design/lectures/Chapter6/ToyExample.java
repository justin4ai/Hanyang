public class ToyExample {
    private Date[] a;

    public ToyExample(int arraySize) {
        a = new Date[arraySize];
        for (int i = 0; i < arraySize; i++) {
            a[i] = new Date();
        }
    
    }

    public ToyExample(ToyExample object) { // Copy constructor for ToyExample
        int lengthOfArrays = object.a.length;
        this.a = new Date[lengthOfArrays];
        for (int i = 0; i < lengthOfArrays; i++) {
            this.a[i] =
            new Date(object.a[i]); // Copy constructor for Date
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
