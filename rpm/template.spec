Name:           ros-kinetic-rviz
Version:        1.12.16
Release:        0%{?dist}
Summary:        ROS rviz package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rviz
Source0:        %{name}-%{version}.tar.gz

Requires:       assimp
Requires:       eigen3-devel
Requires:       mesa-libGL-devel
Requires:       mesa-libGLU-devel
Requires:       ogre-devel
Requires:       qt5-qtbase
Requires:       qt5-qtbase-gui
Requires:       ros-kinetic-geometry-msgs
Requires:       ros-kinetic-image-transport
Requires:       ros-kinetic-interactive-markers
Requires:       ros-kinetic-laser-geometry
Requires:       ros-kinetic-map-msgs
Requires:       ros-kinetic-media-export
Requires:       ros-kinetic-message-filters
Requires:       ros-kinetic-nav-msgs
Requires:       ros-kinetic-pluginlib
Requires:       ros-kinetic-python-qt-binding
Requires:       ros-kinetic-resource-retriever
Requires:       ros-kinetic-rosbag
Requires:       ros-kinetic-rosconsole
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-roslib
Requires:       ros-kinetic-rospy
Requires:       ros-kinetic-sensor-msgs
Requires:       ros-kinetic-std-msgs
Requires:       ros-kinetic-std-srvs
Requires:       ros-kinetic-tf
Requires:       ros-kinetic-urdf
Requires:       ros-kinetic-visualization-msgs
Requires:       tinyxml-devel
Requires:       urdfdom-headers-devel
Requires:       yaml-cpp-devel
BuildRequires:  assimp-devel
BuildRequires:  eigen3-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  ogre-devel
BuildRequires:  qt5-qtbase
BuildRequires:  qt5-qtbase-devel
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-cmake-modules
BuildRequires:  ros-kinetic-geometry-msgs
BuildRequires:  ros-kinetic-image-transport
BuildRequires:  ros-kinetic-interactive-markers
BuildRequires:  ros-kinetic-laser-geometry
BuildRequires:  ros-kinetic-map-msgs
BuildRequires:  ros-kinetic-message-filters
BuildRequires:  ros-kinetic-nav-msgs
BuildRequires:  ros-kinetic-pluginlib
BuildRequires:  ros-kinetic-python-qt-binding
BuildRequires:  ros-kinetic-resource-retriever
BuildRequires:  ros-kinetic-rosbag
BuildRequires:  ros-kinetic-rosconsole
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-roslib
BuildRequires:  ros-kinetic-rospy
BuildRequires:  ros-kinetic-sensor-msgs
BuildRequires:  ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-std-srvs
BuildRequires:  ros-kinetic-tf
BuildRequires:  ros-kinetic-urdf
BuildRequires:  ros-kinetic-visualization-msgs
BuildRequires:  tinyxml-devel
BuildRequires:  urdfdom-headers-devel
BuildRequires:  yaml-cpp-devel

%description
3D visualization tool for ROS.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Fri Apr 27 2018 D. Hood <dhood@osrfoundation.org> - 1.12.16-0
- Autogenerated by Bloom

* Fri Jan 05 2018 D. Hood <dhood@osrfoundation.org> - 1.12.15-0
- Autogenerated by Bloom

* Tue Dec 19 2017 D. Hood <dhood@osrfoundation.org> - 1.12.14-0
- Autogenerated by Bloom

* Mon Aug 21 2017 D. Hood <dhood@osrfoundation.org> - 1.12.13-0
- Autogenerated by Bloom

* Wed Aug 02 2017 D. Hood <dhood@osrfoundation.org> - 1.12.11-0
- Autogenerated by Bloom

* Mon Jun 05 2017 David Gossow <dgossow@gmail.com> - 1.12.10-0
- Autogenerated by Bloom

* Mon Jun 05 2017 David Gossow <dgossow@gmail.com> - 1.12.9-0
- Autogenerated by Bloom

* Thu Oct 27 2016 David Gossow <dgossow@gmail.com> - 1.12.4-0
- Autogenerated by Bloom

* Wed Oct 19 2016 David Gossow <dgossow@gmail.com> - 1.12.3-0
- Autogenerated by Bloom

* Tue Oct 18 2016 David Gossow <dgossow@gmail.com> - 1.12.2-0
- Autogenerated by Bloom

* Wed Apr 20 2016 David Gossow <dgossow@gmail.com> - 1.12.1-0
- Autogenerated by Bloom

* Mon Apr 11 2016 David Gossow <dgossow@gmail.com> - 1.12.0-0
- Autogenerated by Bloom

