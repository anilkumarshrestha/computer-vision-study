/*
 *
 *
 */
#include <iostream>

#include <opencv2/core.hpp>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>


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
    
    std::cout << "Load successful " << std::endl;
    imshow("Input image", src);
    waitKey(0);

    return 0;
}
