package MusicModule2;

import org.jfugue.player.*;

public class MusicProgram {
    public static void main(String[] args) {
        Player music = new Player(); 
        // Music - Dragonhunter by Richard Meyer
        music.play("I[Violin] T125 Bhq A B A G F# E Rhq E Ei Di E Ei Di Ei F#i Gi F#i E D Ei F#i Gi Ai "
                + "B B C#6 A B R E Ei Di E Ei Di Ei F#i Gi F#i E F# G Ai Bi C#6 D6i C#6i Bhq Rs Bi C#6i D6 C#6i "
                + "Bi C#6 A Bhq Ri Bi C#6i D6i C#6i Bi D6i C#6i Bi Ai C#6i Bh A G F#h G F# Eh D E F#h Rhw C#6h D6h B5h C#6h B5 B5 Rh B5 B5 Rh"
                + "B5 Rs B5i A5i B5 B5i A5i B5i C#6i D6i C#6i B5 B5i A5i B5i C#6i D6i C#6i B5 A5 B5 A5 G5 F#5 E5 Rhq E5 E5i D5i E5 E5i D5i E5i F#5i G5i F#5i E5 D5"
                + "Ei F#5i G5i A5i B5 B5 C#6 A5 B5 R E Ei D5i E Ei D5i Ei F#5i G5i F#5i G5 F#5 E5 Rh E5i D5i E5 Rh E5i D5i E5 E5 Rh");
    }
}
