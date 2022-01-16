package com.mycompany.module5;
import java.util.*;
public class ContainedinCompSci {
    public static void main(String[] args) {
        // Create new scanner object to read keyboard input
        Scanner input = new Scanner(System.in);
        // Ask for user input to enter the letter that will be the search term
        System.out.println("Please enter a letter to search for its presence in Computer Science. Please only enter a singular letter, no other letters or character types will be accepted.");
        String inputstr = input.next();
        String validatedstr = inputstr.substring(0,1);
        // Search for the letter inside the word "Computer Science"
        String CS = "computer science";
        if (CS.contains(validatedstr.toLowerCase())) {
            System.out.println("The letter you entered (" + validatedstr + ") is present in the word \"Computer Science\"");
        } else {
            System.out.println("The letter you entered (" + validatedstr + ") is either not present in the world \"Computer Science \" or is not a valid letter. Please re-enter your letter if this is not your desired result.");
        }
    }
    
}
