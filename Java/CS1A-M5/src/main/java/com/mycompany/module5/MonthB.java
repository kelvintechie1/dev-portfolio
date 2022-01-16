package com.mycompany.module5;
import java.util.*;
public class MonthB {
    public static void main(String[] args) {
        // Create scanner object to read keyboard input
        Scanner input = new Scanner(System.in);
        // Asks user for month in word form
        System.out.println("Enter a month in word form, with the first letter being capitalized.");
        String monthStr = input.next();
        // Create new dictionary and populate with month/number associations
        Hashtable<String, String> months = new Hashtable<String, String>();
        int counter = 1; // Use to put value with months
        months.put("January", Integer.toString(counter++));
        months.put("February", Integer.toString(counter++));
        months.put("March", Integer.toString(counter++));
        months.put("April", Integer.toString(counter++));
        months.put("May", Integer.toString(counter++));
        months.put("June", Integer.toString(counter++));
        months.put("July", Integer.toString(counter++));
        months.put("August", Integer.toString(counter++));
        months.put("September", Integer.toString(counter++));
        months.put("October", Integer.toString(counter++));
        months.put("November", Integer.toString(counter++));
        months.put("December", Integer.toString(counter++));
        // Check for validity of month and act accordingly - print or prompt user to re-enter the month.
        if (months.get(monthStr) != null) {
            System.out.println("The numerical form of the month you entered (" + monthStr + ") is " + months.get(monthStr) + ".");
        } else {
            System.out.println("Please re-run the program and enter a valid month, with the first letter being capitalized.");
            // Program could be improved by defining the input code as a function and calling back to the function in this space of the else statement.
        }
    }
}
