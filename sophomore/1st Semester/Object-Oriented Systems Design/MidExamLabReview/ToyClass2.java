public class ToyClass2 {
    private String name;
    private int number;

    ToyClass2(String name, int number) {
        this.name = name;
        this.number = number;
    }

    ToyClass2() {
        this.name = "No name yet.";
        this.number = 0;
    }

    public void set(String name, int number) {
        this.name = name;
        this.number = number; 
    }

    public String toString() {
        return (this.name + " " + number);
    }

    public static void changer(ToyClass2 aParameter) {
        aParameter.name = "Hot Shot";
        aParameter.number = 42;
    }

    public boolean equals(ToyClass2 otherObject) {
        return (name == otherObject.name) && (number == otherObject.number);
    }

    public void makeEqual(ToyClass2 anObject) {
        anObject.name = this.name;
        anObject.number = this.number;
    }

    public void tryToMakeEqual(int number) {
        number = this.number;
    }

}