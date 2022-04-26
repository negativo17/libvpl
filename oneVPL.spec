Name:           oneVPL
Version:        2022.1.1
Release:        1%{?dist}
Summary:        oneAPI Video Processing Library
License:        MIT
URL:            https://www.intel.com/content/www/us/en/developer/tools/oneapi/onevpl.html
ExclusiveArch:  x86_64

Source0:        https://github.com/oneapi-src/oneVPL/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  devtoolset-9-gcc-c++
BuildRequires:  pkgconfig(libdrm) >= 2.4.91
BuildRequires:  pkgconfig(libva) >= 1.2
BuildRequires:  pkgconfig(libva-drm) >= 1.2
BuildRequires:  pkgconfig(libva-x11) >= 1.10.0
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(wayland-client)

Requires:       intel-mediasdk
Requires:       oneVPL-cpu
Requires:       oneVPL-intel-gpu

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

%package        samples
Summary:        Sample programs and source code for %{name}
Requires:       %{name}-devel%{?_isa} = %{version}-%{release}

%description    samples
This package contains sample programs and applications that use %{name}.

%prep
%autosetup -p1

%build
mkdir build
pushd build

. /opt/rh/devtoolset-9/enable
%cmake3 -DBUILD_PYTHON_BINDING:BOOL=OFF ..
%cmake3_build

popd

%install
pushd build

%cmake3_install

popd

find %{buildroot} -name '*.la' -delete

# Let RPM pick up documents in the files section
rm -fr %{buildroot}%{_datadir}/vpl/licensing

%{?ldconfig_scriptlets}

%files
%license LICENSE
%doc README.md CONTRIBUTING.md third-party-programs.txt
%dir %{_prefix}/etc/vpl
%{_prefix}/etc/vpl/vars.sh
%dir %{_prefix}/etc/modulefiles
%{_prefix}/etc/modulefiles/vpl
%dir %{_libdir}/vpl
%{_libdir}/vpl/libvpl_wayland.so
%{_libdir}/libvpl.so.2
%{_libdir}/libvpl.so.2.7

%files devel
%{_includedir}/vpl
%dir %{_libdir}/cmake/vpl
%{_libdir}/cmake/vpl/VPLConfig.cmake
%{_libdir}/cmake/vpl/VPLConfigVersion.cmake
%{_libdir}/libvpl.so
%{_libdir}/pkgconfig/vpl.pc

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
%dir %{_datadir}/vpl
%{_datadir}/vpl/examples

%changelog
* Tue Apr 26 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.1-1
- Update to 2022.1.1.
- Require implementations (at least one must be installed)

* Sat Mar 19 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.0-1
- Update to 2022.1.0.

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
