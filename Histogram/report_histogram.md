# Creating Histogram


Anil Kumar Shrestha (30th August, 2020)


--
## Color Channels
#### RGB
Most commonly, pixels in colorful images can be grouped into one of three channels Red, Green, and Blue. 
- 24-bit RGB ==> 8-bit each channel

#### CMYK
C -> Cyan, M -> Magenta, Y -> Yellow, and K -> Black.

#### Alpha Channel
-stores transparency

## Histogram
Histograms basically plots the frequency of each intensity value in image i.e the number of times each intensity value repeated over the entire image. However, it does not give the location of that intensity and hence we cannot reconstruct image from histogram alone.

Suppose we have a 8-bit grayscale image, then there will be 256 different possible intensities. And the histogram of this image will have higher frequency towards right if the image has more bright part and towards left if the image has more darker part.  

Usages:
- convert Grayscale image to binary and separate backgroud


## Program

#### Read the image and call respective funations.
```
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
```
#### Gray Scale Histogram
First we convert color image to gray scale using `cv::cvtColor(src_img, gray_img, cv::COLOR_BGR2GRAY)` and then calculate the histogram using `cv::calcHist()`. 


We pass pointer of the source image `gray_img` to the function `calcHist()` and the result is stored in matrix `hist`. Similarly, we also pass  
```
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
```

Then we normalize and display the histogram

```
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

    cv::imshow("Grayscale Image", gray_img);
    cv::imshow("Grayscale hist", histImage);

} // End of GrayScaleHistogram()
```

Displaying BGR channel histogram is similar to that of grayscale except the fact that here we split the channels and then show each individually.

```
/ show color histogram
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
    cv::imshow("Histogram", histImage);

}
```


### Resources:

https://docs.opencv.org/master/d8/dbc/tutorial_histogram_calculation.html

https://towardsdatascience.com/exploring-image-processing-techniques-opencv-4860006a243

https://homepages.inf.ed.ac.uk/rbf/HIPR2/histgram.htm
