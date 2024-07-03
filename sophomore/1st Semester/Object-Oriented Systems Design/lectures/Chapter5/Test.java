public class Test {
    public static void main(String[] args) {
        String greeting = "Hello"; // String class is not mutable
        String helloVariable = greeting;
        greeting = greeting + "friend.";
        System.out.println(helloVariable);
    }
}
