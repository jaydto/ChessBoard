import org.opencv.core.Core;
import org.opencv.core.Mat;
import org.opencv.core.Point;
import org.opencv.core.Size;
import org.opencv.imgproc.Imgproc;
import org.opencv.videoio.VideoCapture;
import org.opencv.videoio.Videoio;
import org.opencv.core.Scalar;

public class ChessboardDetector {

    static {
        System.loadLibrary(Core.NATIVE_LIBRARY_NAME);
    }

    public static void main(String[] args) {
        // Set up the camera
        VideoCapture camera = new VideoCapture(0);
        camera.set(Videoio.CAP_PROP_FRAME_WIDTH, 640);
        camera.set(Videoio.CAP_PROP_FRAME_HEIGHT, 480);

        // Define the chessboard dimensions
        int rows = 8;
        int cols = 8;

        // Define the size of each square in pixels
        int square_size = 50;

        while (true) {
            // Read a frame from the camera
            Mat frame = new Mat();
            camera.read(frame);

            // Convert the frame to grayscale
            Mat gray = new Mat();
            Imgproc.cvtColor(frame, gray, Imgproc.COLOR_BGR2GRAY);

            // Find the corners of the chessboard
            Mat corners = new Mat();
            boolean found = Imgproc.findChessboardCorners(gray, new Size(cols, rows), corners);

            // If the corners are found, draw the lines
            if (found) {
                corners.reshape(2);

                // Create a blank image to draw the lines on
                Mat img_lines = new Mat(frame.size(), frame.type(), Scalar.all(0));

                // Draw the horizontal lines
                for (int i = 1; i < rows; i++) {
                    Imgproc.line(img_lines, new Point(corners.get(i*cols, 0)), new Point(corners.get(i*cols + cols - 1, 0)), new Scalar(255, 0, 0), 2);
                }

                // Draw the vertical lines
                for (int i = 0; i < cols; i++) {
                    Imgproc.line(img_lines, new Point(corners.get(i, 0)), new Point(corners.get((rows-1)*cols + i, 0)), new Scalar(255, 0, 0), 2);
                }

                // Draw the lines on the original frame
                Core.addWeighted(frame, 0.5, img_lines, 0.5, 0, frame);
            }

            // Show the frame
            Imgproc.imshow("frame", frame);

            // Wait for a key press
            if (Imgproc.waitKey(1) == 'q') {
                break;
            }
        }

        // Release the camera and close all windows
        camera.release();
        Imgproc.destroyAllWindows();
    }
}
