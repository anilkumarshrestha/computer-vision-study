# Applying Gaussian Blur
Task Definition: Read image and apply gaussian blur on image using C++/OpenCV

### Blur
Blurring or Smoothing is an image processing operation which is used to reduce noise and produce less pixelated images. Mostly, it is achieved with a low pass filter. For this we apply filters on image mostly, linear.

### Gaussian Blur
Gaussian filtering achieved by colvolving each pixel with Gaussian Kernel. The kernel should be odd and moves along the pixel that is being filtered which then replaces the original pixel value with new convolved value (weighted average) in the kernel. The pixels nearest to the center of the kernel are given more weight in Gaussian blur.

Also, larger kernel -> more factored values -> more blur


### Approach
Went through documentations and studies **Gaussian Blur, basic image container, reading images, how pixel values are stored, kernels, and smoothing**

- used `cv::GaussianBlur()` to blur the provided image

### Results
![cat](res/cat.jpg)
Original Image
![blurCat](res/BlurResult.png)
Blurred Image

### Additional
I also compared the time in seconds taken by `cv::GaussianBlur()` and one of the Gaussian Blur Implementation available [Stack Overflow](https://stackoverflow.com/questions/42186498/gaussian-blur-image-processing-c) using `getTickCount()` and `getTickFrequency()`.  `cv::GaussianBlur()` outperformed in this case.


### Resources

- [OpenCV docs](https://docs.opencv.org/4.3.0/dc/dd3/tutorial_gausian_median_blur_bilateral_filter.html)

- [Datacarpentry](https://datacarpentry.org/image-processing/06-blurring/)

- [Stack Overflow](https://stackoverflow.com/questions/42186498/gaussian-blur-image-processing-c)
