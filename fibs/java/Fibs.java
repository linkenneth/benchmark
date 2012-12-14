public class Fibs {

    static int fibs(int n) {
        if (n <= 1) {
            return 1;
        } else {
            return fibs(n - 1) + fibs(n - 2);
        }
    }

    public static void main(String[] args) {
        System.out.println(fibs(Integer.parseInt(args[0])));
    }

}
