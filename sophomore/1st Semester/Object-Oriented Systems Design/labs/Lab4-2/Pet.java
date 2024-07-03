public class Pet {
    private String name;
    private int age;
    private double weight;

    public String toString() {
        return("Name: " + name + "\nAge: " + age + " years" + "\nWeight: " + weight + " pounds");
    }

    public Pet(String name, int age, double weight) {
        
        if ((age < 0) | (weight < 0)) { 
            System.out.println("Error: Negative age or weight.");
            System.exit(0);
    
        }

        else {
            this.name = name;
            this.age = age;
            this.weight = weight;
        }

    }

    public Pet(String name) {
        this.name = name;
        this.age = 0;
        this.weight = 0.0;
    }

    public Pet(int age) {
        if (age < 0) {
            System.out.println("Error: Negative age.");
            System.exit(0);
        }

        else {
            this.name = "No name yet.";
            this.age = age;
            this.weight = 0;
        }

    }

    public Pet(double weight) {
        if (weight < 0) {
            System.out.println("Error: Negative weight.");
            System.exit(0);
        }

        else {
            this.name = "No name yet.";
            this.age = 0;
            this.weight = weight;
        }
    }

    public Pet() {
        this.name = "No name yet.";
        this.age = 0;
        this.weight = 0;
    }

    public void set(String name, int age, double weight) {
        if ((age < 0) | (weight < 0)) {
            System.out.println("Error: Negative age or weight.");
            System.exit(0);
        }

        this.name = name;
        this.age = age;
        this.weight = weight;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        if (age < 0) {
            System.out.println("Error: Negative age.");
        }

        else {
            this.age = age;
        }
    }

    public void setWeight(double weight) {
        if (weight < 0) {
            System.out.println("Error: Negative weight.");
        }

        else {
            this.weight = weight;
        }
    }

    public String getName() {
        return this.name;
    }

    public int getAge() {
        return this.age;
    }

    public double getWeight() {
        return this.weight;
    }
}