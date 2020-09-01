/**
 * @file main.cpp
 * @brief Main file to create histogram
 * @author
 */

#include "histogram/core.hpp"
#include <iostream>

int main( int argc, char** argv )
{
    const char* filename = argv[1];
    if( argc < 2 )
    {
        help();
        return -1;
    }
    
    cv::Mat src = cv::imread( cv::samples::findFile(filename) );
    
    if( src.empty() )
    {
        std::cout << "File not found." << std::endl;
        help();
        return -1;
    }
    
    GreyScaleHistogram( src );

    ColorHistogram( src );
    
    cv::waitKey();
    
    return 0;
}

