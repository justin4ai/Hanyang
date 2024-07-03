public class TurnTaker {
    private static int turn = 0;
    private int myTurn;
    private String name;

    public TurnTaker(String name, int turn) {
        this.name = name;

        if (turn >= 0) {
            this.myTurn = turn;
        }

        else {
            System.out.println("Fatal Error");
            System.exit(0);
        }
    }

    public TurnTaker() {
        this.name = "No name yet";
        this.myTurn = 0;
    }

    public String getName() {
        return this.name;
    }

    public static int getTurn() {
        turn++;
        return turn;
    }

    public boolean isMyTurn() {
        return (myTurn == turn);
    }
}
