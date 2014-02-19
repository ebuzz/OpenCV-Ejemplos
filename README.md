#Ejemplos de OpenCV

Aqui estan todos los ejemplos vistos en el
[video](http://www.youtube.com/watch?v=xH-vDGo0Rzg) y otros mas.

Creditos totales a:

  * http://docs.opencv.org/
  * https://help.ubuntu.com/community/OpenCV
  * http://www.raben.com/book/export/html/3
  
  
##Instalacion OpenCV Linux

###Opcion 1 - 

To install OpenCV 2.4.2 or 2.4.3 on the Ubuntu 12.04 operating system, first install a developer environment to build OpenCV.

    sudo apt-get -y install build-essential cmake pkg-config

Install Image I/O libraries

    sudo apt-get -y install libjpeg62-dev 
    sudo apt-get -y install libtiff4-dev libjasper-dev

Install the GTK dev library

    sudo apt-get -y install  libgtk2.0-dev

Install Video I/O libraries

    sudo apt-get -y install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev

Optional - install support for Firewire video cameras

    sudo apt-get -y install libdc1394-22-dev

Optional - install video streaming libraries

    sudo apt-get -y install libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev 

Optional - install the Python development environment and the Python Numerical library

    sudo apt-get -y install python-dev python-numpy
 
Optional - install the parallel code processing library (the Intel tbb library)

    sudo apt-get -y install libtbb-dev
    
Optional - install the Qt dev library

    sudo apt-get -y install libqt4-dev
    
Now download OpenCV 2.4 to wherever you want to compile the source.

    mkdir xxx
    cd xxx 
    wget http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.2/Op...
    
or 

    wget http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.3/Op...
    tar -xvf OpenCV-2.4.*.tar.bz2
    
Create and build directory and onfigure OpenCV with cmake. Don't forget the .. part at the end of cmake cmd !!

    cd OpenCV-2.4.*
    mkdir build
    cd build
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local
    -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON 
    -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON 
    -D BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON ..
    
Now compile it

    make
    
And finally install OpenCV

    sudo make install
    
###Opcion 2- Ejecutar el archivo.sh(copiar y pegar)

    version="$(wget -q -O - http://sourceforge.net/projects/opencvlibrary/files/opencv-unix | egrep -m1 -o '\"[0-9](\.[0-9])+' | cut -c2-)"
    echo "Installing OpenCV" $version
    mkdir OpenCV
    cd OpenCV
    echo "Removing any pre-installed ffmpeg and x264"
    sudo apt-get -qq remove ffmpeg x264 libx264-dev
    echo "Installing Dependenices"
    sudo apt-get -qq install libopencv-dev build-essential checkinstall cmake pkg-config yasm libtiff4-dev libjpeg-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev python-dev python-numpy libtbb-dev libqt4-dev libgtk2.0-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils ffmpeg
    echo "Downloading OpenCV" $version
    wget -O OpenCV-$version.zip http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/$version/opencv-"$version".zip/download
    echo "Installing OpenCV" $version
    unzip OpenCV-$version.zip
    cd opencv-$version
    mkdir build
    cd build
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON ..
    make -j2
    sudo make install
    sudo sh -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'
    sudo ldconfig
    echo "OpenCV" $version "ready to be used"

