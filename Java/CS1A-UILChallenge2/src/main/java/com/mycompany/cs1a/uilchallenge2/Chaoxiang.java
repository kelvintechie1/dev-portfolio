package com.mycompany.cs1a.uilchallenge2;
import java.util.*;
import java.text.*;
import java.io.*;

public class Chaoxiang {
    
    public static void TempConversion() throws IOException
    {
        // Create scanner obj to read from file
        Scanner input = new Scanner(new File("chaoxiang.dat"));
        // Create DecimalFormat object to round number
        DecimalFormat rounding = new DecimalFormat("#.00");
        
        while (input.hasNextDouble()) {
            Double inputTemp = input.nextDouble();
            // Convert temperature to Kelvin
            Double fiveninths = (double) 5/9;
            Double KelvinTemp = (inputTemp - 32) * fiveninths + 273.16;
            // Print output
            if (rounding.format(KelvinTemp).equals(".00")) {
                System.out.println("0.00");
            }
            else {
                System.out.println(rounding.format(KelvinTemp));                       
            }
        }

        // Ask the user whether they want to continue - meet objective of checking for multiple numbers without using input file
        ContMethod();
    }
    
    public static void ContMethod() throws IOException
    {
        // Create scanner obj to read keyboard input
        Scanner input = new Scanner(System.in);
        // Ask the user whether they want to continue - meet objective of checking for multiple numbers without using input file
        System.out.println("Do you want to convert another Fahrenheit value to Kelvin? Answer yes or no only.");
        String ans = input.nextLine().toLowerCase();
        if (ans.equals("yes")) {
            TempConversion();
        }
        else if (ans.equals("no")) {
            System.out.println("Thank you! Have a great day!");
        }
        else {
            System.out.println("Please enter a valid response of yes or no.");
            ContMethod();
        }
    }

    public static void main(String[] args) throws IOException {
        TempConversion();
    }
    
}
