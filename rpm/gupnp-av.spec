Name:          gupnp-av
Version:       0.12.5
Release:       1%{?dist}
Summary:       A collection of helpers for building UPnP AV applications

Group:         System Environment/Libraries
License:       LGPLv2+
URL:           http://www.gupnp.org/
Source0:       http://download.gnome.org/sources/gupnp-av/0.12/%{name}-%{version}.tar.xz

BuildRequires: glib2-devel
BuildRequires: gssdp-devel >= 0.14.0
BuildRequires: gupnp-devel >= 0.20.0
BuildRequires: libxml2-devel
BuildRequires: libsoup-devel
BuildRequires: gobject-introspection-devel >= 1.36.0
BuildRequires: vala-devel
BuildRequires: vala-tools

%description
GUPnP is an object-oriented open source framework for creating UPnP
devices and control points, written in C using GObject and libsoup.
The GUPnP API is intended to be easy to use, efficient and flexible.

GUPnP-AV is a collection of helpers for building AV (audio/video) 
applications using GUPnP.

%package devel
Summary: Development package for %{name}
Group: Development/Libraries
Requires: %{name} = %{version}-%{release}
Requires: gssdp-devel
Requires: gupnp-devel
Requires: pkgconfig

%description devel
Files for development with %{name}.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
%autogen --disable-static
make %{?_smp_mflags} V=1

%install
make install DESTDIR=%{buildroot}

#Remove libtool archives.
find %{buildroot} -name '*.la' -exec rm -f {} ';'

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%{_libdir}/libgupnp-av-1.0.so.*
%{_libdir}/girepository-1.0/GUPnPAV-1.0.typelib
%{_datadir}/%{name}

%files devel
%{_includedir}/gupnp-av-1.0
%{_libdir}/pkgconfig/gupnp-av-1.0.pc
%{_libdir}/libgupnp-av-1.0.so
%{_datadir}/gir-1.0/GUPnPAV-1.0.gir
%{_datadir}/vala/vapi/*
