import java.util.Scanner;

public class VariableParameterDemo {
    public static void main(String[] args) {
        System.out.println("Enter scores for Tom, Dick and Harriet:");
        Scanner keyboard = new Scanner(System.in);
        int tomsScore = keyboard.nextInt();
        int dicksScore = keyboard.nextInt();
        int harrietsScore = keyboard.nextInt();

        int highestScore = UtilityClass.max(tomsScore, dicksScore, harrietsScore); // double을 int에 넣는건 안됨.
        System.out.println("Highest score = " + highestScore);
    }
}
