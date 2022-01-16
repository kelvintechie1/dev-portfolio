package com.mycompany.module6;
import java.util.*;
public class EvenNumbers {
    public static void main(String[] args) {
        // Create scanner object to read input from user
        Scanner input = new Scanner(System.in);
        // Ask user to input integer number
        System.out.println("Please enter a whole, positive number to display all even numbers from one (1) to that number.");
        Integer number = input.nextInt();
        // Create ArrayList for even numbers
        ArrayList<Integer> EvenNumbers = new ArrayList<>();
        // Use for loop to enumerate all numbers from 1 to that number, check whether they're even, and add to array list if they are
        for (int i = 1; i <= number; i++) {
            if (i % 2 == 0) {
                EvenNumbers.add(i);
            }
        }
        // Print array list
        System.out.println("All of the even numbers from 1 to your specified number (" + Integer.toString(number) + ") are: " + EvenNumbers);
    }
    
}
