public class ScoreNotSetException extends Exception {
    public ScoreNotSetException() {
        super("Score not set");
    }

    public ScoreNotSetException(String message) {
        super(message);
    }
}
