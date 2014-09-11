%global debug_package   %{nil}
%global import_path     github.com/BurntSushi/toml
%global commit          bd2bdf7f18f849530ef7a1c29a4290217cab32a1
%global shortcommit     %(c=%{commit}; echo ${c:0:7})

Name:           golang-github-BurntSushi-toml
Version:        0
Release:        0.0.git%{shortcommit}%{?dist}
Summary:        TOML parser and encoder for Go with reflection
License:        BSD
URL:            https://github.com/BurntSushi/toml
Source0:        https://github.com/BurntSushi/toml/archive/%{commit}/%{name}-%{commit}.tar.gz
ExclusiveArch:  %{go_arches} noarch
Provides:       tomlv = %{version}-%{release}

%description
%{summary}

%package devel
BuildRequires:  golang >= 1.2.1-3
Requires:       golang >= 1.2.1-3
Summary:        TOML parser and encoder for Go with reflection
Provides:       golang(%{import_path}) = %{version}-%{release}
BuildArch:      noarch

%description devel
%{summary}

%prep
%setup -q -n %{name}-%{commit}

%build
mkdir -p _build/src/github.com/BurntSushi
ln -sf $(pwd) _build/src/github.com/BurntSushi/toml
export GOPATH=$(pwd)/_build:%{gopath}
cd cmd/tomlv
go build .

%install
install -d %{buildroot}/%{_bindir}
install -p -m 755 ./cmd/tomlv/tomlv %{buildroot}%{_bindir}/tomlv
install -d %{buildroot}/%{gopath}/src/%{import_path}
cp -pav *.go %{buildroot}/%{gopath}/src/%{import_path}

%check
GOPATH=%{buildroot}/%{gopath}:%{gopath} go test %{import_path}

%files
%defattr(-,root,root,-)
%{_bindir}/tomlv

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
