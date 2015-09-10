cmake \
	-DBOOST_ROOT=/homec/gsp15/gsp1514/juqueen/ \
	-Dpfasst_BUILD_TESTS=OFF \
	-Dpfasst_BUILD_SHARED_LIBS=OFF \
	-DCMAKE_TOOLCHAIN_FILE=../cmake/toolchain_juqueen.cmake \
	-DEigen3_INCLUDE_PATH=~/juqueen/include/eigen3 \
	-Dpfasst_WITH_EXTRA_WRAPPER=ON \
	\ #-DCMAKE_BUILD_TYPE=Release \
	..
