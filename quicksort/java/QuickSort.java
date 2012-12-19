import java.util.List;
import java.util.Random;
import java.util.ArrayList;
import java.io.IOException;
import java.util.Scanner;
import java.io.FileReader;

public class QuickSort {

    private static Random rand;

    static List<Integer> quickSort(List<Integer> A) {
        if (A.size() <= 1) {
            return A;
        }
        int pivotIndex = rand.nextInt(A.size());
        int pivot = A.get(pivotIndex);
        A.set(pivotIndex, null);
        List<Integer> less = new ArrayList<Integer>();
        List<Integer> greater = new ArrayList<Integer>();
        for (Integer x : A) {
            if (x == null) {
                continue;
            }
            if (x <= pivot) {
                less.add(x);
            } else {
                greater.add(x);
            }
        }
        less = quickSort(less);
        less.add(pivot);
        less.addAll(quickSort(greater));
        return less;
    }

    public static void main(String[] args) {
        rand = new Random();
        List<Integer> A = new ArrayList<Integer>();
        Scanner sc;
        try {
            sc = new Scanner(new FileReader(args[0]));
        } catch (IOException ex) {
            System.err.println("OH NO");
            return;
        }
        while (sc.hasNextInt()) {
            A.add(sc.nextInt());
        }
        quickSort(A);
    }

}
