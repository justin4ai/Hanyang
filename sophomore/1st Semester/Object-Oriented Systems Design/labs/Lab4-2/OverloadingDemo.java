/**
 * OverloadingDemo
 */
public class OverloadingDemo {
    public static void main(String[] args) {
        Date date1 = new Date();
        Date date2 = new Date();
        Date date3 = new Date();

        date1.setDate(2022);
        System.out.println(date1);
        date2.setDate("April", 6, 2022);
        System.out.println(date2);
        date3.readInput();
        System.out.println(date3);
    }
}