%define _disable_ld_no_undefined 1
%define rname libvirt-python

Summary:	The libvirt virtualization API python binding
Name:		python-libvirt
Version:	6.1.0
Release:	1
License:	LGPLv2+
Group:		Development/Python
URL:		http://libvirt.org
Source0:	http://libvirt.org/sources/python/%{rname}-%{version}.tar.gz
BuildRequires:	libvirt-devel >= 1.2.0
BuildRequires:	libvirt-utils >= 1.2.0
BuildRequires:	python-devel

Obsoletes:    python2-libvirt

%description
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%prep

%setup -q -n %{rname}-%{version}

%build
CFLAGS="%{optflags}" LDFLAGS="-lvirt" %{__python3} setup.py build

%install
%{__python} setup.py install --skip-build --root=%{buildroot}

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


