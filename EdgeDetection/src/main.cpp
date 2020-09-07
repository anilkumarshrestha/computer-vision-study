/**
 * @file main.cpp
 * @brief Applies Edge detection
 * @author
 */

#include <iostream>
#include "EdgeDetection/core.hpp"


int main(int argc, char** argv)
{
    const char* filename = argv[1];
    
    if( argc < 2 )
    {
        std::cout << "No source image provided" << std::endl;
        return -1;
    }

    // read the image
    cv::Mat src = cv::imread( cv::samples::findFile(filename) );

    // Check if empty
    if( src.empty() )
    {
        std::cout << "File not found." << std::endl;
        return -1;
    }

    int kernel_size = 3;

    cv::Mat src_gray;
    
    // create destination matrix
    cv::Mat dst;
    dst.create( src.size(), src.type() );

    // convert to grayscale
    cv::cvtColor( src, src_gray, cv::COLOR_BGR2GRAY );
    
    // Apply blur to reduce noise
    cv::blur(src_gray, dst, cv::Size(3,3) );
    
    // Apply Canny Edge detection
    // Using upper:lower threshold as 3:1
    cv::Canny( dst, dst, 30, 90, kernel_size );

    cv::imwrite("canny_edge.png", dst);
    cv::imshow("Source image", src);
    cv::imshow("Canny Edge Detected", dst);
    cv::waitKey(0);
    
    return 0;
}
