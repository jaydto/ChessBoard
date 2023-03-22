import java.util.*;
public class ChessBoard3 {
    public static void main(String[] args) {
        Scanner sc= new Scanner(System.in);

        System.out.print("Enter number of scuares needed: ");
        int size= sc.nextInt();
        
        
        for (int i = 0; i < size; i++) {
            // draw top border of each box
            // for (int j = 0; j < size; j++) {
            //     System.out.print("*****");
            // }
            // System.out.println("*");
            
            // draw middle of each box
            for (int k = 0; k < 3; k++) {
                for (int j = 0; j < size; j++) {
                    if ((i + j) % 2 == 0) {
                    System.out.print("*****");
                } else {
                    System.out.print("*     ");
                }  
                    
                }
                System.out.println("*");
            }
        }
        
        // draw bottom border of the chess board
        // for (int j = 0; j < size; j++) {
        //     System.out.print("*****");
        // }
        // System.out.println("*");
    }
}
