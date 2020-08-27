/*
 * Gaussian Blur from OpenCV
 *
 */

#include <iostream>

#include <opencv2/imgcodecs.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/highgui.hpp>

#define KERNEL_LENGTH 27

using namespace cv;

int accessPixel(unsigned char * arr, int col, int row, int k, int width, int height);

//Comparision purpose
//source: https://stackoverflow.com/questions/42186498/gaussian-blur-image-processing-c

int kernel[3][3] = { 1, 2, 1,
                   2, 4, 2,
                   1, 2, 1 };

void gaussian_blur2D(unsigned char * arr, unsigned char * result, int width, int height)
{
    for (int row = 0; row < height; row++)
    {
        for (int col = 0; col < width; col++)
        {
            for (int k = 0; k < 3; k++)
            {
                result[3 * row * width + 3 * col + k] = accessPixel(arr, col, row, k, width, height);
            }
        }
    }
}


int accessPixel(unsigned char * arr, int col, int row, int k, int width, int height)
{
    int sum = 0;
    int sumKernel = 0;

    for (int j = -1; j <= 1; j++)
    {
        for (int i = -1; i <= 1; i++)
        {
            if ((row + j) >= 0 && (row + j) < height && (col + i) >= 0 && (col + i) < width)
            {
                int color = arr[(row + j) * 3 * width + (col + i) * 3 + k];
                sum += color * kernel[i + 1][j + 1];
                sumKernel += kernel[i + 1][j + 1];
            }
        }
    }

    return sum / sumKernel;
}

// !Comparision purpose


int main(int argc, char** argv)
{
    const char* filename = argv[1];
    
    Mat src, dst;
    src = imread(filename, IMREAD_COLOR);

    if( src.empty() )
    {
        std::cout << "The image " << filename << 
                    " could not be loaded. No such file." << std::endl;
        return -1;
    }
    
    double t = getTickCount();

    // Applying Gaussian Blur
    GaussianBlur(src, dst, Size(KERNEL_LENGTH, KERNEL_LENGTH), 0, 0);

    t = ((double)getTickCount() - t)/getTickFrequency();
    std::cout << "Gaussian Blur function (OpenCV) time passed in seconds: " << t << std::endl;
    
    
    namedWindow("Original image");
    namedWindow("Gaussian blured image");

    imshow("Original image", src);
    imshow("Gaussian blured image", dst);

    waitKey(0);

    t = getTickCount(); 
    gaussian_blur2D(src.data, dst.data, src.cols, src.rows);
    t = ((double)getTickCount() - t)/getTickFrequency();
    std::cout << "Gaussian Blur function time passed in seconds: " << t << std::endl;
    
    imshow("img", src);
    imshow("out", dst);
    waitKey(0);

    return 0;
}


