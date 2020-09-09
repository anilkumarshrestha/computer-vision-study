cmake_minimum_required(VERSION 3.1)
project( ImageFlipping VERSION 0.1 
    DESCRIPTION "Flips image" 
                    LANGUAGES CXX )

find_package(OpenCV 4 REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

SET(FILES
    "src/main.cpp"
    "src/flip.cpp"
)

add_executable( image_flipping ${FILES} )
target_include_directories( image_flipping PUBLIC GLOB_RECURSE "${PROJECT_SOURCE_DIR}/include/" )
target_link_libraries( image_flipping ${OpenCV_LIBS} )
