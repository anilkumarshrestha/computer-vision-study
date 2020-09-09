/**
 * @file main.cpp
 * @brief Flips image horizontally and vertically
 * @author
 */

#include <iostream>
#include <ImageFlipping/image_flipping.h>

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
    

    cv::Mat dst_h(src.size(), src.type());
    cv::Mat dst_v(src.size(), src.type());

    flipH(src, dst_h);
    flipV(src, dst_v);
   

    cv::imwrite("horizontal_flip.png",dst_h);
    cv::imshow("Horizontal flip", dst_h);

    cv::imwrite("vertical_flip.png",dst_v);
    cv::imshow("Vertical flip", dst_v);


    cv::waitKey(0);

    return 0;

}
