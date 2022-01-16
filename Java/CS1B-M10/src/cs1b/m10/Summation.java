package cs1b.m10;
import java.util.*;
public class Summation {
    
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the maximum number of the summation series to sum the squares of all numbers from 1 to that point.");
        int number = input.nextInt();
        double result = 0.0;
        for (int i = 1; i <= number; i++) {
            result = result + Math.pow(i,2);
        }
        System.out.println("The summation result is: " + result);
    }
    
}
