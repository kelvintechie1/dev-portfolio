package com.mycompany.cs1a.forloopifstatement;
import java.util.*;
import java.util.regex.*;

public class NumContains1 {

    public static void NumContains1()
    {
        // Create new scanner object
        Scanner input = new Scanner(System.in);
        // Ask user to input strings and store it in integer variable
        System.out.println("Please enter a whole number.");
        Integer n = input.nextInt();
        // Use regex to match on anything that has a 1 in it
        Pattern Match1 = Pattern.compile("1");
        Matcher MatchingOn1 = Match1.matcher(n.toString());
        // Store number of matches in integer called "Matches"
        Integer Matches = (int) MatchingOn1.results().count();
        // Use if/elif statements to check for whether Matches integer is more than 0 or is 0 - if more than 0, has a 1 in it
        if (Matches > 0) {
            System.out.println(true);
        }
        else if (Matches.equals(0)) {
            System.out.println(false);
        }

        // Ask user whether to continue
        ContMethod();
    }
    
    public static void ContMethod() 
    {
        // Create scanner obj to read keyboard input
        Scanner input = new Scanner(System.in);
        // Ask the user whether they want to continue - meet objective of checking for multiple numbers without using input file
        System.out.println("Do you want to check another number? Answer yes or no only.");
        String ans = input.nextLine().toLowerCase();
        if (ans.equals("yes")) {
            NumContains1();
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
        NumContains1();
    }
    
}
