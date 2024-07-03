import java.util.Random;

public class CoinFlipDemo {
    public static void main(String[] args) {
        Random randomGenerator = new Random();
        int counter = 1;
    
        while (counter <= 5) {
            System.out.println("Flip number " + counter + ": ");
            int coinFlip = randomGenerator.nextInt(2); // from 0 to n, from 0 to 1 (exclusive) if we use .nextDouble()
            if (coinFlip == 1)
                System.out.println("Heads");
            else
                System.out.println("Tails");
    
            counter++;
    }


    }
}
