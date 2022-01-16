package com.mycompany.module4;
import java.util.*;
import java.text.*;
public class TaxRate {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        DecimalFormat format = new DecimalFormat("#.00");
        // Allow user to input base tax rate and store in variable "rate"
        System.out.println("Please enter your base tax rate. Enter in decimal form.");
        double rate = input.nextDouble();
        // Ask user to input gross pay
        System.out.println("What is your gross pay?");
        double gross = input.nextDouble();
        // Do mathematical calculation to figure out net pay
        double netrate = 1 - rate;
        double net = gross * netrate;
        // Return to user
        System.out.println("Your net pay is $" + format.format(net) + ".");
    }
    
}
