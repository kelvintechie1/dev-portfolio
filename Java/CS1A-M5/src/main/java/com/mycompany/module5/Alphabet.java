package com.mycompany.module5;
import java.util.*;
public class Alphabet {
    public static void main(String[] args) {
        // Create new scanner object to read keyboard input
        Scanner input = new Scanner(System.in);
        // Ask for user input to enter the letter that will be the search term
        System.out.println("Enter a letter in the American English alphabet to see what it stands for!");
        String inputletter = input.next();
        String validatedletter = inputletter.substring(0,1);
        // Create dictionary containing letter to word pairings
        Hashtable<String, String> words = new Hashtable<String, String>();
        // Add words to dictionary
        words.put("a", "apple");
        words.put("b", "banana");
        words.put("c", "computer");
        words.put("d", "dog");
        words.put("e", "east");
        words.put("f", "fountain");
        words.put("g", "girl");
        words.put("h", "hype");
        words.put("i", "instant");
        words.put("j", "jest");
        words.put("k", "kelp");
        words.put("l", "listen");
        words.put("m", "magician");
        words.put("n", "never");
        words.put("o", "opera");
        words.put("p", "passionfruit");
        words.put("q", "quirk");
        words.put("r", "rascal");
        words.put("s", "smirk");
        words.put("t", "top");
        words.put("u", "unicorn");
        words.put("v", "very");
        words.put("w", "watch");
        words.put("x", "xylophone");
        words.put("y", "yell");
        words.put("z", "zebra");
        // Check whether letter is present in dictionary and act accordingly
        if (words.get(validatedletter.toLowerCase()) != null) {
            System.out.println("It's the letter " + validatedletter + ", as in " + words.get(validatedletter.toLowerCase()) + "!");
        } else {
            System.out.println("Please enter a letter of the American English alphabet.");
        }
    }
    
}
