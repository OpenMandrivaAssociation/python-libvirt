%define _disable_ld_no_undefined 1
%define rname libvirt-python

Summary:	The libvirt virtualization API python2 binding
Name:		python-libvirt
Version:	4.10.0
Release:	1
License:	LGPLv2+
Group:		Development/Python
URL:		http://libvirt.org
Source0:	http://libvirt.org/sources/python/libvirt-python-%{version}.tar.gz
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
CFLAGS="%{optflags}" LDFLAGS="-lvirt" python2} setup.py build

CFLAGS="%{optflags}" LDFLAGS="-lvirt" python3} setup.py build

%install
python setup.py install --skip-build --root=%{buildroot}

python setup.py install --skip-build --root=%{buildroot}

rm -f %{buildroot}%{_libdir}/python*/site-packages/*egg-info
rm -Rf %{buildroot}%{py3_platsitedir}/__pycache__

%files
%doc ChangeLog AUTHORS NEWS README COPYING COPYING.LESSER examples/
%{py3_platsitedir}/libvirt.py*
%{py3_platsitedir}/__pycache__/*
%{py3_platsitedir}/libvirt_qemu.py*
%{py3_platsitedir}/libvirt_lxc.py*
%{py3_platsitedir}/libvirtmod*
%{py3_platsitedir}/libvirtaio.py

%files -n python2-libvirt
%doc ChangeLog AUTHORS NEWS README COPYING COPYING.LESSER examples/
%{py_platsitedir}/libvirt.py*
%{py_platsitedir}/libvirt_qemu.py*
%{py_platsitedir}/libvirt_lxc.py*
%{py_platsitedir}/libvirtmod*
