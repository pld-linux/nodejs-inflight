#
# Conditional build:
%bcond_with	tests		# build with tests

%define		pkg	inflight
Summary:	Node.js inflight
Name:		nodejs-%{pkg}
Version:	1.0.4
Release:	1
License:	ISC
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/inflight/-/inflight-%{version}.tgz
# Source0-md5:	7643dfe43b25ca289c11ae5515afc3eb
URL:		https://github.com/isaacs/inflight
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	nodejs-once
BuildRequires:	nodejs-packaging
BuildRequires:	nodejs-tap
BuildRequires:	nodejs-wrappy
%endif
Requires:	nodejs
Requires:	nodejs-once < 2.0.0
Requires:	nodejs-once >= 1.3.0
Requires:	nodejs-wrappy < 2
Requires:	nodejs-wrappy >= 1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Add callbacks to requests in flight to avoid async duplication

%prep
%setup -qc
mv package/* .

%build
%if %{with tests}
tap test.js
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -p %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{nodejs_libdir}/%{pkg}
