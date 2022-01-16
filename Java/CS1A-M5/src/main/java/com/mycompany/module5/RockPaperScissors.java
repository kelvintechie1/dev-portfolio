package com.mycompany.module5;
import static java.lang.System.in;
import java.util.Scanner;
public class RockPaperScissors {
    public static void Continue() {
        // Continue() - ask user whether they want to continue playing
        // Create scanner object to read user input
        Scanner prompt = new Scanner(in);
        // Ask user whether they want to continue playing
        System.out.println("Do you want to play Rock, Paper, Scissors? Please enter yes or no.");
        String YesNo = prompt.nextLine();
        String YesNo_Lower = YesNo.toLowerCase(); // Change text to all lower case for text processing
        // Use if statements to call Rock Paper Scissors (RPS) function if user says "yes" and exit if "no"
        if (YesNo_Lower.equals("yes")) {
            System.out.println("Great!");
            RPS();
        } else if (YesNo_Lower.equals("no")) {
            System.out.println("Thanks for playing!");
            System.exit(0);
        } else { // Recall Continue function if response is invalid
            System.out.println("Please enter a valid response of \"yes\" or \"no\".");
            Continue();
        }
    }
    public static void RPS()
    {
        // Credit for code - provided in classroom instruction
        // Create scanner object to read user input
        Scanner input = new Scanner(in);
        // Ask user to provide input of rock, paper, or scissors and change choice to uppercase
        System.out.println("Enter Rock, paper, or scissors.");
        String choice = input.nextLine();
        choice = choice.toUpperCase();
        
        int CPU = (int)(Math.random()*3);  // have computer generate random number from 0-2 corresponding to computer's pick
        
        // If statements with unique print statements for computer's choices if user chose rock
        if(choice.contains("RO") && CPU == 0) {
            System.out.println("Draw, you both choose rock");
        } else if(choice.contains("RO") && CPU == 1) {
            System.out.println("You lose, you choose rock Computer choose paper");
        } else if(choice.contains("RO") && CPU == 2) {
            System.out.println("You Win, you choose rock Computer choose Scissors");
        }
        // If statements with unique print statements for computer's choices if user chose paper
        if (choice.contains("PA") && CPU == 0) {
            System.out.println("You win, the computer chose rock and you chose paper.");
        } else if (choice.contains("PA") && CPU == 1) {
            System.out.println("It's a draw, both you and the computer chose paper.");
        } else if (choice.contains("PA") && CPU == 2) {
            System.out.println("You lose, the computer chose scissors and you chose paper.");
        }
        // If statements with unique print statements for computer's choices if user chose scissors
        if (choice.contains("SC") && CPU == 0) {
            System.out.println("You lose, you chose scissors and the computer chose rock.");
        } else if (choice.contains("SC") && CPU == 1) {
            System.out.println("You win, you chose scissors and the computer chose paper.");
        } else if (choice.contains("SC") && CPU == 2) {
            System.out.println("You draw, both you and the computer chose scissors.");
        }
    }

    public static void main(String[] args) {
        while(true) {
            // Always call the continue() function
            Continue();
        }
    }
    
}
