public class YourCloneableClass2 implements Cloneable{
    private Date someDate; // Mutable
    private int a;
    private String b;

    public Object clone() {
        try {
            YourCloneableClass2 copy = (YourCloneableClass2)super.clone();
            copy.someDate = (Date) someDate.clone();
            return copy;
        }

        catch (CloneNotSupportedException e) {
            return null;
        }

    }
}
