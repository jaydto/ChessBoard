public class ChessBoard4 {
    public static void main(String[] args) {
        int size = 8; // size of the chessboard
        for (int i = 0; i < size; i++) { // iterate over rows
            for (int j = 0; j < size; j++) { // iterate over columns
                if ((i + j) % 2 == 0) { // check if square should be filled
                    System.out.print("* "); // fill square with *
                } else {
                    System.out.print("  "); // leave square empty
                }
            }
            System.out.println(); // start new line for the next row
        }
        System.out.println("*********************************"); // draw line
    }
}
