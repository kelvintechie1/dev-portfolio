package com.mycompany.module4;
import java.util.*;
public class ConvertNumber {
    public static void main(String[] args) {
        // Create scanner object to read keyboard input
        Scanner input = new Scanner(System.in);
        // Ask user to input radius
        System.out.println("Please enter the radius of the circle.");
        Double rad = input.nextDouble();
        // Calculate area of circle
        Double area = (Math.pow(rad, 2) * Math.PI);
        // Print area of the circle to user
        System.out.println("The area of the requested circle is " + Double.toString(area) + ".");
    }
}
