%global srcname uosclient

Name:		python-%{srcname}
Version:	0.0.3
Release:	1%{?dist}
Summary:	Unipart OpenStack client tools
License:	GPLv2+
URL:		https://github.com/unipartdigital/uosclient
Source0:	%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_scm

%description
This is a set of simple tools designed to automate various common
system administration tasks within the Unipart OpenStack
infrastructure.

%package -n	python3-%{srcname}
Summary:	%{summary}
Provides:	%{srcname} = %{version}-%{release}

%{?python_provide:%python_provide python3-%{srcname}}

%description -n python3-%{srcname}
This is a set of simple tools designed to automate various common
system administration tasks within the Unipart OpenStack
infrastructure.

%prep
%autosetup

%build
%py3_build

%install
export SETUPTOOLS_SCM_PRETEND_VERSION=%{version}
%py3_install

%files -n python3-%{srcname}
%doc README.md
%license COPYING
%{python3_sitelib}/%{srcname}/
%{python3_sitelib}/%{srcname}-%{version}-*.egg-info/

%changelog
