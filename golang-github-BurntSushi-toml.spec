%global debug_package   %{nil}
%global import_path     github.com/BurntSushi/toml
%global gopath          %{_datadir}/gocode
%global commit          bd2bdf7f18f849530ef7a1c29a4290217cab32a1
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-BurntSushi-toml
Version:        0
Release:        0.git%{shortcommit}%{?dist}
Summary:        TOML parser and encoder for Go with reflection
License:        BSD
URL:            https://github.com/BurntSushi/toml
Source0:        https://github.com/BurntSushi/toml/archive/%{commit}/%{name}-%{commit}.tar.gz
BuildArch:      noarch

%description
%{summary}

%package devel
BuildRequires:  golang
Requires:       golang
Summary:        TOML parser and encoder for Go with reflection
Provides:       golang(%{import_path}) = %{version}-%{release}

%description devel
%{summary}

%prep
%setup -n %{name}-%{commit}

%build

%install
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -av *.go %{buildroot}/%{gopath}/src/%{import_path}

%check
GOPATH=%{gopath}:%{buildroot}/%{gopath} go test %{import_path}

%files devel
%defattr(-,root,root,-)
%doc COPYING README.md
%dir %attr(755,root,root) %{gopath}
%dir %attr(755,root,root) %{gopath}/src
%dir %attr(755,root,root) %{gopath}/src/github.com
%dir %attr(755,root,root) %{gopath}/src/github.com/BurntSushi
%dir %attr(755,root,root) %{gopath}/src/github.com/BurntSushi/toml
%{gopath}/src/%{import_path}/*.go

%changelog
* Thu Jul 17 2014 Colin Walters <walters@verbum.org>
- Initial package
