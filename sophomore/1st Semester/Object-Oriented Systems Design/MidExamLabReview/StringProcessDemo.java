public class StringProcessDemo {
    public static void main(String[] args) {
        String sentence = "I hate text processing!";
        String word = "hate";
        System.out.println("01234567890123456789012");
        System.out.println(sentence);
        System.out.println("The word \"hate\" starts at index " + sentence.indexOf(word));
        System.out.println("The changed string is:");
        System.out.println(sentence.substring(0,sentence.indexOf(word)) + 
        "adore" + sentence.substring(sentence.indexOf(word) + word.length(), sentence.length() ) );
        ..
    }
}
