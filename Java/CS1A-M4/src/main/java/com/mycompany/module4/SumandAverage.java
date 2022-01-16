package com.mycompany.module4;
import java.util.*;
public class SumandAverage {
    public static void main(String[] args) {
        Scanner inputVar = new Scanner(System.in);
        int intNum = 5;
        System.out.println("Provide 5 numbers.");
        int num1 = inputVar.nextInt();
        int num2 = inputVar.nextInt();
        int num3 = inputVar.nextInt();
        int num4 = inputVar.nextInt();
        int num5 = inputVar.nextInt();
        int sum = num1 + num2 + num3 + num4 + num5;
        double avg = 1.0 * sum / intNum;
        System.out.println("Number of integers = " + Integer.toString(intNum));
        System.out.println("Number1 = " + Integer.toString(num1));
        System.out.println("Number2 = " + Integer.toString(num2));
        System.out.println("Number3 = " + Integer.toString(num3));
        System.out.println("Number4 = " + Integer.toString(num4));
        System.out.println("Number5 = " + Integer.toString(num5));
        System.out.println("Sum = " + Integer.toString(sum));
        System.out.println("Average = " + Double.toString(avg));
    }
    
}
