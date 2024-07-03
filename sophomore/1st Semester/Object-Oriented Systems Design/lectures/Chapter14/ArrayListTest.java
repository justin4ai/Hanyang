import java.util.ArrayList;

public class ArrayListTest {
    public static void main(String[] args) {
        ArrayList<String> aList = new ArrayList<String>(20); // Default capacity : 10 / Don't be confused with capacity and size

        aList.add("one"); // return type : boolean
        aList.add("two");
        aList.add("three");
        aList.add("four");
        aList.add("five");
        aList.add("six");
        System.out.println(aList.size());
        System.out.println(aList);

        aList.add(0, "zero"); // return type : void
        System.out.println(aList.size());
        System.out.println(aList);

        //aList.add(8, "eight"); // Error - only possible from 0 to the size of the array
        //System.out.println(aList);

        aList.set(0, "ZERO");
        System.out.println(aList.size());
        System.out.println(aList);

        //aList.set(7, "eight"); // Error - only possible from 0 to the maximum index
        //System.out.println(aList);
    
        
        System.out.println(aList.get(0));
        aList.remove(1); // return type : base_type which is removed ) - for this case, one
        System.out.println(aList.size());
        System.out.println(aList);
        aList.remove("ZERO"); // If multiple elements -> remove leftmost one
        System.out.println(aList.size());
        System.out.println(aList);


        if (aList.contains("ZERO"))
            System.out.println("aList contians ZERO");
        

        System.out.println("The first index of ZERO is " + aList.indexOf("ZERO"));
        System.out.println("The last index of ZERO is " + aList.lastIndexOf("ZERO")); // Both return -1 if not found

        // aList.clear();
        // System.out.println(aList.size());
        // System.out.println(aList);

        System.out.println(aList.isEmpty());

        for (String element: aList) {
            System.out.println(element);
        }


    }

}