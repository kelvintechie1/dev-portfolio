package com.mycompany.module5;
import java.util.*;
public class CompareNumto100 {
    public static void main(String[] args) {
        // Create new scanner object to read keyboard input from user
        Scanner input = new Scanner(System.in);
        // Read user input to determine what the desired number is
        System.out.println("Please enter a number to determine whether it is greater than, less than, or equal to 100.");
        Double num = input.nextDouble();
        // Use if statements to find how the number compares to 100
        if (num == 100) {
            System.out.println("The number you entered (" + Double.toString(num) + ") is equal to 100.");
        } else if (num > 100) {
            System.out.println("The number you entered (" + Double.toString(num) + ") is greater than 100.");
        } else if (num < 100) {
            System.out.println("The number you entered (" + Double.toString(num) + ") is less than 100.");
        } else {
            System.out.println("Please enter a valid number for comparison.");
        }
    }
    
}
