cmake_minimum_required(VERSION 3.1)
project( FacialEmbedding VERSION 0.1 
    DESCRIPTION "FacialEmbedding" 
                    LANGUAGES CXX )

#find_package(OpenCV 4 REQUIRED)
#include_directories(${OpenCV_INCLUDE_DIRS})

SET(FILES
    "src/main.cpp"
    "src/preprocessing.cpp"
    "src/naive_bayes.cpp"
    "src/Math.cpp"
)
#link_directories(/usr/local/lib/)
add_executable( FacialEmbedding ${FILES} )
set(CMAKE_BUILD_TYPE Debug)
target_include_directories( FacialEmbedding PUBLIC GLOB_RECURSE "${PROJECT_SOURCE_DIR}/include/" )
#target_link_libraries( FacialEmbedding ${OpenCV_LIBS} )
#target_link_libraries( FacialEmbedding cnpy)

