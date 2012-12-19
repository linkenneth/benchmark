import java.util.Random;

/** Generates a random sequence of integers of length ARG[0].
 *
 *  Usage: java RandGen N > file, where N is the number of random integers
 *  to generate. You should redirect the output to a file because, well,
 *  this could print a LOT of stuff.
 *  @author Kenneth Lin */
public class RandGen {

    public static void main(String[] args) {
        int i = Integer.parseInt(args[0]);
        Random rand = new Random(42);
        while (i-- > 0) {
            System.out.println(rand.nextInt());
        }
    }

}
