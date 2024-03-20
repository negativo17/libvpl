Name:           libvpl
Epoch:          1
Version:        2.10.2
Release:        1%{?dist}
Summary:        oneAPI Video Processing Library
License:        MIT
URL:            https://intel.github.io/libvpl/latest/index.html
ExclusiveArch:  x86_64

Source0:        https://github.com/intel/libvpl/archive/v%{version}/%{name}-%{version}.tar.gz
Patch0:         %{name}-system-analyzer.patch

BuildRequires:  cmake
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(libdrm) >= 2.4.91
BuildRequires:  pkgconfig(libva) >= 1.2
BuildRequires:  pkgconfig(libva-drm) >= 1.2
BuildRequires:  pkgconfig(libva-x11) >= 1.10.0
BuildRequires:  pkgconfig(pciaccess)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(wayland-protocols) >= 1.15
BuildRequires:  pkgconfig(x11)

Recommends:     intel-mediasdk
Recommends:     oneVPL-cpu
Recommends:     oneVPL-intel-gpu

Obsoletes:      oneVPL <= 2023.4.0
Provides:       oneVPL%{?_isa} == %{?epoch:%{epoch}:}%{version}-%{release}

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
Requires:       %{name}%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:      oneVPL-devel <= 2023.4.0
Provides:       oneVPL-devel%{?_isa} == %{?epoch:%{epoch}:}%{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for developing
applications that use %{name}.

%package        samples
Summary:        Sample programs and source code for %{name}
Requires:       %{name}-devel%{?_isa} = %{?epoch:%{epoch}:}%{version}-%{release}

Obsoletes:      oneVPL-samples <= 2023.4.0
Provides:       oneVPL-samples%{?_isa} == %{?epoch:%{epoch}:}%{version}-%{release}

%description    samples
This package contains sample programs and applications that use %{name}.

%prep
%autosetup -p1 -n libvpl-%{version}

%build
%cmake -DCMAKE_INSTALL_SYSCONFDIR=%{_sysconfdir}
%cmake_build

%install
%cmake_install

# Let RPM pick up documents in the files section
rm -fr %{buildroot}%{_datadir}/vpl/licensing

%files
%license LICENSE
%doc README.md CONTRIBUTING.md third-party-programs.txt
%dir %{_sysconfdir}/vpl
%{_sysconfdir}/vpl/vars.sh
%{_libdir}/libvpl.so.2
%{_libdir}/libvpl.so.2.10
%{_bindir}/system_analyzer
%dir %{_libdir}/vpl
%{_libdir}/vpl/libvpl_wayland.so

%files devel
%{_includedir}/vpl
%dir %{_libdir}/cmake/vpl
%{_libdir}/cmake/vpl/VPLConfig.cmake
%{_libdir}/cmake/vpl/VPLConfigVersion.cmake
%{_libdir}/libvpl.so
%{_libdir}/pkgconfig/vpl.pc

%files samples
%{_bindir}/sample_decode
%{_bindir}/sample_encode
%{_bindir}/sample_multi_transcode
%{_bindir}/sample_vpp
%{_bindir}/val-surface-sharing
%{_bindir}/vpl-import-export
%{_bindir}/vpl-inspect
%dir %{_datadir}/vpl
%{_datadir}/vpl/examples

%changelog
* Wed Mar 20 2024 Simone Caronni <negativo17@gmail.com> - 1:2.10.2-1
- Update to 2.10.2.

* Thu Jan 18 2024 Simone Caronni <negativo17@gmail.com> - 1:2.10.1-1
- Rename to libvpl with new versioning scheme.

* Wed Dec 13 2023 Simone Caronni <negativo17@gmail.com> - 2023.4.0-1
- Update to 2023.4.0.

* Tue Aug 08 2023 Simone Caronni <negativo17@gmail.com> - 2023.3.1-1
- Update to 2023.3.1.

* Fri Jul 14 2023 Simone Caronni <negativo17@gmail.com> - 2023.3.0-1
- Update to 2023.3.0.

* Wed Apr 19 2023 Simone Caronni <negativo17@gmail.com> - 2023.2.1-1
- Update to 2023.2.1.

* Thu Apr 13 2023 Simone Caronni <negativo17@gmail.com> - 2023.2.0-1
- Update to 2023.2.0.
- Fix install path for config files (#2177912).

* Tue Mar 07 2023 Simone Caronni <negativo17@gmail.com> - 2023.1.3-1
- Update to 2023.1.3.

* Mon Jan 30 2023 Simone Caronni <negativo17@gmail.com> - 2023.1.2-1
- Update to 2023.1.2.

* Thu Jan 26 2023 Simone Caronni <negativo17@gmail.com> - 2023.1.1-1
- Update to 2023.1.1.

* Fri Nov 18 2022 Simone Caronni <negativo17@gmail.com> - 2023.1.0-1
- Update to 2023.1.0.
- Drop python preview.

* Mon Oct 24 2022 Simone Caronni <negativo17@gmail.com> - 2022.2.5-1
- Update to 2022.2.5.

* Tue Oct 04 2022 Simone Caronni <negativo17@gmail.com> - 2022.2.4-1
- Update to 2022.2.4.

* Wed Aug 24 2022 Simone Caronni <negativo17@gmail.com> - 2022.2.2-1
- Update to 2022.2.2.

* Tue Aug 09 2022 Simone Caronni <negativo17@gmail.com> - 2022.2.1-1
- Update to 2022.2.1.

* Fri Jul 22 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.6-2
- Patch system_analyzer so it works without devel subpackage installed.

* Thu Jul 21 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.6-1
- Update to 2022.1.6.

* Thu Jun 16 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.5-1
- Update to 2022.1.5.

* Tue May 31 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.4-1
- Update to 2022.1.4.

* Wed May 25 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.3-1
- Update to 2022.1.3.

* Mon May 02 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.2-1
- Update to 2022.1.2.

* Tue Apr 26 2022 Simone Caronni <negativo17@gmail.com> - 2022.1.1-1
- Update to 2022.1.1.
- Recommend implementations (at least one must be installed).

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
