import java.util.*;
public class ChessBoard {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);

        System.out.print("Enter number of scuares needed: ");
        int num= sc.nextInt();
        

        for (int i = 0; i < num; i++) {
            for (int j = 0; j < num; j++) {
                if ((i + j) % 2 == 0) {
                    System.out.print("□ ");
                } else {
                    System.out.print("■ ");
                }        
            }
            System.out.println();
        }
    }
}
