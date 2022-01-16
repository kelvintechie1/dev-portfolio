package com.mycompany.module5;
import java.util.*;
import java.text.*;
public class PayRate {
    public static void main(String[] args) {
        // Create new scanner object to read keyboard input
        Scanner input = new Scanner(System.in);
        // Create new DecimalFormat to format for currency and money
        DecimalFormat Money = new DecimalFormat("#.00");
        // Ask user for total number of hours and hourly rate of pay
        System.out.println("Enter your total number of hours worked this week:");
        Integer Hours = input.nextInt();
        System.out.println("Enter your hourly rate of pay (without the currency sign):");
        Double Pay = input.nextDouble();
        // Run conditional if statement to find whether overtime hours is needed and print to user
        if (Hours > 40) {
            Integer OTHours = Hours - 40;
            Double StdPay = Pay * 40;
            Double OTPay = 1.5 * Pay * OTHours;
            System.out.println("The total amount earned before taxes is $" + Money.format(StdPay + OTPay) + ".");
        } else if (Hours < 40) {
            Double StdPay = Pay * Hours;
            System.out.println("The total amount earned before taxes is $" + Money.format(StdPay) + ".");
        } else {
            System.out.println("Please enter a valid number of hours.");
        }
    }
    
}
