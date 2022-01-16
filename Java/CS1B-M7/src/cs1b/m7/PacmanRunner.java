package cs1b.m7;

/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


import info.gridworld.world.World;
import java.io.File;
import java.util.Scanner;

public class PacmanRunner {
    
    public static void main(String[] args) throws Exception {
        Scanner file = new Scanner(new File("maze.txt"));
        int len = file.nextInt();
        int width = file.nextInt();
        // read the width
        file.nextLine();
        // you should change next line for width also
        World world = new PacWorld(file,len,width);  
    //   World world = new World();
        world.show();
    }
    
}
 