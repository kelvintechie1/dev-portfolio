package com.mycompany.module5;
import java.util.*;
public class CompareSize {
    public static void main(String[] args) {
        // Create new scanner object to read keyboard input from user
        Scanner input = new Scanner(System.in);
        // Read user input to determine what the desired numbers are
        System.out.println("Please enter two numbers to determine which is larger.");
        Double num1 = input.nextDouble();
        Double num2 = input.nextDouble();
        // Use if statement to determine which is larger
        if (num1 > num2) {
            System.out.println("Number 1 (" + Double.toString(num1) + ") is larger than Number 2 (" + Double.toString(num2) + ").");
        } else if (num1 < num2) {
            System.out.println("Number 1 (" + Double.toString(num1) + ") is smaller than Number 2 (" + Double.toString(num2) + ").");
        } else if (num1 == num2) {
            System.out.println("Number 1 (" + Double.toString(num1) + ") is equal to Number 2 (" + Double.toString(num2) + ").");
        } else {
            System.out.println("Please enter a valid set of two numbers for comparison.");
        }
    }
    
}
