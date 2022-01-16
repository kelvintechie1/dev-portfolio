package com.mycompany.module5;
import java.util.*;
public class VowelorConsonant {
    public static void main(String[] args) {
        // Create scanner object to read keyboard input
        Scanner input = new Scanner(System.in);
        // Ask for user to enter a letter
        System.out.println("Please enter a letter to determine whether it is a letter or a consonant. Please ONLY input a single letter, any other characters will not be accepted.");
        String inputletter = input.next();
        String validatedletter = inputletter.substring(0,1);
        // Create ArrayList with vowels
        ArrayList<String> Vowels = new ArrayList<String>();
        Vowels.add("a");
        Vowels.add("e");
        Vowels.add("i");
        Vowels.add("o");
        Vowels.add("u");
        // Use if statement to compare letter to ArrayList and print a result accordingly
        if (Vowels.contains(validatedletter.toLowerCase()) == true) {
            System.out.println("This letter (" + validatedletter + ") is a vowel!");
        } else {
            System.out.println("This letter (" + validatedletter + ") is either a consonant or you entered a non-letter character. Please re-enter your value if this is not the desired result.");
        }
    }
    
}
