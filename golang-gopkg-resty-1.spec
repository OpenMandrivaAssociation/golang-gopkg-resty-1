%global goipath         gopkg.in/resty.v1
%global forgeurl        https://github.com/go-resty/resty
Version:                1.10.3
%gometa

Name:           %{goname}
Release:        1%{?dist}
Summary:        Simple HTTP and REST client library for Go
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}
BuildRequires:  golang(golang.org/x/net/publicsuffix)


%description
%{summary}.


%package devel
Summary:        %{summary}
BuildArch:      noarch


%description devel
%{summary}.

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.


%prep
%forgeautosetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Wed Dec 05 2018 Carl George <carl@george.computer> - 1.10.3-1
- Latest upstream

* Wed Dec 05 2018 Carl George <carl@george.computer> - 1.10.2-2
- Add patch0 to fix panic on i686

* Tue Nov 27 2018 Carl George <carl@george.computer> - 1.10.2-1
- Initial package
