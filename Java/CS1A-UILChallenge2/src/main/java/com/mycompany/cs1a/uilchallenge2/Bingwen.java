package com.mycompany.cs1a.uilchallenge2;
import java.util.*;
import java.text.*;
import java.io.*;

public class Bingwen {

    public static void ThirdRoot() throws IOException
    {
        // Create scanner object to read from a file
        Scanner input = new Scanner(new File("bingwen.dat"));
        // Create new DecimalFormat variable
        DecimalFormat rounding = new DecimalFormat("#.00");
        while (input.hasNextDouble()) {
            Double num = 0.0;
            Double inputnum = input.nextDouble();
            if (inputnum <= 2147483647) {
                num = inputnum;
            }
            else {
                System.out.println("Please enter a number that is smaller or equal to 2147483647.");
                break;
            }
            // Perform third root on number
            Double root = 0.0;
            root = Math.cbrt(num);
            // Print third root
            System.out.println(rounding.format(root));
        }
 
        // Ask the user whether they want to continue - meet objective of checking for multiple numbers without using input file
        ContMethod();
    }
    
    public static void ContMethod() throws IOException
    {
        // Create scanner obj to read keyboard input
        Scanner input = new Scanner(System.in);
        // Ask the user whether they want to continue - meet objective of checking for multiple numbers without using input file
        System.out.println("Do you want to test another number? Answer yes or no only.");
        String ans = input.nextLine().toLowerCase();
        if (ans.equals("yes")) {
            ThirdRoot();
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
        ThirdRoot();
    }
    
}
