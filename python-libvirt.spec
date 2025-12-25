%define _disable_ld_no_undefined 1
%define oname libvirt_python
%define module libvirt

Summary:	The libvirt virtualization API python binding
Name:		python-libvirt
Version:	11.10.0
Release:	1
License:	LGPL-2.1-or-later
Group:		Development/Python
URL:		https://libvirt.org
Source0:	https://download.libvirt.org/python/%{oname}-%{version}.tar.gz
BuildSystem:	python
BuildRequires:	libvirt-devel >= 1.2.0
BuildRequires:	libvirt-utils >= 1.2.0
BuildRequires:	pkgconfig(python)
BuildRequires:  python%{pyver}dist(lxml)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:  python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

Obsoletes:    python2-libvirt

%description
The libvirt-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libvirt library to use the virtualization capabilities
of recent versions of Linux (and other OSes).

%prep
%autosetup -n %{oname}-%{version} -p1

# Unset execute bit for example scripts; it can introduce spurious
# RPM dependencies
find examples -type f -exec chmod 0644 \{\} \;

%build
export CFLAGS="%{optflags}"
export LDFLAGS="-lvirt -lpython%{pyver}"
%py_build

%install
%py_install

%files
%doc ChangeLog AUTHORS README examples/
%license COPYING
%{python_sitearch}/%{module}.py*
%{python_sitearch}/%{module}_qemu.py*
%{python_sitearch}/%{module}_lxc.py*
%{python_sitearch}/%{module}mod*
%{python_sitearch}/%{module}aio.py
%{python_sitearch}/%{oname}-%{version}.dist-info/
%{python_sitearch}/__pycache__/%{module}*
