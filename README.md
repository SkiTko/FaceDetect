# 画像分類


## 必要なもの

* Python 3
* pyenv


## インストール手順

```
sudo apt-get install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
pyenv install 3.7.3
source mkvenv.src.sh
```

必要なパッケージをインストール
```
pip install numpy scipy matplotlib opencv-python
```

OpenCV をビルドしてインストール。
```
git clone https://github.com/opencv/opencv.git
git clone https://github.com/opencv/opencv_contrib.git
cd opencv
git checkout 4.1.0
cd ../opencv_contrib
git checkout 4.1.0
cd ../opencv
mkdir build
cd build

cmake \
-G "Unix Makefiles" \
--build . \
-D BUILD_CUDA_STUBS=ON \
-D BUILD_DOCS=OFF \
-D BUILD_EXAMPLES=OFF \
-D BUILD_FFMPEG=OFF \
-D BUILD_JASPER=OFF \
-D BUILD_JPEG=OFF \
-D BUILD_NEW_PYTHON_SUPPORT=ON \
-D BUILD_OPENEXR=OFF \
-D BUILD_PACKAGE=ON \
-D BUILD_PERF_TESTS=OFF \
-D BUILD_PNG=OFF \
-D BUILD_SHARED_LIBS=ON \
-D BUILD_TBB=OFF \
-D BUILD_TESTS=OFF \
-D BUILD_TIFF=OFF \
-D BUILD_WEBP=OFF \
-D BUILD_WITH_DEBUG_INFO=ON \
-D BUILD_ZLIB=OFF \
-D ENABLE_NEON=OFF \
-D ENABLE_PRECOMPILED_HEADERS=OFF \
-D BUILD_opencv_apps=ON \
-D BUILD_opencv_calib3d=ON \
-D BUILD_opencv_core=ON \
-D BUILD_opencv_cudaarithm=ON \
-D BUILD_opencv_cudabgsegm=ON \
-D BUILD_opencv_cudacodec=OFF \
-D BUILD_opencv_cudafeatures2d=ON \
-D BUILD_opencv_cudafilters=ON \
-D BUILD_opencv_cudaimgproc=ON \
-D BUILD_opencv_cudalegacy=ON \
-D BUILD_opencv_cudaobjdetect=ON \
-D BUILD_opencv_cudaoptflow=ON \
-D BUILD_opencv_cudastereo=ON \
-D BUILD_opencv_cudawarping=ON \
-D BUILD_opencv_cudev=ON \
-D BUILD_opencv_features2d=ON \
-D BUILD_opencv_flann=ON \
-D BUILD_opencv_highgui=ON \
-D BUILD_opencv_imgcodecs=ON \
-D BUILD_opencv_imgproc=ON \
-D BUILD_opencv_java=OFF \
-D BUILD_opencv_ml=ON \
-D BUILD_opencv_objdetect=ON \
-D BUILD_opencv_photo=ON \
-D BUILD_opencv_python2=OFF \
-D BUILD_opencv_python3=ON \
-D BUILD_opencv_shape=ON \
-D BUILD_opencv_stitching=ON \
-D BUILD_opencv_superres=ON \
-D BUILD_opencv_ts=ON \
-D BUILD_opencv_video=ON \
-D BUILD_opencv_videoio=ON \
-D BUILD_opencv_videostab=ON \
-D BUILD_opencv_viz=OFF \
-D BUILD_opencv_world=OFF \
-D CUDA_FAST_MATH=ON \
-D CMAKE_BUILD_TYPE=RELEASE \
-D ENABLE_FAST_MATH=ON \
-D WITH_1394=ON \
-D WITH_CUBLAS=ON \
-D WITH_CUDA=ON \
-D WITH_CUFFT=ON \
-D WITH_EIGEN=ON \
-D WITH_FFMPEG=ON \
-D WITH_GDAL=OFF \
-D WITH_GPHOTO2=OFF \
-D WITH_GIGEAPI=ON \
-D WITH_GSTREAMER=OFF \
-D WITH_GTK=ON \
-D WITH_INTELPERC=OFF \
-D WITH_IPP=ON \
-D WITH_IPP_A=OFF \
-D WITH_JASPER=ON \
-D WITH_JPEG=ON \
-D WITH_LIBV4L=ON \
-D WITH_OPENCL=ON \
-D WITH_OPENCLAMDBLAS=OFF \
-D WITH_OPENCLAMDFFT=OFF \
-D WITH_OPENCL_SVM=OFF \
-D WITH_OPENEXR=ON \
-D WITH_OPENGL=ON \
-D WITH_OPENMP=OFF \
-D WITH_OPENNI=OFF \
-D WITH_PNG=ON \
-D WITH_PTHREADS_PF=OFF \
-D WITH_PVAPI=OFF \
-D WITH_QT=OFF \
-D WITH_TBB=ON \
-D WITH_TIFF=ON \
-D WITH_UNICAP=OFF \
-D WITH_V4L=ON \
-D WITH_VTK=OFF \
-D WITH_WEBP=ON \
-D WITH_XIMEA=OFF \
-D WITH_XINE=OFF \
-D WITH_LAPACKE=ON \
-D WITH_MATLAB=OFF \
-D OPENCV_EXTRA_MODULES_PATH=$HOME/Documents/dev/opencv/opencv_contrib/modules \
-D CMAKE_INSTALL_PREFIX=$(python3 -c "import sys; print(sys.prefix)") \
-D PYTHON_EXECUTABLE=$(which python3)  \
-D PYTHON_LIBRARY=$HOME/.pyenv/versions/3.7.3/lib/libpython3.7m.a \
-D PYTHON_INCLUDE_DIR=$(python3 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())")  \
-D PYTHON_PACKAGES_PATH=$(python3 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") \
-D INSTALL_C_EXAMPLES=OFF \
-D INSTALL_PYTHON_EXAMPLES=ON \
..
make -j 12
make install
```
