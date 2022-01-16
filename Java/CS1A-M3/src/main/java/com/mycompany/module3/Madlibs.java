package com.mycompany.module3;
import java.util.*;
public class Madlibs {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter your favorite technological device. ");
        String TechDevice1 = input.nextLine();
        System.out.println("Enter your second favorite technological device or appliance. ");
        String TechDevice2 = input.nextLine();
        System.out.println("Enter your age. ");
        String Age = input.nextLine();
        System.out.println("Enter your favorite book. ");
        String Book = input.nextLine();
        System.out.println("Finally, enter your name. ");
        String Name = input.nextLine();
        // Produce Madlibs story based on input provided in variables.
        System.out.println(Name + " at age " + Age + " loves " + Book + ".");
        System.out.println("They love this book so much, they accidentally threw their " + TechDevice1 + " into the air and broke it when a relationship in the book split up.");
        System.out.println("Fortunately, they had their " + TechDevice2 + ", so it was no big deal.");
    }
}
