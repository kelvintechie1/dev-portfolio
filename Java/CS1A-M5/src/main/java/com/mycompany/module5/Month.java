package com.mycompany.module5;
import java.util.*;
public class Month {
    public static void main(String[] args) {
        // Create scanner object to read keyboard input
        Scanner input = new Scanner(System.in);
        // Asks user for month in word form
        System.out.println("Enter a month in numerical form.");
        Integer monthInt = input.nextInt();
        // Create new dictionary and populate with month/number associations
        Hashtable<Integer, String> months = new Hashtable<Integer, String>();
        Integer counter = 1; // Use to put value with months
        months.put(counter++, "January");
        months.put(counter++, "February");
        months.put(counter++, "March");
        months.put(counter++, "April");
        months.put(counter++, "May");
        months.put(counter++, "June");
        months.put(counter++, "July");
        months.put(counter++, "August");
        months.put(counter++, "September");
        months.put(counter++, "October");
        months.put(counter++, "November");
        months.put(counter++, "December");
        // Check for validity of month and act accordingly - print or prompt user to re-enter the month.
        if (months.get(monthInt) != null) {
            System.out.println("The word form of the month you entered (" + monthInt + ") is " + months.get(monthInt) + ".");
        } else {
            System.out.println("Please re-run the program and enter a valid month number.");
            // Program could be improved by defining the input code as a function and calling back to the function in this space of the else statement.
    }
    
}
}
