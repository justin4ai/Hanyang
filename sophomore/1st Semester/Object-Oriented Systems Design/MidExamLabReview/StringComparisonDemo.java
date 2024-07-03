public class StringComparisonDemo {
    public static void main(String[] args) {
        String s1 = "Java isn\'t just for breakfast.";
        String s2 = "JAVA isn\'t just for breakfast.";
        String s3 = "A cup of java is a joy forever.";

        if (s3.compareToIgnoreCase(s1) < 0) {
            System.out.println("dd ");
        }
    }
}
