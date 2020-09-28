# Logistic Set Ups
___
## Install Linux
Since I already had linux installed in my system I skipped this step.


## Built OpenCV 4.3
#### Installed dependencies
Dependencies for Manjaro are quite different from that of Ubunutu as it is based on Arch. So following dependencies were installed: 
```
sudo pacman -S base-devel
sudo pacman -S cmake 
sudo pacman -S gtk3 libjpeg libtiff libpng libx264 ffmpeg v4l-utils libcanberra lapack gcc-fortran
```


#### Built and Installed OpenCV 4.3 stable version
1. Download file from OpenCV official site or git repo
2. create build directory
```
cd mkdir build
cd build
```
3. Configuring

- Configure and generate using cmake or cmake-gui 
- Make sure to enable `OPENCV_ENABLE_NONFREE` and `OPENCV_GENERATE_PKGCONFIG`
 
4. make
```
cd build
#make -jx where x is the number of jobs in parallel. eg:
make -j7
```
5. Finally installation
```
sudo make install
```

6. Test
- compiled samples available at samples/cpp folder in build
```
g++ squares.cpp -o sq `pkg-config opencv4 --cflags --libs`
```

#### Challenges encountered:
- pkg-config could not find `opencv4.pc`
- finding dependency packages in Manjaro for OpenCV

Approach:
- using CMakeLists method worked fine
- manually linking pkg-config to `opencv4.pc`

Solution:
- generated `opencv4.pc` (usually located at build/unix-install) with `OPENCV_GENERATE_PKGCONFIG=YES` while building with cmake
- then linked the file to `pkg-config` by adding following at the end of `~/.zshrc (~/.bashrc for bash) export PKG_CONFIG_PATH="/usr/local/lib/pkgconfig"` 



## Resources


https://docs.opencv.org/trunk/d7/d9f/tutorial_linux_install.html 
https://techesoterica.com/installing-opencv-on-arch-linux-from-source/ 
https://stackoverflow.com/questions/15320267/package-opencv-was-not-found-in-the-pkg-config-search-path 
https://bbs.archlinux.org/viewtopic.php?id=250444 
