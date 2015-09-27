#!/bin/bash

cmake \
    -Dpfasst_BUILD_TESTS=OFF \
    -DCMAKE_TOOLCHAIN_FILE=../cmake/toolchain_jureca_intel.cmake \
    -DEigen3_INCLUDE_PATH=~/jureca/include/eigen3 \
    -Dpfasst_WITH_EXTRA_WRAPPER=ON \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_EXPORT_COMPILE_COMMANDS=ON \
    -Dpfasst_WITH_LOGGING=OFF \
    ..
