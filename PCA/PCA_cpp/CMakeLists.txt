cmake_minimum_required(VERSION 3.1)
project( PCA VERSION 0.1 
    DESCRIPTION "PCA" 
                    LANGUAGES CXX )


#include_directories(${OpenCV_INCLUDE_DIRS})

SET(FILES
    "src/main.cpp"
)

add_executable( PCA ${FILES} )
target_include_directories( PCA PUBLIC GLOB_RECURSE "${PROJECT_SOURCE_DIR}/include/" )
#target_link_libraries( PCA ${OpenCV_LIBS} )
