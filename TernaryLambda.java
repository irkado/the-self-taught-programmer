
import java.util.Scanner;
import java.util.function.Function;

public class TernaryLambda {

    /* Lambda with interface :) */
    @FunctionalInterface
    public static interface Check {

        public String apply(int num);
    }
    /* */

    public static void main(String[] args) {

        try (Scanner in = new Scanner(System.in)) {
            int number = in.nextInt();

            /* Lambda with interface :) */
            // Check checkEvenOdd = num -> (num % 2 == 0) ? "Even" : "Odd";
            /* */

            /* Lambda with util.func */
            Function<Integer, String> checkEvenOdd = num -> (num % 2 == 0) ? "Even" : "Odd";
            /* */

            System.out.println("\n4 - " + checkEvenOdd.apply(4));  // Output: Even
            System.out.println("5 - " + checkEvenOdd.apply(5));  // Output: Odd
            System.out.println(number + " - " + checkEvenOdd.apply(number));
        }

    }
}
