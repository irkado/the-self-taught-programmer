
import java.util.function.Function;

public class TernaryLambdaExample {

    // @FunctionalInterface
    // public static interface Checks {
    //     public String apply(int num);
        
    // }
    // @FunctionalInterface
    // public interface Get {
    //     public String get(int num);
    // }

    public static void main(String[] args) {
        // Checks checkEvenOdd = num -> (num % 2 == 0) ? "Even" : "Odd";

        Function<Integer, Integer> checkEvenOdd = num -> (num % 2 == 0) ? 0 : 1;

        System.out.println(checkEvenOdd.apply(4));  // Output: Even
        System.out.println(checkEvenOdd.apply(5));  // Output: Odd
    }
}
