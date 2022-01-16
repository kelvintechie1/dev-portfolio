package com.mycompany.cs1a.forloopifstatement;
import java.util.*;
import java.util.regex.*;

public class CountBob {

    public static void BobLogic()
    {
        // Create new scanner object
        Scanner input = new Scanner(System.in);
        // Ask user to input string and store it in a string
        System.out.println("Please enter a sentence to detect whether the given sentence contains any instance of \"bxb\", where x can be any character, including a space.");
        String answer = (input.nextLine()).toLowerCase();
        // Match string against regex to find any occurrence of a pattern where b is optionally followed by a range of a-z and immediately followed again by a b
        Pattern regexp = Pattern.compile("b?.b");    
        Matcher matching = regexp.matcher(answer);
        Integer matches = (int) matching.results().count();
        // Print result
        System.out.println("The string you provided (\"" + answer + "\") has " + matches.toString() + " occurrences of the pattern bxb, where x can be any character, including a space.");
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
            BobLogic();
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
        BobLogic();
    }
    
}
