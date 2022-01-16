package com.mycompany.module3;
import java.util.*;
public class MathProblems {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter two positive, whole numbers.");
        int num1 = input.nextInt();
        int num2 = input.nextInt();
        int sumof2 = num1 + num2;
        int productof2 = num1 * num2;
        int diffof2 = num1 - num2;
        int diffof2reversed = num2 - num1;
        int max = Math.max(num1, num2);
        double sqrt = Math.sqrt(num1);
        double sq = Math.pow(num1, 2);
        int times10 = num1 * 10;
        int modulo = num1 % num2;
        int complex = num1 * num2 - num2;
        System.out.println("You entered " + Integer.toString(num1) + " and " + Integer.toString(num2) + ".");
        System.out.println("The sum of these two numbers is: " + Integer.toString(sumof2) + " and the product of these two numbers is: " + Integer.toString(productof2) + ".");
        System.out.println("The difference between the first number and the second number is: " + Integer.toString(diffof2) + ", while the difference between the second and the first number is: " + Integer.toString(diffof2reversed) + ".");
        System.out.println("The larger of these two numbers is " + Integer.toString(max) + ".");
        System.out.println("The square root of the first number is " + Double.toString(sqrt) + ", and the square is " + Double.toString(sq) + ".");
        System.out.println("The first number multiplied by 10 is " + Integer.toString(times10) + ".");
        System.out.println("The remainder if the first number is divided by the second number is: " + Integer.toString(modulo) + ".");
        System.out.println("Last, but certainly not least, if you multiply the first number by the second number and then subtract the product by the second number, the result is: " + Integer.toString(complex) + "!");
    }
}
