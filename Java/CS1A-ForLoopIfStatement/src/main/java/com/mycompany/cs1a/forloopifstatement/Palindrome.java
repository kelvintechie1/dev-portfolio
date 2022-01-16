package com.mycompany.cs1a.forloopifstatement;
import java.util.*;
import java.lang.*;

public class Palindrome {

    public static void Palindrome()
    {
        // Create new scanner object
        Scanner input = new Scanner(System.in);
        // Ask user to input string and store it in a string
        System.out.println("Please enter a sentence to determine whether the string is a palindrome (something that, if reversed, will be spelled the same way as it was spelled forward.");
        String original = (input.nextLine()).toLowerCase();
        // Remove spaces
        String answer = original.replaceAll("\\s", "");
        // Use StringBuilder to reverse string
        StringBuilder reverse = new StringBuilder(answer);
        reverse.reverse();
        Boolean palindrome = false;
        if (reverse.toString().equals(answer)) {
            palindrome = true;
        }
        // Print output
        if (palindrome == true) {
            System.out.println("The string you provided (\"" + original + "\") is a palindrome.");
        }
        else {
            System.out.println("The string you provided (\"" + original + "\") is NOT a palindrome.");
        }
        // Ask user whether to continue
        ContMethod();
    }
    
    public static void ContMethod() 
    {
        // Create scanner obj to read keyboard input
        Scanner input = new Scanner(System.in);
        // Ask the user whether they want to continue - meet objective of checking for multiple numbers without using input file
        System.out.println("Do you want to check another string? Answer yes or no only.");
        String ans = input.nextLine().toLowerCase();
        if (ans.equals("yes")) {
            Palindrome();
        }
        else if (ans.equals("no")) {
            System.out.println("Thank you! Have a great day!");
        }
        else {
            System.out.println("Please enter a valid response of yes or no.");
            ContMethod();
        }
    }

    public static void main(String[] args) {
        Palindrome();
    }
    
}