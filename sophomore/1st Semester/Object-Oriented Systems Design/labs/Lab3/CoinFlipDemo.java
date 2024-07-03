import java.util.Random;

public class CoinFlipDemo {
    public static void main(String[] args) {
        
        Random randomGenerator = new Random();
    
        for (int i = 0; i < 5; i++) {
            int coinFlip = randomGenerator.nextInt(2);
            if (coinFlip == 1) {
                System.out.println("Flip number 1: Heads");
            }

            else {
                System.out.println("Flip number 1: Tails");
            }
        }
    }
}
