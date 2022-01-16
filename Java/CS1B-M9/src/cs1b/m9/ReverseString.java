package cs1b.m9;
import java.util.*;
public class ReverseString {
    
    public static boolean PalindromeTest(String normal, String reversed) {
        boolean result = false;
        if (reversed.equals(normal)) {
            result = true;
        }
        return result;
    }
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Please input a string.");
        String value = input.nextLine();
        
        StringBuilder SB = new StringBuilder(value);
        SB.reverse();
        
        System.out.println("Normal string: " + value);
        System.out.println("Reversed string: " + SB);
        System.out.println("Palindrome: " + PalindromeTest(value, SB.toString()));
        
    }
    
}
