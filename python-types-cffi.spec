%define module types_cffi

Name:		python-types-cffi
Version:	1.17.0.20250915
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/t/types-cffi/%{module}-%{version}.tar.gz
Summary:	Typing stubs for cffi
URL:		https://pypi.org/project/types-cffi/
License:	Apache-2.0
Group:		Development/Python
BuildSystem:	python
BuildArch:	noarch

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(setuptools)
Requires:	python%{pyver}dist(types-setuptools)
Provides:	python%{pyver}dist(%{module})

%description
Typing stubs for cffi

%files
%{py_sitedir}/_cffi_backend-stubs/*
%{py_sitedir}/cffi-stubs/*
%{py_sitedir}/%{module}-%{version}.dist-info
%license LICENSE
%doc README.md
