package com.mycompany.module4;
import java.util.Scanner;
public class SmallestNumber {
    public static void main(String[] args) {
        // Create new scanner object to read input from keyboard
        Scanner input = new Scanner(System.in);
        // Request user for input on three numbers and store them in respectively named variables
        System.out.println("Please enter three numbers.");
        double num1 = input.nextDouble();
        double num2 = input.nextDouble();
        double num3 = input.nextDouble();
        // Find the smallest of the three numbers
        double smallest_candidate = Math.min(num1, num2);
        double smallest = Math.min(smallest_candidate, num3);
        // Convert to integer before converting it to string to eliminate decimal point
        System.out.println("The smallest number is " + Double.toString(smallest));
    }
}
