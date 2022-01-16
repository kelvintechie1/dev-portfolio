package com.mycompany.modulemethods;

import java.util.*;

class ChooseYourOwnAdventure {

    public static void m1()
    {
        Scanner input = new Scanner(System.in);
        System.out.println("You're quarantining due to COVID-19 and you see a group of people that are actively violating social distancing guidelines. Do you talk them out of it?");
        String ans = input.nextLine();
        ans = ans.toUpperCase();
        
        if(ans.contains("YES"))
        {
            m2();
        }
        else if(ans.contains("NO"))
        {
            m3();
        }
        else
        {
            System.out.println("Please enter a valid response of \"yes\" or \"no\"");
            m1();
        }
    }

    public static void m2()
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Do you get a megaphone?");
        String ans = input.nextLine();
        ans = ans.toUpperCase();
        
        if(ans.contains("YES"))
        {
            m4();
        }
        else if(ans.contains("NO"))
        {
            m5();
        }
        else 
        {
            System.out.println("Please enter a valid response of \"yes\" or \"no\"");
            m2();            
        }
    }
    public static void m3()
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Do you go to the super critical business meeting you have planned?");
        String ans = input.nextLine();
        ans = ans.toUpperCase();
        
        if(ans.contains("YES"))
        {
            m7();
        }
        else if(ans.contains("NO"))
        {
            m6();
        }
        else 
        {
            System.out.println("Please enter a valid response of \"yes\" or \"no\"");
            m3();            
        }
    }
    public static void m4()
    {
        Scanner input = new Scanner(System.in);
        System.out.println("You speak through the megaphone and they hear you, but they look at you with a look of dismissiveness. Do you go closer to try to convince them?");
        String ans = input.nextLine();
        ans = ans.toUpperCase();
        
        if(ans.contains("YES"))
        {
            m7();
        }
        else if(ans.contains("NO"))
        {
            m3();
        }
        else 
        {
            System.out.println("Please enter a valid response of \"yes\" or \"no\"");
            m4();
        }
    }
    public static void m5()
    {
        Scanner input = new Scanner(System.in);
        System.out.println("You try your best to yell at them but they don't hear you. Do you go closer?");
        String ans = input.nextLine();
        ans = ans.toUpperCase();
        
        if(ans.contains("YES"))
        {
            m7();
        }
        else if(ans.contains("NO"))
        {
            m3();
        }
        else 
        {
            
        }
    }  
    public static void m6()
    {
        Scanner input = new Scanner(System.in);
        System.out.println("Your boss has threatened that he will terminate your employment, should you choose not to attend the meeting. Do you attend the meeting?");
        String ans = input.nextLine();
        ans = ans.toUpperCase();
        
        if(ans.contains("YES"))
        {
            m7();
        }
        else if(ans.contains("NO"))
        {
            m8();
        }
        else 
        {
            System.out.println("Please enter a valid response of \"yes\" or \"no\"");
            m6();
        }
    }
    public static void m7()
    {
        Scanner input = new Scanner(System.in);
        System.out.println("You find out that you've been exposed to coronavirus. Do you go to get tested?");
        String ans = input.nextLine();
        ans = ans.toUpperCase();
        
        if(ans.contains("YES"))
        {
            m10();
        }
        else if(ans.contains("NO"))
        {
            m11();
        }
        else 
        {
            System.out.println("Please enter a valid response of \"yes\" or \"no\"");
            m7(); 
        }
    }
    public static void m8()
    {
        Scanner input = new Scanner(System.in);
        System.out.println("You now have no source of income during the coronavirus season. However, you found a job as a cashier at a grocery store, one of the few businesses still open. Do you take this job?");
        String ans = input.nextLine();
        ans = ans.toUpperCase();
        
        if(ans.contains("YES"))
        {
            m7();
        }
        else if(ans.contains("NO"))
        {
            m9();
        }
        else 
        {
            System.out.println("Please enter a valid response of \"yes\" or \"no\"");
            m8();  
        }
    }
    public static void m9()
    {
        Scanner input = new Scanner(System.in);
        System.out.println("You are at no point exposed to the coronavirus and have taken all the safe precautions to ensure that you do not get infected. Your friend allows you access to some of her excess funds to ensure your survival while you have no job and you look for other benefits to ensure proper funds during this time.");
        System.out.println("Do you wish to return to the beginning and try it with a new set of outcomes?");
        String ans = input.nextLine();
        ans = ans.toUpperCase();
        
        if(ans.contains("YES"))
        {
          m1();
        }
        else 
        {
          System.out.println("Thanks for playing!"); 
        }
    }
    public static void m10()
    {
        Scanner input = new Scanner(System.in);
        System.out.println("You find out that you are infected with the coronavirus and are ordered to stay home, receiving proper medical care during that period.");
        System.out.println("Do you wish to return to the beginning and try it with a new set of outcomes?");
        String ans = input.nextLine();
        ans = ans.toUpperCase();
        
        if(ans.contains("YES"))
        {
          m1();
        }
        else 
        {
          System.out.println("Thanks for playing!"); 
        }
    }  
    public static void m11()
    {
        Scanner input = new Scanner(System.in);
        System.out.println("You experience a severe case of coronavirus with no medical support ready and die as a result of the complications.");
        System.out.println("Do you wish to return to the beginning and try it with a new set of outcomes?");
        String ans = input.nextLine();
        ans = ans.toUpperCase();
        
        if(ans.contains("YES"))
        {
          m1();
        }
        else 
        {
          System.out.println("Thanks for playing!"); 
        }
    }
    public static void main(String[] args) {
        System.out.println("Welcome to Kelvin Tran's Coronavirus-themed Choose your Own Adventure game! The questions and scenarios that you will be presented with will differ depending on the responses you give! Try it out with multiple responses if you'd like. Be sure to answer with the exact phrases \"yes\" or \"no\" (without quotes) for your answer to be accepted. Good luck!");
        m1();
    }

}