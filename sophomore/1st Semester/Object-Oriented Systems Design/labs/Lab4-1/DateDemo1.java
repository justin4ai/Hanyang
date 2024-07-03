public class DateDemo1 {
    public static void main(String[] args) {
        Date myDate = new Date();
        Date myDate2 = new Date();

        myDate.readInput();
        myDate2.setDate(8, 15, 1945);


        if(myDate.equals(myDate2))
            System.out.println(myDate + " equals " + myDate2);
        else
            System.out.println(myDate + " does not equal " + myDate2);

        if (myDate2.precedes(myDate))
            System.out.println(myDate2 + " comes before " + myDate);
        else
            System.out.println(myDate2 + " does not come before " + myDate);


    }
}
