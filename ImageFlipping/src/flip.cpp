/**
 * @file flip.cpp
 * @brief function definition
 * @author
 */

#include <iostream>
#include <ImageFlipping/image_flipping.h>


/*
// horizontal flipping using C method
void flipHRef(cv::Mat &src, cv::Mat &dst) 
{
     
    int channels = src.channels();
    int nRows = src.rows;
    int nCols = src.cols * channels;

    int i,j;
    uchar* p;
    for( i = 0; i < nRows; ++i)
    {
        p = dst.ptr<uchar>(i);
        for ( j = 0; j < nCols; ++j)
        {
            p[j] = ;
        }
    }
}
*/
/* using Iterator
void flipHRef(cv::Mat &src, cv::Mat &dst)
{
    cv::MatIterator_<cv::Vec3b> it, end;
    for( it = src.begin<cv::Vec3b>(), end = src.end<cv::Vec3b>(); it != end; ++it)
    {
        (*it)[0]
    }
}

*/

void flipH(cv::Mat &src, cv::Mat &dst)
{
    for( int i = 0; i < src.rows; i++ )
    {
        for( int j = 0; j < src.cols; j++)
        {
            dst.at<cv::Vec3b>(i,j) = src.at<cv::Vec3b>(src.cols - i, j);
        }

    }
}

void flipV(cv::Mat &src, cv::Mat &dst)
{
    for( int i = 0; i < src.rows; i++ )
    {
        for( int j = 0; j < src.cols; j++)
        {
            dst.at<cv::Vec3b>(i,j) = src.at<cv::Vec3b>(i, src.cols - j);
        }

    }
}

void help()
{
    std::cout << "This program shows the histogram of image." << std::endl
              << "To run the program: ./create_histogram <image>" << std::endl;
}
