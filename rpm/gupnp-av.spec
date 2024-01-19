Name:          gupnp-av
Version:       0.14.1
Release:       1
Summary:       A collection of helpers for building UPnP AV applications
License:       LGPLv2+
URL:           http://www.gupnp.org/
Source0:       %{name}-%{version}.tar.xz
Patch1:        0001-Remove-deprecates-xmlRecoverMemory.patch
Patch2:        0002-xml-Fix-compatibility-with-libxml2-2.12.x.patch
BuildRequires: gobject-introspection-devel
BuildRequires: meson
BuildRequires: vala-devel
BuildRequires: vala-tools
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(libxml-2.0)

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-AV is a collection of helpers for building AV (audio/video) 
applications using GUPnP.

%package devel
Summary: Development package for %{name}
Requires: %{name} = %{version}-%{release}
Requires: gupnp-devel
Requires: pkgconfig

%description devel
Files for development with %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%meson -Dgtk_doc=false
%meson_build

%install
%meson_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
%{_libdir}/libgupnp-av-1.0.so.*
%{_libdir}/girepository-1.0/GUPnPAV-1.0.typelib
%{_datadir}/%{name}

%files devel
%{_includedir}/gupnp-av-1.0
%{_libdir}/pkgconfig/gupnp-av-1.0.pc
%{_libdir}/libgupnp-av-1.0.so
%{_datadir}/gir-1.0/GUPnPAV-1.0.gir
%{_datadir}/vala/vapi/*
