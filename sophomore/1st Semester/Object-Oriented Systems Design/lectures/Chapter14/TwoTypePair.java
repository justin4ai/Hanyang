import java.net.PortUnreachableException;

public class TwoTypePair<T1, T2> {
    private T1 first;
    private T2 second;

    public TwoTypePair() { // Constructor heaindgs do not include the type parameter in angular brackets.
        first = null;
        second = null;
    }

    public TwoTypePair(T1 firstItem, T2 secondItem) {
        first = firstItem;
        second = secondItem;
    }

    public void setFirst(T1 newFirst) {
        first = newFirst;
    }

    public void setSecond(T2 newSecond) {
        second = newSecond;
    }

    public T1 getFirst() {
        return first;
    }

    public T2 getSecond() {
        return second;
    }

    public String toString() {
        return ("first: " + first + "\n" + "second: " + second);
    }

    public boolean equals(Object otherObject) {
        if (otherObject == null)
            return false;
        else if (getClass() != otherObject.getClass()) {
            return false;
        }

        else {
            TwoTypePair<T1, T2> otherPair = (TwoTypePair<T1, T2>) otherObject ;
            return (first.equals(otherPair.first) &&
            second.equals(otherPair.second));
        }
    }

}
