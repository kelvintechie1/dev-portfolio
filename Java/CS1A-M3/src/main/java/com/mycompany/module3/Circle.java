package com.mycompany.module3;
import java.util.*;
public class Circle {
    public static void main(String[] args) {
        Scanner radius = new Scanner(System.in);
        System.out.println("Enter the radius of the desired circle.");
        double rad = radius.nextDouble();
        double pi = 3.14159;
        double area = pi * Math.pow(rad, 2);
        double cir = 2 * pi * rad;
        System.out.println(area);
        System.out.println(cir);
    }
}
