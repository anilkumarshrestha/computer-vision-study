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
        help();
        return -1;
    }

    cv:: Mat src = cv::imread( cv::samples::findFile(filename) );

    if( src.empty() )
    {
        std::cout << "File not found." << std::endl;
        help();
        return -1;
    }
    
    // Edge Detection function call here.

    return 0;
}
