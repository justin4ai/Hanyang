import java.util.Scanner;

public class ArrayOfScores {
    public static void main(String[] args) {
        double[] score = new double[5];
        int index;
        double max;

        System.out.println("Enter 5 scores:");
        Scanner keyboard = new Scanner(System.in);
        
        
        score[0] = keyboard.nextDouble();
        max = score[0];
        for (index = 1; index < 5; index++) {
            score[index] = keyboard.nextDouble();

            if (max < score[index]) {
                max = score[index];
            }
        }

        System.out.println("The highest score is " + max);
        System.out.println("The scores are:");
        for (index = 0; index < 5; index++) {
            System.out.println(score[index] + " differs from max by " + (max - score[index]));
        }
    }
}