/**
 * @file create_histogram.cpp
 * @brief Simply create the color / intensity histogram from given image
 * @author
 */

#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.cpp>
#include <opencv2/imgproc.cpp>

#include <iostream>

int main( int argc, char** argv )
{
    cv::Mat src = imread( cv::samples::findFile(argv[1]) );
    if( src.empty() )
    {
        std::cout << "File not found." << filename << "Does not exist." << std::endl;
        help();
        return -1;
    }
    
    vector<Mat> planes;
    
    //![Split] Split the given image into B, G, and R planes
    cv::split( src, planes );
    


}
