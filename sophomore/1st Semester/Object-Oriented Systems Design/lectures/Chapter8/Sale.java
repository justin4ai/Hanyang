public class Sale {

    private String name;
    private double price;

    public Sale() {
        name = "No name yet";
        price = 0;
    }

    public Sale(String theName, double thePrice) {
        setName(theName);
        setPrice(thePrice);
    }

    public Sale(Sale originalObject) {
        if (originalObject == null) {
            System.out.println("Error: null Sale object.");
            System.exit(0);
        }

        name = originalObject.name;
        price = originalObject.price;
    }

    public Sale clone() {
        return new Sale(this); // only if Sale class has a copy constructor
                               // if not overriden, return Object type -> if not overriden, Sale x = originalSale.clone() errors even originalSale is Sale class
    }

    public static void announcement() {
        System.out.println("This is the Sale class.");

    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double newPrice) {
        if (newPrice >= 0) {
            price = newPrice;
        }

        else {
            System.out.println("Error: Negative price.");
            System.exit(0);
        }
    }

    public String getName() {
        return name;
    }

    public void setName(String newName) {
        if (newName != null && newName != "") {
            name = newName;
        }

        else {
            System.out.println("Error: Improper name value.");
            System.exit(0);
        }
    } 

    public String toString() {
        return (name + " Price and total cost = $" + price);
    }

    public double bill() {
        return price;
    }

    public boolean equalDeals(Sale otherSale) {
        if (otherSale == null) {
            return false;
        }

        else {
            return (name.equals(otherSale.name) && bill() == otherSale.bill());
        }
    }

    public boolean lessThan (Sale otherSale) {
        if (otherSale == null) {
            System.out.println("Error: null Sale object.");
            System.exit(0);
            return false;
        }

        else {
            return (bill() < otherSale.bill()); // Late Binding : .bill() of Sale class or DiscountSale class?]
                                                // Determined during runtime
        }
    }

    public boolean equals(Object otherObject) { // Hard to understand
        if (otherObject == null) {
            return false;
        }

        else if (getClass() != otherObject.getClass()) {
            return false;
        }

        else {
            Sale otherSale = (Sale) otherObject; // Downcasting - Object class has no instance variables name and price
            return (name.equals(otherSale.name) && (price == otherSale.price));
        }
    }
}