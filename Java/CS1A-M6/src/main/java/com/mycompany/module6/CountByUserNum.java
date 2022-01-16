package com.mycompany.module6;
import java.util.*;
import java.text.*;
public class CountByUserNum {
    public static void main(String[] args) {
        // Create scanner object to read user input
        Scanner input = new Scanner(System.in);
        // Create decimalFormat object to use in formatting number
        DecimalFormat TwoDecimalPlaces = new DecimalFormat("#.00");
        // Ask user to input number to increment by
        System.out.println("Please enter a number to increment by when counting from 1 to 100.");
        Double increment = input.nextDouble();
        // Create an array list to contain counted numbers
        ArrayList<String> countedNum = new ArrayList<>();
        // Use a for loop to count through numbers and add to array list
        for (double i = 1; i <=100; i = i + increment) {
            String formattedi = TwoDecimalPlaces.format(i);
            countedNum.add(formattedi);
        }
        // Print array list
        System.out.println("Incrementing by your specified number (" + Double.toString(increment) + ") when counting from 1 to a maximum of 100, the list is as follows: " + countedNum);
    }
    
}
