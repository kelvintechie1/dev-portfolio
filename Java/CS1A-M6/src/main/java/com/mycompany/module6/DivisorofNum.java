package com.mycompany.module6;
import java.util.*;
public class DivisorofNum {
    public static void main(String[] args) {
        // Create scanner object to read user input
        Scanner input = new Scanner(System.in);
        // Ask user to enter number to determine divisors of
        System.out.println("Please enter a whole number to determine the divisors of.");
        Integer num = input.nextInt();
        // Create ArrayList to contain divisors
        ArrayList<Integer> divisors = new ArrayList<>();
        // Use for loop to enumerate divisors and check whether they are divisors
        for (Integer i = 1; i <= num; i++) {
            if (num % i == 0) {
                divisors.add(i);
            }
        }
        // Print ArrayList of divisors
        System.out.println("The divisors of your specified number (" + Integer.toString(num) + ") are as follows: " + divisors);
    }
    
}
