package com.mycompany.cs1a.forloopifstatement;
import java.util.*;

public class MakeFunnyWord {

    public static void FunnyWord()
    {
        // Create new scanner object
        Scanner input = new Scanner(System.in);
        // Ask user to input strings and store it in string variables
        System.out.println("Please enter a word.");
        String string1 = input.nextLine();
        System.out.println("Please enter another word.");
        String string2 = input.nextLine();
        // Declare variables
        String ModifiedString1 = "";
        String ModifiedString2 = "";
        String Final = "";
        Integer len1 = string1.length();
        Integer len2 = string2.length();
        // Find out which one is longer and go into the appropriate for loop
        if (len1 > len2) {
            for (int i = 0; i <= (len2 - 1); i++) {
                Final = Final + string1.charAt(i);
                Final = Final + string2.charAt(i);
            }
            for (int x = (len1 - (len1 - len2)); x <= (len1 - 1); x++) { 
            // First for loop will add to the final string the same amount of characters in the larger string as there are characters in the smaller string
            // therefore, we need to use len1 - len2 to find how many characters are left and then subtract that difference from the length of the longer string to find the starting position for the second for loop
                Final = Final + string1.charAt(x);
            }
        }
        
        else if (len2 > len1) {
            for (int i = 0; i <= (len1 - 1); i++) {
                Final = Final + string1.charAt(i);
                Final = Final + string2.charAt(i);
            }
            for (int x = (len2 - (len2 - len1)); x <= (len2 - 1); x++) {
                // see above comment for reason why the logic is written like this
                Final = Final + string1.charAt(x);
            }
        }
        
        else if (len1.equals(len2)) {
            for (int i = 0; i <= (len1 - 1); i++) {
                Final = Final + string1.charAt(i);
                Final = Final + string2.charAt(i);
            }         
        }
        // Output to user the final funny word
        System.out.println("Your funny word is: " + Final);
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
            FunnyWord();
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
        FunnyWord();
    }
    
}
