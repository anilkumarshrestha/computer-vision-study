/**
 * @file headers.h
 * @brief includes all the headers
 * @author
 */

#pragma once

#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>

void GreyScaleHistogram( cv::Mat const& src_img );
void ColorHistogram( cv::Mat const& src_img );
void help();
