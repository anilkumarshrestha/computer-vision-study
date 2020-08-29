cmake_minimum_required(VERSION 3.1)
project( Histogram )
find_package(OpenCV 4 REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

add_executable( create_histogram src/create_histogram.cpp)
target_link_libraries( create_histogram ${OpenCV_LIBS})
