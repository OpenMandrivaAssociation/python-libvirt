%define _disable_ld_no_undefined 1
%define rname libvirt-python

Summary:	The libvirt virtualization API python2 binding
Name:		python-libvirt
Version:	1.2.3
Release:	2
License:	LGPLv2+
Group:		Development/Python
URL:		http://libvirt.org
Source0:	http://libvirt.org/sources/python/%{rname}-%{version}.tar.gz
BuildRequires:	libvirt-devel >= 1.2.0
BuildRequires:	libvirt-utils >= 1.2.0
BuildRequires:	python-devel
BuildRequires:	python3-devel

%description
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%package -n	python3-libvirt
Summary:	The libvirt virtualization API python3 binding
Group:		Development/Python

%description -n	python3-libvirt
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%prep

%setup -q -n %{rname}-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-lvirt" %{__python} setup.py build

CFLAGS="$RPM_OPT_FLAGS" LDFLAGS="-lpython3.3 -lvirt" %{__python3} setup.py build

%install
%{__python} setup.py install --skip-build --root=%{buildroot}

%{__python3} setup.py install --skip-build --root=%{buildroot}

rm -f %{buildroot}%{_libdir}/python*/site-packages/*egg-info

%files
%doc ChangeLog AUTHORS NEWS README COPYING COPYING.LESSER examples/
%{python_sitearch}/libvirt.py*
%{python_sitearch}/libvirt_qemu.py*
%{python_sitearch}/libvirt_lxc.py*
%{python_sitearch}/libvirtmod*

%files -n python3-libvirt
%doc ChangeLog AUTHORS NEWS README COPYING COPYING.LESSER examples/
%{python3_sitearch}/libvirt.py*
%{python3_sitearch}/libvirt_qemu.py*
%{python3_sitearch}/libvirt_lxc.py*
%{python3_sitearch}/libvirtmod*


