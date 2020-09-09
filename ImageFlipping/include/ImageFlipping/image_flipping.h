/**
 * @file image_flipping.h
 * @brief Headers
 * @author
 */

#include <iostream>
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

void help();
void flipH(cv::Mat&, cv::Mat&);
void flipV(cv::Mat&, cv::Mat&);
