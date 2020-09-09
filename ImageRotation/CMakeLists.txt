cmake_minimum_required(VERSION 3.1)
project( ImageRotation VERSION 0.1 
    DESCRIPTION "Rotate image" 
                    LANGUAGES CXX )

find_package(OpenCV 4 REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

SET(FILES
    "src/main.cpp"
    "src/rotate.cpp"
)

add_executable( image_rotation ${FILES} )
target_include_directories( image_rotation PUBLIC GLOB_RECURSE "${PROJECT_SOURCE_DIR}/include/" )
target_link_libraries( image_rotation ${OpenCV_LIBS} )
