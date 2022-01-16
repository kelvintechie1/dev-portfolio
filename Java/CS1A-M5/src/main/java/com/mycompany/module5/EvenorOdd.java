package com.mycompany.module5;
import java.util.*;
public class EvenorOdd {
    public static void main(String[] args) {
        // Create new scanner object to read keyboard input from user
        Scanner input = new Scanner(System.in);
        // Read user input to determine what the desired number is
        System.out.println("Please enter a whole number to determine whether it is even or odd.");
        Integer num = input.nextInt();
        // Determine modulo of the number
        Integer mod_num = num % 2;
        // Print statement accordingly depending on whether modulo returns 0 or any other number
        if (mod_num == 0) {
            System.out.println("The number you entered (" + Integer.toString(num) + ") is even.");
        } else if (mod_num != 0) {
            System.out.println("The number you entered (" + Integer.toString(num) + ") is odd.");
        } else {
            System.out.println("Please enter a valid number.");
        }
    }
    
}
