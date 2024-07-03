import java.util.Scanner;

public class Date {
    private String month;
    private int day;
    private int year;

    public Date() {
        month = "January";
        day = 1;
        year = 1000;
    }

    public Date(int month, int day, int year) {
        setDate(month, day, year);
    }

    public Date(String month, int day, int year) {
        setDate(month, day, year);
    }

    public Date(int year) {
        setDate(1, 1, year);
    }

    public Date(Date aDate) {
        if (aDate == null) {
            System.out.println("Fatal Error.");
            System.exit(0);
        }

        month = aDate.month;
        day = aDate.day;
        year = aDate.year;
    }



    public String toString() {
        return(month + " " + day +", " + year);
    }

    public void writeOutput() {
        // System.out.println(this); // Gotta check whether this is valid or not
        System.out.println(month + " " + day +", " + year);
    }

    public void readInput() { // 7.

        boolean tryAgain = true;
        Scanner keyboard = new Scanner(System.in);
        while (tryAgain) {

            System.out.println("Enter month, day, and year.");
            System.out.println("Do not use a comma.");

            String monthInput = keyboard.next();
            int dayInput = keyboard.nextInt();
            int yearInput = keyboard.nextInt();

            if (dateOK(monthInput, dayInput, yearInput)) {
                setDate(monthInput, dayInput, yearInput);
                tryAgain = false;
            }

            else {
                System.out.println("Illegal date. Reenter input.");
            }
        }

    }

    public int getDay() {
        return(day);
    }

    public int getYear() {
        return(year);
    }

    public int getMonth() {
        if(month.equalsIgnoreCase("January"))
            return 1;
        else if (month.equalsIgnoreCase("February"))
            return 2;
        else if (month.equalsIgnoreCase("March"))
            return 3;
        else if (month.equalsIgnoreCase("April"))
            return 4;
        else if (month.equalsIgnoreCase("May"))
            return 5;
        else if (month.equalsIgnoreCase("June"))
            return 6;
        else if (month.equalsIgnoreCase("July"))
            return 7;
        else if (month.equalsIgnoreCase("August"))
            return 8;
        else if (month.equalsIgnoreCase("September"))
            return 9;
        else if (month.equalsIgnoreCase("October"))
            return 10;
        else if (month.equalsIgnoreCase("November"))
            return 11;
        else if (month.equalsIgnoreCase("December"))
            return 12;
        else {
            System.out.println("Fatal Error");
            System.exit(0);
            return 0; // To make the compiler happy
        }
    }

    public String monthString(int monthNumber) {
        switch(monthNumber) {
        case 1:
            return "January";
        case 2:
            return "February";
        case 3:
            return "March";
        case 4:
            return "April";
        case 5:
            return "May";
        case 6:
            return "June";
        case 7:
            return "July";
        case 8:
            return "August";
        case 9:
            return "September";
        case 10:
            return "October";
        case 11:
            return "November";
        case 12:
            return "December";
        default:
            System.out.println("Fatal Error");
            System.exit(0);
            return "Error";
        }
    }

    public boolean equals(Date otherDate) {
        return ( (this.month.equalsIgnoreCase(otherDate.month)) && (this.day == otherDate.day) && (this.year == otherDate.year) );
    }

    public boolean precedes(Date otherDate) {
        return ( (year < otherDate.year) || (year == otherDate.year && getMonth() < otherDate.getMonth())
        || (year == otherDate.year && month.equals(otherDate.month) && day < otherDate.day) );
    }

    private boolean dateOK(String month, int day, int year) { // 1.
        return(monthOK(month) && (day >= 1) && (day <= 31) && (year >= 1000) && (year <= 9999));

    }

    private boolean dateOK(int month, int day, int year) { // 1.
        return((month >= 1) && (month <= 12) && (day >= 1) && (day <= 31) && (year >= 1000) && (year <= 9999));
    }

    private boolean monthOK(String month) { // 2.
        return (month.equals("January") || month.equals("February") || month.equals("March") || month.equals("April") ||
        month.equals("May") || month.equals("June") || month.equals("July") || month.equals("August") ||
        month.equals("September") || month.equals("October") || month.equals("November") || month.equals("December"));
    
    }

    public void setDate(String month, int day, int year) { // 3.
        if (dateOK(month, day, year)) {
            this.month = month;
            this.day = day;
            this.year = year;
        }

        else {
            System.out.println("Fatal Error");
            System.exit(0);
        }
    }

    public void setDate(int month, int day, int year) { // 3.
        if (dateOK(month, day, year)) {
            this.month = monthString(month);
            this.day = day;
            this.year = year;
        }

        else {
            System.out.println("Fatal Error");
            System.exit(0);
        }
    }

    public void setDate(int year) { // 3.
        if ((year >= 1000) && (year <= 9999)) {
            setDate(1, 1, year);
        }

        else {
            System.out.println("Fatal Error");
            System.exit(0);
        }
    }

    public void setMonth(int month) { // 4.
        if ((month >= 1) && (month <= 12)) {
            this.month = monthString(month);
        }

        else {
            System.out.println("Fatal Error");
            System.exit(0);
        }
    }

    public void setDay(int day) { // 5.
        if ((day >= 1) && (day <= 31)) {
            this.day = day;
        }

        else {
            System.out.println("Fatal Error");
            System.exit(0);
        }
    }

    public void setYear(int year) { // 6.
        if ((year >= 1000) && (year <= 9999)) {
            this.year = year;
        }

        else {
            System.out.println("Fatal Error");
            System.exit(0);
        }
    }

}


