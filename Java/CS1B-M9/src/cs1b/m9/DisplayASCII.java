package cs1b.m9;
import java.util.*;
public class DisplayASCII {
    public static void main(String[] args) {
        for (int i = 1; i <= 255; i++) {
            System.out.println(("ASCII Symbol: " + (char) i) + " " +
                    ("Decimal number: " + i) + " " +
                    ("Binary: " + Integer.toBinaryString(i)) + " " +
                    ("Hex Number: " + Integer.toHexString(i)) + " " +
                    ("Octal Number: " + Integer.toOctalString(i)));
        }
    }
    
}
