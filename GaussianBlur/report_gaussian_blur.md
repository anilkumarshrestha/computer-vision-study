# Gaussan Blur

Anil Kumar Shrestha
(26th August, 2020)

---

Task Definition: Read image and apply gaussian blur on image using C++/OpenCV

### Documentation
Went through documentations and searched about Gaussian Blur.
- understand about **basic image container, reading images, how pixel values are stored, kernels, and smoothing**
#### Gaussian Blur
- mostly used for noise reduction in image
- we define a group of pixels (kernel) around the current pixel and then calculate weighted average of the color values in that group; this is done on every pixel point
- pixel nearest to center is give more weight
- larger kernel -> more factored values -> more blur


### Applied Gaussian Blur

- used `cv::GaussianBlur()` to blur the provided image
- compared the time in seconds taken by `cv::GaussianBlur()` and one of the Gaussian Blurimplementation available [here](https://stackoverflow.com/questions/42186498/gaussian-blur-image-processing-c) using `getTickCount()` and `getTickFrequency()`.  `cv::GaussianBlur()` outperformed in this case.


Resources

https://docs.opencv.org/4.3.0/dc/dd3/tutorial_gausian_median_blur_bilateral_filter.html

https://datacarpentry.org/image-processing/06-blurring/

https://riptutorial.com/opencv/example/6645/smoothing-images-with-gaussian-blur-in-cplusplus

https://stackoverflow.com/questions/42186498/gaussian-blur-image-processing-c


 

