package com.mycompany.module5;
import java.util.*;
public class WordFormofNumber {
    public static void main(String[] args) {
        // Create new scanner object to read keyboard input from user
        Scanner input = new Scanner(System.in);
        // Read user input to determine what the desired number is
        System.out.println("Please enter a whole number from 1 to 10 to receive its word form: ");
        Integer num1 = input.nextInt();
        // Create dictionary to store number to words association
        Hashtable<Integer, String> Words = new Hashtable<Integer, String>();
        // Store number to words association
        Integer number = 1;
        Words.put(number++, "one");
        Words.put(number++, "two");
        Words.put(number++, "three");
        Words.put(number++, "four");
        Words.put(number++, "five");
        Words.put(number++, "six");
        Words.put(number++, "seven");
        Words.put(number++, "eight");
        Words.put(number++, "nine");
        Words.put(number++, "ten");
        // Use if statement to determine validity of number in range and print
        if (num1 >= 1 && num1 <= 10) {
            System.out.println("The word form for the number you entered (" + Integer.toString(num1) + ") is " + Words.get(num1) + ".");
        } else {
            System.out.println("Please enter a valid positive whole number in the range of 1-10.");
        }
    }
    
}
