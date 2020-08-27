/*
 * Gaussian Blur from OpenCV
 *
 */

#include <iostream>

#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>

#define KERNEL_LENGTH 27

using namespace cv;

int main(int argc, char** argv)
{
    const char* filename = argv[1];
    
    Mat src, dst;
    src = imread(filename, IMREAD_COLOR);

    if( src.empty() )
    {
        std::cout << "The image " << filename << 
                    " could not be loaded. No such file." << std::endl;
        return -1;
    }
    
    double t = getTickCount();

    // Applying Gaussian Blur
    GaussianBlur(src, dst, Size(KERNEL_LENGTH, KERNEL_LENGTH), 0, 0);

    t = ((double)getTickCount() - t)/getTickFrequency();
    std::cout << "Gaussian Blur function (OpenCV) time passed in seconds: " << t << std::endl;
    
    
    namedWindow("Original image");
    namedWindow("Gaussian blured image");

    imshow("Original image", src);
    imshow("Gaussian blured image", dst);

    waitKey(0);

    return 0;
}


