package cs1b.m10;
import java.util.*;
public class Factorial {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the number to find the factorial of.");
        int number = input.nextInt();
        long result = number * (number - 1);
        for (int i = (number - 2); i >= 1; i--) {
            result = result * i;
        }
        System.out.println("The factorial result is: " + result);
    }
    
}
