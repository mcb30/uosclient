%global srcname uosclient

%define with_py2 1
%define with_py3 1

%if 0%{?rhel}
%define with_py3 0
%endif

Name:		python-%{srcname}
Version:	0.0.5
Release:	1%{?dist}
Summary:	Unipart OpenStack client tools
License:	GPLv2+
URL:		https://github.com/unipartdigital/uosclient
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
%if 0%{?with_py2}
BuildRequires:	python2-devel
BuildRequires:	python2-setuptools
BuildRequires:	python2-setuptools_scm
%endif
%if 0%{?with_py3}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm
%endif

%description
This is a set of simple tools designed to automate various common
system administration tasks within the Unipart OpenStack
infrastructure.

%if 0%{?with_py2}
%package -n	python2-%{srcname}
Summary:	%{summary}
%if ! 0%{?with_py3}
Provides:	%{srcname} = %{version}-%{release}
%endif
%{?python_provide:%python_provide python2-%{srcname}}

%description -n python2-%{srcname}
This is a set of simple tools designed to automate various common
system administration tasks within the Unipart OpenStack
infrastructure.
%endif

%if 0%{?with_py3}
%package -n	python3-%{srcname}
Summary:	%{summary}
Provides:	%{srcname} = %{version}-%{release}
%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This is a set of simple tools designed to automate various common
system administration tasks within the Unipart OpenStack
infrastructure.
%endif

%prep
%autosetup

%build
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%if 0%{?with_py2}
%py2_build
%endif
%if 0%{?with_py3}
%py3_build
%endif

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%if 0%{?with_py2}
%py2_install
%endif
%if 0%{?with_py3}
%py3_install
%endif

%if 0%{?with_py2}
%files -n python2-%{srcname}
%doc README.md
%license COPYING
%{python2_sitelib}/%{srcname}/
%{python2_sitelib}/%{srcname}-%{version}-*.egg-info/
%endif

%if 0%{?with_py3}
%files -n python3-%{srcname}
%doc README.md
%license COPYING
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info/
%endif

%changelog
* Tue Feb 04 2020 Michael Brown <mbrown@fensystems.co.uk> 0.0.5-1
- build: Fix building of RPM from a tarball

* Tue Feb 04 2020 Michael Brown <mbrown@fensystems.co.uk> 0.0.4-1
- First package built with tito
