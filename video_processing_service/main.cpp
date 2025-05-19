#include <opencv2/opencv.hpp>
#include <opencv2/objdetect.hpp>
#include <iostream>

using namespace cv;
using namespace std;

int main() {
    // Load pre-trained cascade classifier (for face detection)
    if (!face_cascade.load("haarcascade_frontalface_default.xml")) {
        std::cerr << "Error loading cascade classifier!" << std::endl;
    }
    

    // Open video file or capture device
    VideoCapture cap(0);  // Use 0 for webcam or provide video file path
    if (!cap.isOpened()) {
        cerr << "Error opening video stream or file!" << endl;
        return -1;
    }

    Mat frame;
    while (true) {
        cap >> frame; // Capture frame-by-frame
        if (frame.empty()) break; // Check if frame is empty

        // Convert frame to grayscale
        Mat gray;
        cvtColor(frame, gray, COLOR_BGR2GRAY);

        // Detect faces in the frame
        vector<Rect> faces;
        face_cascade.detectMultiScale(gray, faces);

        // Draw rectangle around detected faces
        for (size_t i = 0; i < faces.size(); i++) {
            rectangle(frame, faces[i], Scalar(255, 0, 0), 2);
        }

        // Show the processed frame
        imshow("Video", frame);

        // Break loop if 'q' is pressed
        if (waitKey(1) == 'q') break;
    }

    // Release video capture and close all OpenCV windows
    cap.release();
    destroyAllWindows();
    return 0;
}
