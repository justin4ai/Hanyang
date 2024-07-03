public class Utility2 {
    public static String censor(String sentence, String... unwanted) {
        for (int i = 0; i < unwanted.length; i++) {
            sentence = deleteOne(sentence, unwanted[i]);
        // for (String element : unwanted) { // using for-each loop
        //     sentence = deleteOne(sentence, element)
        //}
        }
        return sentence;
    }
    
    private static String deleteOne(String sentence, String oneUnwanted) {
        String ending;
        int position = sentence.indexOf(oneUnwanted);
        System.out.println("position:" + position);
        while (position >= 0) {
            ending = sentence.substring(position + oneUnwanted.length());
            sentence = sentence.substring(0, position) + ending;
            position = sentence.indexOf(oneUnwanted);

        }
        return sentence;
    }
}
