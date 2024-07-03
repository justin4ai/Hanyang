public class StringProcessDemo {
    public static void main(String[] args) {
        
        String word = "hate";
        String sentence = "I hate text processing!";
        
        System.out.println("01234567890123456789012");
        System.out.println(sentence);

        System.out.printf("The word \"%s\" starts at index %d %n", word, sentence.indexOf(word));
        System.out.println("The changed string is:");
        System.out.println(sentence.substring(0, sentence.indexOf(word)) + "adore" + sentence.substring( sentence.indexOf(word) + word.length()));
    }
}
