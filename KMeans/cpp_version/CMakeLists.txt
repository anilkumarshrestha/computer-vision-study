cmake_minimum_required(VERSION 3.1)
project( CannyEdge VERSION 0.1 
    DESCRIPTION "KMeans" 
                    LANGUAGES CXX )

find_package(OpenCV 4 REQUIRED)
include_directories(${OpenCV_INCLUDE_DIRS})

SET(FILES
    "src/main.cpp"
)

add_executable( edge ${FILES} )
target_include_directories( kmeans PUBLIC GLOB_RECURSE "${PROJECT_SOURCE_DIR}/include/" )
target_link_libraries( kmeans ${OpenCV_LIBS} )
