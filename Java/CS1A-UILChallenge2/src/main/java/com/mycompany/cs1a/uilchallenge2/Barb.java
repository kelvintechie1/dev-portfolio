package com.mycompany.cs1a.uilchallenge2;

import java.util.*;
import java.lang.*;
import java.io.*;

public class Barb {
    
    public static void Word() throws IOException
    {
        // Create Scanner object to look for file
        Scanner input = new Scanner(new File("barb.dat"));
        while (input.hasNextLine()) {
            String word = "";
            word = input.nextLine();
            // Find out how many characters are in the word
            Integer len = word.length();
            Double halfLen = (Double.valueOf(len) / 2);
            long roundedlong = Math.round(halfLen);
            int rounded = (int) roundedlong;
            // Find first half of the word
            String FH = "";  
            for (Integer FHi = 0; FHi<=(rounded - 1); FHi++) { // Do "rounded - 1" to ensure that it doesn't accidentally count an extra character, since it needs to start at 0   
                FH = (FH + word.charAt(FHi));
            }
            // Find last half of the word
            Integer initialLHi = (len - rounded);
            String LH = "";            
            for (Integer LHi = initialLHi; LHi<=(initialLHi + (rounded - 1)); LHi++) {
                LH = (LH + word.charAt(LHi));
            }
            // Manipulate word using StringBuilder - Reverse, Whole Word
            StringBuilder SBReverse = new StringBuilder(word);            
            SBReverse.reverse();
            // Manipulate word using StringBuilder - Reverse, first half of the word
            StringBuilder SBFH = new StringBuilder(FH);            
            SBFH.reverse();
            // Second half of the word only needs to be capitalized - will be done on the fly in the println statement
            // Print output
            System.out.println(word + " " + (SBReverse.toString()).toUpperCase() + " " + SBFH.toString() + " " + LH.toUpperCase());
        }
        
        // Ask whether user wants to repeat
        ContMethod();
    }
    
    public static void ContMethod() throws IOException
    {
        // Create new scanner object
        Scanner input = new Scanner(System.in);
        // Ask whether user wants to repeat and store in cont string
        System.out.println("Do you wish to continue with another file? Answer yes or no.");
        String cont = input.nextLine();
        // Act appropriately depending on user response
        if ((cont.toLowerCase()).equals("yes")) {
            Word();
        }
        else if ((cont.toLowerCase()).equals("no")) {
            System.out.println("Thank you! Have a good day.");
        }
        else {
            System.out.println("Please provide an answer of yes or no (exact spelling).");
            ContMethod();
        }
    }
    
    public static void main(String[] args) throws IOException {
        Word();
    }
    
}
