Name:       libbmp
Summary:    A library of functions for manipulating BMP image format files
Version:    0.1.3
Release:    1
Group:      System/Libraries
License:    LGPL
URL:        https://code.google.com/p/libbmp/
Source0:    https://libbmp.googlecode.com/libbmp-%{version}.tar.bz2
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
libbmp is a simple, cross-platform, open source (revised LGPL) C library designed for easily 
reading, writing, and modifying Windows bitmap (BMP) image files. 
The library is oriented towards the novice programmer with little formal experience, 
but it is sufficiently capable for anybody who desires to do I/O and pixel operations 
on uncompressed 1, 4, 8, 16, 24, and 32 bpp (bits per pixel) BMP files. 


%prep
%setup -q -n %{name}-%{version}

%build

%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install 
rm -rf $RPM_BUILD_ROOT/usr/share/man

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%manifest libbmp.manifest
%{_libdir}/libbmp*.so.*
%{_bindir}/*
%{_includedir}/*
%{_libdir}/libbmp*.so
%{_libdir}/pkgconfig/*

