cmake_minimum_required(VERSION 3.1)
project( GaussianBlur )
find_package(OpenCV 4 REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable( gaussian_blur src/gaussian_blur.cpp)
target_link_libraries( gaussian_blur ${OpenCV_LIBS})
