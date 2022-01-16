package com.mycompany.module6;
import java.util.*;
public class PrimeNumBonus {
    public static void main(String[] args) {
        // Create scanner object to read user input
        Scanner input = new Scanner(System.in);
        // Ask user to enter number to determine prime status
        System.out.println("Please enter a whole number to determine whether it is prime or non-prime.");
        Integer num = input.nextInt();
        // Create ArrayList to contain divisors
        ArrayList<Integer> divisors = new ArrayList<>();
        // Use for loop to enumerate divisors and check whether they are divisors
        for (Integer i = 1; i <= num; i++) {
            if (num % i == 0) {
                divisors.add(i);
            }
        }
        // Check ArrayList length
        Integer length = divisors.size();
        // Print whether number is prime or not by using conditional if statement
        if (length == 2) {
            System.out.println("Your specified number (" + Integer.toString(num) + ") is prime.");
        } else {
            System.out.println("Your specified number (" + Integer.toString(num) + ") is not prime. Its divisors are as follows: " + divisors + ".");
        }
    }
    
}