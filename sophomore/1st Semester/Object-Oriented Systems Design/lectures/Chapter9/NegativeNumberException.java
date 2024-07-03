public class NegativeNumberException extends Exception{
    private int negativeNumber;
    public NegativeNumberException(int number) {
        super("NegativeNumberException");
        negativeNumber = number;
    }

    public NegativeNumberException() {
        super("NegativeNumberException");
    }

    public NegativeNumberException(String message) {
        super(message);
    }


    public int getNegativeNumber() {
        return negativeNumber;
    }

}
