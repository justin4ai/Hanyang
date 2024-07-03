public class TurnTaker {
    private static int turn = 0;
    private int myTurn;
    private String name;

    public TurnTaker() {
        name = "No name yet";
        myTurn = 0;
    }

    public TurnTaker(String name, int turn) {
        this.name = name;

        if (turn >= 0) {
            myTurn = turn;
        }

        else {
            System.out.println("Fatal Error");
            System.exit(0);
        }
    }

    public String getName() {
        return name;
    }

    public static int getTurn() {
        return ++turn;
    }

    public boolean isMyTurn() {
        return (myTurn == turn);
    }


}
