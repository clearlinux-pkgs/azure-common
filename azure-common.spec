#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : azure-common
Version  : 1.1.24
Release  : 16
URL      : https://files.pythonhosted.org/packages/f9/01/1466ec85113b59f9c0bce9d53dc3861d8671bcde49e408c4f0d1f375e13f/azure-common-1.1.24.zip
Source0  : https://files.pythonhosted.org/packages/f9/01/1466ec85113b59f9c0bce9d53dc3861d8671bcde49e408c4f0d1f375e13f/azure-common-1.1.24.zip
Summary  : Microsoft Azure Client Library for Python (Common)
Group    : Development/Tools
License  : MIT
Requires: azure-common-python = %{version}-%{release}
Requires: azure-common-python3 = %{version}-%{release}
Requires: azure-nspkg
BuildRequires : azure-nspkg
BuildRequires : buildreq-distutils3

%description
==============================
        
        This is the Microsoft Azure common code.
        
        This package provides shared code by the Azure packages.

%package python
Summary: python components for the azure-common package.
Group: Default
Requires: azure-common-python3 = %{version}-%{release}

%description python
python components for the azure-common package.


%package python3
Summary: python3 components for the azure-common package.
Group: Default
Requires: python3-core
Provides: pypi(azure_common)

%description python3
python3 components for the azure-common package.


%prep
%setup -q -n azure-common-1.1.24
cd %{_builddir}/azure-common-1.1.24

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583531346
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
