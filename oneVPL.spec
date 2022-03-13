Name:           oneVPL
Version:        2022.0.6
Release:        1%{?dist}
Summary:        oneAPI Video Processing Library
License:        MIT
URL:            https://www.intel.com/content/www/us/en/developer/tools/oneapi/onevpl.html
ExclusiveArch:  x86_64

Source0:        https://github.com/oneapi-src/oneVPL/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libdrm) >= 2.4.91
BuildRequires:  pkgconfig(libva) >= 1.2
BuildRequires:  pkgconfig(libva-drm) >= 1.2
BuildRequires:  pkgconfig(libva-x11) >= 1.10.0
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  python3dist(pybind11)
BuildRequires:  python3-devel

%description
The oneAPI Video Processing Library (oneVPL) provides a single video processing
API for encode, decode, and video processing that works across a wide range of
accelerators.

The base package is limited to the dispatcher and samples. To use oneVPL for
video processing you need to install at least one implementation. Current
implementations:

- oneVPL-cpu for use on CPU
- oneVPL-intel-gpu for use on Intel Xe graphics and newer
- Media SDK for use on legacy Intel graphics

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package -n python3-%{name}
Summary:    Python3 interface to %{name}

%description -n python3-%{name}
This package contains python3 interfaces to %{name}.

%package        samples
Summary:        Sample programs and source code for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    samples
This package contains sample programs and applications that use %{name}.

%prep
%autosetup -p1

%build
%cmake \
    -DBUILD_PYTHON_BINDING:BOOL=ON \
    -DPYTHON_INSTALL_DIR:STRING=%{python3_sitearch}
%cmake_build

%install
%cmake_install

find %{buildroot} -name '*.la' -delete

# Let RPM pick up documents in the files section
rm -fr %{buildroot}%{_docdir}

%{?ldconfig_scriptlets}

%files
%license LICENSE
%doc README.md CONTRIBUTING.md third-party-programs.txt
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/env
%{_datadir}/%{name}/modulefiles
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/libvpl_wayland.so
%{_libdir}/libvpl.so.2
%{_libdir}/libvpl.so.2.6

%files devel
%{_includedir}/vpl
%dir %{_libdir}/cmake/vpl
%{_libdir}/cmake/vpl/VPLConfig.cmake
%{_libdir}/cmake/vpl/VPLConfigVersion.cmake
%{_libdir}/libvpl.so
%{_libdir}/pkgconfig/vpl.pc

%files -n python3-%{name}
%{python3_sitearch}/*

%files samples
%{_bindir}/decvpp_tool
%{_bindir}/hello-decode
%{_bindir}/hello-encode
%{_bindir}/hello-vpp
%{_bindir}/sample_decode
%{_bindir}/sample_encode
%{_bindir}/sample_multi_transcode
%{_bindir}/sample_vpp
%{_bindir}/vpl-inspect
%{_datadir}/%{name}/examples

%changelog
* Sun Mar 13 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.6-1
- Update to 2022.0.6.

* Wed Mar 02 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.5-2
- Rebuild for updated libva.

* Wed Mar 02 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.5-1
- Update to 2022.0.5.

* Tue Feb 08 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.4-1
- Update to 2022.0.4.

* Mon Feb 07 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.0-2
- Enable Python binding.

* Sat Feb 05 2022 Simone Caronni <negativo17@gmail.com> - 2022.0.0-1
- First build.
