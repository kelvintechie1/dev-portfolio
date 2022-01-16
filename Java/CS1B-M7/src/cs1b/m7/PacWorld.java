package cs1b.m7;

import info.gridworld.actor.*;
import info.gridworld.grid.*;
import java.util.Scanner;

// Credit for base code - jmellen
public class PacWorld extends ActorWorld{
    
    public PacWorld(Scanner file, int len, int width) throws Exception
    {
        super(new BoundedGrid<Actor>(len,width));
        for (int i = 0; i < len; i++) {
            String nextLine = file.nextLine();
            // Create walls
            for (int j = 0; j < width; j++) {
                if(nextLine.charAt(j)=='x')
                {
                    wall b = new wall();
                    add(new Location(i,j),b);
                }
            // Create pellets
                if(nextLine.charAt(j)=='-')
                {
                    Actor b = new Actor();
                    add(new Location(i,j),b);
                }
            }
        }
    }
}