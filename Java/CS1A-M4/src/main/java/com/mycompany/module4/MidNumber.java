package com.mycompany.module4;
import java.util.*;
public class MidNumber {
    public static void main(String[] args) {
        // Create new scanner object to read input from keyboard
        Scanner input = new Scanner(System.in);
        // Request user for input on three numbers and store them in respectively named variables
        System.out.println("Please enter three numbers.");
        double num1 = input.nextDouble();
        double num2 = input.nextDouble();
        double num3 = input.nextDouble();
        // Find the largest of the three numbers - Code used from largest number assignemnt
        double largest_candidate = Math.max(num1, num2);
        double largest = Math.max(largest_candidate, num3);
        // Find the smallest of the three numbers - Code used from smallest number assignment
        double smallest_candidate = Math.min(num1, num2);
        double smallest = Math.min(smallest_candidate, num3);
        // Find the middle of the three numbers and print
        if (num1 != largest && num1 != smallest) {
            System.out.println("The middle number is " + num1);
        } else if (num2 != largest && num2 != smallest) {
            System.out.println("The middle number is " + num2);
        } else if (num3 != largest && num3 != smallest) {
            System.out.println("The middle number is " + num3);
        }
    }
}
