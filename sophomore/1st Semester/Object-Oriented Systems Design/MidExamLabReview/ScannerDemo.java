import java.util.Scanner;

public class ScannerDemo {
    public static void main(String[] args) {
        Scanner keyboard = new Scanner(System.in);

        System.out.println("Enter the number of pods followed by");
        System.out.println("the number of peas in a pod:");
        int numberOfPods = keyboard.nextInt();
        int peasPerPod = keyboard.nextInt();

        System.out.printf("%d pods and %d peas per pod.%n", numberOfPods, peasPerPod);
        int totalNumberOfPeas = numberOfPods* peasPerPod;
        System.out.println("The total number of peas = " + totalNumberOfPeas);

    }
}
