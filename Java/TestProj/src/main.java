import java.util.concurrent.*;
import java.io.*;
import java.util.*;

public class main {
    public static void main(String[] args) throws InterruptedException, IOException {
        String[] people = new String[2];
        people[0] = "Trevor";
        people[1] = "Meow";

        // More Java!
        System.out.println("Java's about to kick your ass in 5 seconds!");

        TimeUnit.SECONDS.sleep(5);

        for (int i = 0; i < 2; i++) {
            System.out.println(people[i] + " sucks!");
        }

        for (int i = 0; i < 5; i++) {
            System.out.println(".");
        }

        System.out.println("Furthermore, " + people[0] + ", your opinion is irrelevant. You suck.");

        System.out.println("Ha, I win!");

    }
}
