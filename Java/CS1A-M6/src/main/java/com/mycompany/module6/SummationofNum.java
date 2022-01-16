package com.mycompany.module6;
import java.util.*;
public class SummationofNum {
    public static void main(String[] args) {
        // Create scanner objec to read user input
        Scanner input = new Scanner(System.in);
        // Ask user for number
        System.out.println("Please enter a WHOLE number to display the whole number summation from 1 to that number.");
        Integer userNum = input.nextInt();
        // Create integer variable to store the summation
        Integer summation = 0;
        // Use for loop to enumerate all whole numbers from 1 to the user specified number and add it to the value of the summation variable.
        for (Integer i = 1; i <= userNum; i++) {
            summation = summation + i;
        }
        // Print the value of the summation variable
        System.out.println("The whole numer summation from 1 to your specified number (" + Integer.toString(userNum) + ") is " + Integer.toString(summation) + ".");
    }
    
}
