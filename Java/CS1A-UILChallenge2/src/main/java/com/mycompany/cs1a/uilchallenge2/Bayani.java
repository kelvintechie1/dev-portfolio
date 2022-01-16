package com.mycompany.cs1a.uilchallenge2;
import java.util.*;
import java.text.*;
import java.io.*;

public class Bayani {

    public static void main(String[] args) throws IOException {
        Scanner file = new Scanner(new File("bayani.dat"));
        Double total = 0.0;
        while (file.hasNextDouble()) {
            Double num = file.nextDouble();
            total = total + num;
            System.out.printf("        $%7.2f\n", num);
        }
        // System.out.println
        System.out.printf("Total = $%7.2f", total);
    }
    
}
