/**
 * @file rotate.cpp
 * @brief ratation functions
 * @author
 */

#include<ImageRotation/image_rotation.h>

void ImageRotation(cv::Mat& src, cv::Mat& dst, float angle)
{
    // find the center of image 
    float center_x = src.cols / 2;
    float center_y = src.rows / 2;
    
    int x,y;
   
    // Degree to Rad
    float rad = angle * 3.14/180;
    
    for( int i =0; i < src.cols; i++)
    {
        for( int j = 0; j < src.rows; j++)
        {
            // Translate to origin, then rotate about origin and finally translate back to image center
            x = ((i - center_x) * cos(rad) + (j - center_y)*sin(rad) + center_x);
            y = ((i - center_x) * sin(rad) - (j - center_y)*cos(rad) + center_y);
            
            if((x>=0 && x<src.cols) && (y>=0 && y<src.rows))
            {
                // At each point(x,y) store the value of correspondin (i,j) from source
                dst.at<cv::Vec3b>(cv::Point(x,y)) = src.at<cv::Vec3b>(cv::Point(i,j));
            } 
        }
    }
}

void help()
{
    std::cout << "Rotates image." << std::endl
              << "To run the program: ./image_rotation <image>" << std::endl;
}
