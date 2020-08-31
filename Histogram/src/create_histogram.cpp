/**
 * @file create_histogram.cpp
 * @brief Simply create the color / intensity histogram from given image
 * @author
 */

#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

#include <iostream>

// Show Grey Scale (Intensity) Histogram
void GreyScaleHistogram(cv::Mat const& src_img )
{
    cv::Mat gray_img;
    cv::cvtColor(src_img, gray_img, cv::COLOR_BGR2GRAY);

    int histSize = 256;
    
    int channels[] = {0};
    
    float range[] = { 0, 256 }; // excluding 256
    const float* histRange = { range };

    bool uniform = true, accumulate = false;
    
    // Calculate histogram and store in hist
    cv::Mat hist;
    cv::calcHist( &gray_img, 1, channels, cv::Mat(), hist, 1, &histSize, &histRange, uniform, accumulate);
    
    // display size
    int hist_w = 512, hist_h = 400;
    int bin_w = cvRound( (double) hist_w/histSize );

    // Create matrix to show histogram
    cv::Mat histImage( hist_h, hist_w, CV_8UC3, cv::Scalar( 0,0,0 ) );
    normalize( hist, hist, 0, histImage.rows, cv::NORM_MINMAX, -1, cv::Mat() );

    for( int i = 1; i < histSize; i++)
    {
        cv::line( histImage, cv::Point( bin_w*(i-1), hist_h - cvRound(hist.at<float>(i-1)) ),
              cv::Point( bin_w*(i), hist_h - cvRound(hist.at<float>(i)) ),
              cv::Scalar::all(255));
    }
   
    // Show both image on a single window
    /*
    int width = 2*image.cols;
    int height = image.rows;

    cv::Mat combinedImage = cv::Mat(height, width, image.type());

    cv::Rect subImageROI = cv::Rect(0, 0, image.cols, image.rows);

    image.copyTo(combinedImage(subImageROI));

    subImageROI.x = image.cols;
    histImage.copyTo(combinedImage(subImageROI));
    */

    cv::imshow("Grayscale Image", gray_img);
    cv::imshow("Grayscale Histogram", histImage);

}

// show color histogram
void ColorHistogram(cv::Mat const& src_img)
{
    // Split channels and store in bgr_palanes
    std::vector<cv::Mat> bgr_planes;
    cv::split( src_img, bgr_planes );

    int histSize = 256;
    
    float range[] = {0, 256};
    const float* histRange = {range};

    bool uniform = true, accumulate = false;

    cv::Mat b_hist, g_hist, r_hist;
    calcHist( &bgr_planes[0], 1, 0, cv::Mat(), b_hist, 1, &histSize, &histRange, uniform, accumulate );
    calcHist( &bgr_planes[1], 1, 0, cv::Mat(), g_hist, 1, &histSize, &histRange, uniform, accumulate );
    calcHist( &bgr_planes[2], 1, 0, cv::Mat(), r_hist, 1, &histSize, &histRange, uniform, accumulate );
   
    int hist_w = 512, hist_h = 400;
    int bin_w = cvRound( (double) hist_w/histSize );
    
    // create matrix for histogram visualization
    cv::Mat histImage( hist_h, hist_w, CV_8UC3, cv::Scalar(0, 0, 0) );

    cv::normalize(b_hist, b_hist, 0, histImage.rows, cv::NORM_MINMAX, -1, cv::Mat() );
    cv::normalize(g_hist, g_hist, 0, histImage.rows, cv::NORM_MINMAX, -1, cv::Mat() );
    cv::normalize(r_hist, r_hist, 0, histImage.rows, cv::NORM_MINMAX, -1, cv::Mat() );

    for(int i = 1; i < histSize; i++)
    {
        cv::line( histImage, cv::Point( bin_w * (i-1), hist_h - cvRound(b_hist.at<float>(i - 1))),
                cv::Point(bin_w * (i), hist_h - cvRound(b_hist.at<float>(i)) ),
                cv::Scalar( 255, 0, 0), 2, 8, 0);
        cv::line( histImage, cv::Point( bin_w * (i-1), hist_h - cvRound(g_hist.at<float>(i - 1)) ),
                cv::Point( bin_w*(i), hist_h - cvRound(g_hist.at<float>(i)) ),
                cv::Scalar(0, 255, 0), 2, 8, 0);
        cv::line( histImage, cv::Point( bin_w * (i-1), hist_h - cvRound(r_hist.at<float>(i - 1)) ),
                cv::Point( bin_w*(i), hist_h - cvRound(r_hist.at<float>(i)) ),
                cv::Scalar(0, 0, 255), 2, 8, 0);
    }
    
    cv::imshow("Original Image", src_img );
    cv::imshow("COlor Histogram", histImage);

}

void help()
{
    std::cout << "This program shows the histogram of image." << std::endl
              << "To run the program: ./create_histogram <image>" << std::endl;
}

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
