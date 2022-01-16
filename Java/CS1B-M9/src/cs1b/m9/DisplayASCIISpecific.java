package cs1b.m9;
import java.util.*;
public class DisplayASCIISpecific {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Please enter an integer base 10 (decimal) value.");
        int value = input.nextInt();
        System.out.println(("ASCII Symbol: " + (char) value) + " " +
                ("Decimal number: " + value) + " " +
                ("Binary: " + Integer.toBinaryString(value)) + " " +
                ("Hex Number: " + Integer.toHexString(value)) + " " +
                ("Octal Number: " + Integer.toOctalString(value)));
    }
    
}
