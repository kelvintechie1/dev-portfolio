package cs1b.m10;
import java.util.*;
public class CS1BM10 {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter a positive integer number to determine whether it's prime.");
        int value = input.nextInt();
        int factors = 0;
        // Determine whether number is prime
        for (int i = 1; i <= value; i++) {
            if (value % i == 0) {
                factors++;
            }
        }
        if (factors > 2) {
            System.out.println("Not prime");
        }
        else if (factors == 2) {
            System.out.println("Prime");
        }
        else {
            System.out.println("You entered an invalid number.");
        }
    }
    
}
