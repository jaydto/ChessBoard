public class ChessBoard3 {
    public static void main(String[] args) {
        int size = 8;
        for (int i = 0; i < size; i++) {
            // draw top border of each box
            for (int j = 0; j < size; j++) {
                System.out.print("*****");
            }
            System.out.println("*");
            
            // draw middle of each box
            for (int k = 0; k < 3; k++) {
                for (int j = 0; j < size; j++) {
                    System.out.print("*    ");
                }
                System.out.println("*");
            }
        }
        
        // draw bottom border of the chess board
        for (int j = 0; j < size; j++) {
            System.out.print("*****");
        }
        System.out.println("*");
    }
}
