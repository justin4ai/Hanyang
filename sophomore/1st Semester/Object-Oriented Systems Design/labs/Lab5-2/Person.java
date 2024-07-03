public class Person {
    private String name;
    private Date born;
    private Date died;

    Person(String name, Date birth, Date death) {
        if (consistent(birth, death)) {
            this.name = name;
            this.born = new Date(birth); // Important
            if (death == null)
                died = null;
            else 
                died = new Date(death);
        }

        else {
            System.out.println("Inconsistent dates. Aborting.");
            System.exit(0);
        }
    }

    Person(Person original) {
        if (original == null) {
            System.out.println("Fatal error.");
            System.exit(0);
        }

        else {
            this.name = original.name; /// confusing
            this.born = new Date(original.born);
            
            if (original.died == null)
            this.died = null;

        else
            this.died = new Date(original.died);
        }
    }

    public String toString() {
        String diedString;
        if (died == null) {
            diedString = "";
        }

        else {
            diedString = died.toString();
        }
        return (name + ", " + born + "-" + diedString);
    }

    public boolean equals(Person otherPerson) {
        if (otherPerson == null) {
            return false;
        }

        return (this.name.equals(otherPerson.name) && datesMatch(this.born, otherPerson.born) && datesMatch(this.died, otherPerson.died));
    }

    private static boolean datesMatch(Date date1, Date date2) {
        if (date1 == null)
            return (date2 == null);

        else if (date2 == null)
            return false;
        else
            return (date1.equals(date2));

    }

    public void setBirthDate(Date date) {
        if (consistent(date, died))
            born = new Date(date);

        else {
            System.out.println("Inconsistent dates. Aborting.");
            System.exit(0);
        }
    }

    public void setDeathDate(Date date) {
        if (!consistent(born, date)) {
            System.out.println("Incosistent dates. Aborting.");
            System.exit(0);
        }

        if (date == null)
            died = null;
        else
            died = new Date(date);
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setBirthYear(int year) {
        if (born == null) {
            System.out.println("Fatal Error. Aborting.");
            System.exit(0);
        }

        born.setYear(year);
        if (!consistent(born, died)) {
            System.out.println("Inconsistent dates. Aborting.");
            System.exit(0);
        }
    }

    public void setDeathYear(int year) {
        if (died == null) {
            System.out.println("Fatal Error. Aborting.");
            System.exit(0);
        }

        died.setYear(year);
        if (!consistent(born, died)) {
            System.out.println("Inconsistent dates. Aborting.");
            System.exit(0);
        }
    }

    public String getName() {
        return name; // not good (privacy leak)
    }

    public Date getBirthDate() {
        return new Date(born); // good and safe
    }

    public Date getDeathDate() {
        if (died == null)
            return null;
        else
            return new Date(died);
    }

    private static boolean consistent(Date birthDate, Date deathDate) {
        if (birthDate == null)
            return false;
        else if (deathDate == null)
            return true;
        else 
            return (birthDate.precedes(deathDate) || birthDate.equals(deathDate));
    }



}

