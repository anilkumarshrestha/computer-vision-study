/**
 * @file main.cpp
 * @brief Rotate image
 * @author
 */

#include <iostream>
#include <ImageRotation/image_rotation.h>

int main(int argc, char** argv)
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
    
    const char* window_name = "Rotation";
    
    float angle;
    std::cout << "Angle in Degree:";
    std::cin >> angle; 

    cv::Mat dst;
    dst.create(src.size(), src.type());

    // std::cout << src.at<cv::Vec3b>(0,0);
    
    ImageRotation(src, dst, angle);
    
    cv::imshow("original", src);
    cv::imwrite("rotated.png",dst);
    cv::imshow("rotated", dst);
    cv::waitKey(0);

    return 0;

}
