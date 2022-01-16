package com.mycompany.module4;
import java.util.*;
public class Quadratic {
    public static void main(String[] args) {
        // Create new scanner object to read input from keyboard
        Scanner input = new Scanner(System.in);
        // Request a, b, and c from user and store them in variables (doubles)
        System.out.println("Please enter \"a\" to be used in the quadratic formula.");
        Double a = input.nextDouble();
        System.out.println("Please enter \"b\" to be used in the quadratic formula.");
        Double b = input.nextDouble();
        System.out.println("Please enter \"c\" to be used in the quadratic formula.");
        Double c = input.nextDouble();
        // Perform quadratic formula calculation, accounting for the plus or minus
        Double x_positive = ((-1)*b + Math.sqrt(Math.pow(b, 2) - 4*a*c)) / 2*a;
        Double x_negative = ((-1)*b - Math.sqrt(Math.pow(b, 2) - 4*a*c)) / 2*a;
        // Print values
        System.out.println("The result of the quadratic formula if the square root expression is added is " + Double.toString(x_positive) + " and the result of the quadratic formula if the square root expression is subtracted is " + Double.toString(x_negative) + ".");
    }
}
