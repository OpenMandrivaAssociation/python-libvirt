%define _disable_ld_no_undefined 1
%define rname libvirt-python

Summary:	The libvirt virtualization API python binding
Name:		python-libvirt
Version:	4.9.0
Release:	2
License:	LGPLv2+
Group:		Development/Python
URL:		http://libvirt.org
Source0:	http://libvirt.org/sources/python/%{rname}-%{version}.tar.gz
BuildRequires:	libvirt-devel >= 1.2.0
BuildRequires:	libvirt-utils >= 1.2.0
BuildRequires:	python2-devel
BuildRequires:	python3-devel

%description
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%package -n	python2-libvirt
Summary:	The libvirt virtualization API python2 binding
Group:		Development/Python

%description -n	python2-libvirt
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%prep

%setup -q -n %{rname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-lvirt" %{__python2} setup.py build

CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-lvirt" %{__python3} setup.py build

%install
%{__python} setup.py install --skip-build --root=%{buildroot}

%{__python2} setup.py install --skip-build --root=%{buildroot}

rm -f %{buildroot}%{_libdir}/python*/site-packages/*egg-info
rm -Rf %{buildroot}%{python3_sitearch}/__pycache__

%files
%doc ChangeLog AUTHORS NEWS README COPYING COPYING.LESSER examples/
%{python3_sitearch}/libvirt.py*
%{python3_sitearch}/__pycache__/*
%{python3_sitearch}/libvirt_qemu.py*
%{python3_sitearch}/libvirt_lxc.py*
%{python3_sitearch}/libvirtmod*
%{python3_sitearch}/libvirtaio.py

%files -n python2-libvirt
%doc ChangeLog AUTHORS NEWS README COPYING COPYING.LESSER examples/
%{python2_sitearch}/libvirt.py*
%{python2_sitearch}/libvirt_qemu.py*
%{python2_sitearch}/libvirt_lxc.py*
%{python2_sitearch}/libvirtmod*


