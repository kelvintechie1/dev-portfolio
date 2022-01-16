package com.mycompany.module4;
import java.util.*;
public class LargestNumber {
    public static void main(String[] args) {
        // Create new scanner object to read input from keyboard
        Scanner input = new Scanner(System.in);
        // Request user for input on three numbers and store them in respectively named variables
        System.out.println("Please enter three numbers.");
        double num1 = input.nextDouble();
        double num2 = input.nextDouble();
        double num3 = input.nextDouble();
        // Find the largest of the three numbers
        double largest_candidate = Math.max(num1, num2);
        double largest = Math.max(largest_candidate, num3);
        // Convert to integer before converting it to string to eliminate decimal point
        System.out.println("The largest number is " + Double.toString(largest));
    }
}