%if 0%{?fedora}
%global _with_python3 1
%endif

%if 0%{?rhel} && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python2_sitearch: %global python2_sitearch %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:       python-vcrpy
Version:    1.0.2
Release:    1%{?dist}
Summary:    Simplify and speed up testing HTTP by recording all HTTP interactions

Group:      Development/Languages
License:    MIT
URL:        https://github.com/kevin1024/vcrpy
Source0:    https://pypi.python.org/packages/source/v/vcrpy/vcrpy-%{version}.tar.gz

BuildRequires:  python2-devel python-setuptools
Requires:   PyYAML python-six python-contextdecorator
BuildArch:      noarch

%description
Simplify and speed up testing HTTP by recording all HTTP interactions and saving
them to "cassette" files, which are yaml files containing the contents of your 
requests and responses.


%if 0%{?_with_python3}
%package -n python3-vcrpy
Summary: VMware vSphere Python SDK 
BuildRequires:  python3-devel python3-setuptools
Requires: python3-PyYAML python3-six python3-contextdecorator

%description -n python3-vcrpy
Simplify and speed up testing HTTP by recording all HTTP interactions and saving
them to "cassette" files, which are yaml files containing the contents of your 
requests and responses.
%endif


%prep
%setup -q


%build
%configure
make %{?_smp_mflags}


%install
make install DESTDIR=%{buildroot}


%files
%doc



%changelog

