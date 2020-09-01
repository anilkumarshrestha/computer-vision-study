cmake_minimum_required(VERSION 3.1)
project( Histogram VERSION 0.1 
                    DESCRIPTION "Creates histogram of given image" 
                    LANGUAGES CXX )

find_package(OpenCV 4 REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

SET(FILES
    "src/main.cpp"
    "src/create_histogram.cpp"
)

add_executable( histogram ${FILES} )
target_include_directories( histogram PUBLIC GLOB_RECURSE "${PROJECT_SOURCE_DIR}/include/" )
target_link_libraries( histogram ${OpenCV_LIBS} )
