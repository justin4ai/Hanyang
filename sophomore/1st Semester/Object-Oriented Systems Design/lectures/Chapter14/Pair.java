public class Pair<T extends Comparable> {
    private T first;
    private T second;

    public Pair() { // Constructor heaindgs do not include the type parameter in angular brackets.
        first = null;
        second = null;
    } 

    public Pair(T firstItem, T secondItem) {
        first = firstItem;
        second = secondItem;
    }

    public T max() {
        if (first.compareTo(second) >= 0) {
            return first;
        }
        else 
            return second;
    }

    public void setFirst(T newFirst) {
        first = newFirst;
    }

    public void setSecond(T newSecond) {
        second = newSecond;
    }

    public T getFirst() {
        return first;
    }

    public T getSecond() {
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
            Pair<T> otherPair = (Pair<T>) otherObject ;
            return (first.equals(otherPair.first) &&
            second.equals(otherPair.second));
        }
    }

}
