# Script generated with Bloom
pkgdesc="ROS - euscollada"
url='http://ros.org/wiki/euscollada'

pkgname='ros-kinetic-euscollada'
pkgver='0.3.5_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('collada-dom'
'qhull'
'ros-kinetic-assimp-devel'
'ros-kinetic-catkin'
'ros-kinetic-cmake-modules'
'ros-kinetic-collada-parser'
'ros-kinetic-collada-urdf'
'ros-kinetic-mk'
'ros-kinetic-openhrp3'
'ros-kinetic-pr2-description'
'ros-kinetic-resource-retriever'
'ros-kinetic-rosboost-cfg'
'ros-kinetic-rosbuild'
'ros-kinetic-roscpp'
'ros-kinetic-roseus'
'ros-kinetic-rospack'
'ros-kinetic-rostest'
'ros-kinetic-tf'
'ros-kinetic-urdf'
'urdfdom'
'yaml-cpp'
)

depends=('collada-dom'
'qhull'
'ros-kinetic-assimp-devel'
'ros-kinetic-collada-parser'
'ros-kinetic-collada-urdf'
'ros-kinetic-resource-retriever'
'ros-kinetic-roscpp'
'ros-kinetic-rospack'
'ros-kinetic-rostest'
'ros-kinetic-tf'
'ros-kinetic-urdf'
'urdfdom'
'yaml-cpp'
)

conflicts=()
replaces=()

_dir=euscollada
source=()
md5sums=()

prepare() {
    cp -R $startdir/euscollada $srcdir/euscollada
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

