Name:           ros-jade-eus-assimp
Version:        0.2.1
Release:        2%{?dist}
Summary:        ROS eus_assimp package

Group:          Development/Libraries
License:        BSD
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-assimp-devel
Requires:       ros-jade-roseus
BuildRequires:  pkgconfig
BuildRequires:  ros-jade-assimp-devel
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-euslisp

%description
eus_assimp

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
* Mon Dec 07 2015 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.2.1-2
- Autogenerated by Bloom

* Thu Dec 03 2015 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.2.1-1
- Autogenerated by Bloom

* Mon Nov 30 2015 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.2.1-0
- Autogenerated by Bloom

* Thu Nov 05 2015 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.1.13-4
- Autogenerated by Bloom

* Wed Nov 04 2015 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.1.13-3
- Autogenerated by Bloom

* Tue Nov 03 2015 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.1.13-2
- Autogenerated by Bloom

* Tue Nov 03 2015 Yohei Kakiuchi <youhei@jsk.imi.i.u-tokyo.ac.jp> - 0.1.13-1
- Autogenerated by Bloom

