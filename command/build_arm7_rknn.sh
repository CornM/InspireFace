mkdir -p build/arm32_rknn
cd build/arm32_rknn
# export cross_compile_toolchain=/home/s4129/software/gcc-arm-8.3-2019.03-x86_64-arm-linux-gnueabihf
cmake -DCMAKE_SYSTEM_NAME=Linux \
  -DCMAKE_SYSTEM_VERSION=1 \
  -DCMAKE_SYSTEM_PROCESSOR=armv7 \
  -DCMAKE_C_COMPILER=$ARM_CROSS_COMPILE_TOOLCHAIN/bin/arm-linux-gnueabihf-gcc \
  -DCMAKE_CXX_COMPILER=$ARM_CROSS_COMPILE_TOOLCHAIN/bin/arm-linux-gnueabihf-g++ \
  -DBUILD_LINUX_ARM7=ON \
  -DENABLE_RKNN=ON \
  -DBUILD_HYPERFACE_TEST=OFF \
  -DBUILD_SHARED_LIBS=OFF ../../

make -j4