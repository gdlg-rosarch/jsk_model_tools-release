Name:           ros-jade-euscollada
Version:        0.2.4
Release:        0%{?dist}
Summary:        ROS euscollada package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/euscollada
Source0:        %{name}-%{version}.tar.gz

Requires:       collada-dom-devel
Requires:       qhull-devel
Requires:       ros-jade-assimp-devel
Requires:       ros-jade-collada-parser
Requires:       ros-jade-collada-urdf
Requires:       ros-jade-resource-retriever
Requires:       ros-jade-roscpp
Requires:       ros-jade-rospack
Requires:       ros-jade-tf
Requires:       ros-jade-urdf
Requires:       urdfdom-devel
Requires:       yaml-cpp-devel
BuildRequires:  collada-dom-devel
BuildRequires:  qhull-devel
BuildRequires:  ros-jade-assimp-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cmake-modules
BuildRequires:  ros-jade-collada-parser
BuildRequires:  ros-jade-collada-urdf
BuildRequires:  ros-jade-mk
BuildRequires:  ros-jade-resource-retriever
BuildRequires:  ros-jade-rosboost-cfg
BuildRequires:  ros-jade-rosbuild
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-rospack
BuildRequires:  ros-jade-tf
BuildRequires:  ros-jade-urdf
BuildRequires:  urdfdom-devel
BuildRequires:  yaml-cpp-devel

%description
euscollada

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Sat Apr 30 2016 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.4-0
- Autogenerated by Bloom

* Thu Dec 31 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.3-0
- Autogenerated by Bloom

* Tue Dec 15 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.2-3
- Autogenerated by Bloom

* Tue Dec 15 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.2-2
- Autogenerated by Bloom

* Mon Dec 14 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.2-1
- Autogenerated by Bloom

* Mon Dec 14 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.2-0
- Autogenerated by Bloom

* Tue Dec 08 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.1-4
- Autogenerated by Bloom

* Tue Dec 08 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.1-3
- Autogenerated by Bloom

* Mon Dec 07 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.1-2
- Autogenerated by Bloom

* Thu Dec 03 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.1-1
- Autogenerated by Bloom

* Mon Nov 30 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.2.1-0
- Autogenerated by Bloom

* Thu Nov 05 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.13-4
- Autogenerated by Bloom

* Wed Nov 04 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.13-3
- Autogenerated by Bloom

* Tue Nov 03 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.13-2
- Autogenerated by Bloom

* Tue Nov 03 2015 Yohei Kakiuchi <youhei@jsk.t.u-tokyo.ac.jp> - 0.1.13-1
- Autogenerated by Bloom

