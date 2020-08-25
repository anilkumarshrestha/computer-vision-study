# Logistic Set Ups
___
## Install Linux
Since I already had linux installed in my system I skipped this step.


## Built OpenCV 4.3

#### Installed dependencies
Dependencies for Manjaro are quite different from that of Ubunutu as it is based on Arch. So Following dependencies were installed. 

    sudo pacman -S base-devel
    Sudo pacman -S cmake 
    Sudo pacman -S gtk3 libjpeg libtiff libpng libx264 ffmpeg v4l-utils libcanberra lapack gcc-fortran
#### Built and Installed OpenCV 4.3 stable version

Challenges encountered:
- pkg-config could not find opencv4.pc

Approach:
- using CMakeLists method worked fine
- Manually linking pkg-config to opencv4.pc

Solution:
- Generated opencv4.pc (usually located at build/unix-install) with OPENCV_GENERATE_PKGCONFIG=YES while building with cmake
- Then linked the file to pkg-config by adding following at the end of ~/.zshrc (~/.bashrc for bash) export PKG_CONFIG_PATH="/usr/local/lib/pkgconfig" 

Test
- compiled samples available at samples/cpp folder in build

## OpenCV modules
I am still exploring the modules in OpenCV.


## Resources


https://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html 
https://techesoterica.com/installing-opencv-on-arch-linux-from-source/ 
https://stackoverflow.com/questions/15320267/package-opencv-was-not-found-in-the-pkg-config-search-path 
https://bbs.archlinux.org/viewtopic.php?id=250444 