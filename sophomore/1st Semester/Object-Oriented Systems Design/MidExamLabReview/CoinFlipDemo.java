import java.util.Random;

public class CoinFlipDemo {
    public static void main(String[] args) {
        int coinFlip;
        Random randomgenerator = new Random();
        for (int i = 0; i < 5; i++) {
            
            coinFlip = randomgenerator.nextInt(2);

            if (coinFlip == 1) {
                System.out.println("Heads");
            } else if (coinFlip == 0) { 
                System.out.println("Tails");
            }
        }
    }
}
