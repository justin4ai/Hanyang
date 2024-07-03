public class InvocationCounter {
    private static int numberOfInvocations = 0;

    public void demoMethod() {
        numberOfInvocations++;
    }

    public void outputCount() {
        numberOfInvocations++;
        System.out.println("Number of invocations so far = " + numberOfInvocations);
    }

    public static int numberSoFar() {
        numberOfInvocations++;
        return numberOfInvocations;
    }

    public static void main(String[] args) {
        InvocationCounter object1 = new InvocationCounter();
        InvocationCounter object2 = new InvocationCounter();

        for (int i = 1; i <= 5; i++) {
            object1.demoMethod();
        }
        object1.outputCount();



        for (int i = 1; i <= 5; i++) {
            object2.demoMethod();
            object2.outputCount();
        }

        System.out.println("Total numbe of invocations = " + numberSoFar());
    }
}
