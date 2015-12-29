Name:       libbmp
Summary:    A library of functions for encoding BMP image format files
Version:    0.1.3
Release:    1
Group:      System/Libraries
License:    LGPL-2.1
URL:        https://code.google.com/p/libbmp/
Source0:    https://libbmp.googlecode.com/libbmp-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
libbmp is a simple, cross-platform, open source (revised LGPL-2.1) C library designed for easily 
reading, writing, and modifying Windows bitmap (BMP) image files. 
The library is oriented towards the novice programmer with little formal experience, 
but it is sufficiently capable for anybody who desires to do I/O and pixel operations 
on uncompressed 1, 4, 8, 16, 24, and 32 bpp (bits per pixel) BMP files. 

%package devel
Summary:    A library of functions for encoding BMP image format files (DEV)
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
A library of functions for encoding BMP image format files - Development files.

%prep
%setup -q -n %{name}-%{version}

%build
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
rm -rf $RPM_BUILD_ROOT/usr/share/man

#license
mkdir -p %{buildroot}/%{_datadir}/license
cp -rf %{_builddir}/%{name}-%{version}/COPYING %{buildroot}/%{_datadir}/license/%{name}

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest libbmp.manifest
%defattr(-,root,root,-)
%{_libdir}/libbmp*.so.*
%{_bindir}/*
%{_datadir}/license/%{name}

%files devel
%manifest libbmp.manifest
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/libbmp*.so
%{_libdir}/pkgconfig/*

