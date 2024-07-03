public class HighScore {
    private int score = 0;
    private boolean scoreSet = false;

    public HighScore() {
        score = 0;
        scoreSet = false;
    }

    public void setScore(int newScore) {
        score = newScore;
        scoreSet = true;
    }

    public int getScore() throws ScoreNotSetException{
        if (!scoreSet) {
            throw new ScoreNotSetException();
        }

        else {
            return score;
        }
    }

    public static void main(String[] args) {
        HighScore highScore = new HighScore();
        try {
        System.out.println(highScore.getScore());
        }
        catch (ScoreNotSetException e) {
            System.out.println(e.getMessage());
        }
        highScore.setScore(100);
        try {
            System.out.println(highScore.getScore());
        }
        catch (ScoreNotSetException e) {
            System.out.println(e.getMessage());
        }
    }
}
