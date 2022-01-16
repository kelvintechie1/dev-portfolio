package com.mycompany.cs1a.forloopifstatement;
import java.util.*;
import java.text.*;

public class CountVowels {

    public static void CountVowels() {
        // Create scanner object to read keyboard input
        Scanner input = new Scanner(System.in);
        // Ask user to provide a string
        System.out.println("Please provide a word, phrase, or sentence to calculate how many vowels are in it.");
        String answer = input.nextLine().toLowerCase();
        // Declare variables
        Integer vowelNum = 0;
        Integer length = 0;
        ArrayList<Character> vowels = new ArrayList<>();
        // Assign values to variables
        length = answer.length();
        vowels.add('a');
        vowels.add('e');
        vowels.add('i');
        vowels.add('o');
        vowels.add('u');
        // Go through for loop to search for variables
        for (Integer i = 0; i <= (length - 1); i++) {
            if (vowels.contains(answer.charAt(i))) {
                vowelNum = vowelNum + 1;
            }
        }
        // Print output
        System.out.println("The string you provided (\"" + answer + "\") has " + vowelNum.toString() + " vowels in it.");
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
            CountVowels();
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
        CountVowels();
    }
    
}
