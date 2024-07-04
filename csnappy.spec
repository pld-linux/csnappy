Summary:	Google Snappy in C
Summary(pl.UTF-8):	Implementacja Google Snappy w C
Name:		csnappy
Version:	0
%define	gitref	6c10c305e8dde193546e6b33cf8a785d5dc123e2
%define	snap	20200805
Release:	0.%{snap}.1
License:	BSD
Group:		Libraries
Source0:	https://github.com/zeevt/csnappy/archive/%{gitref}/%{name}-%{snap}.tar.gz
# Source0-md5:	c6fda5bd51eaa2af6b2c54787c692a4a
URL:		https://github.com/zeevt/csnappy
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains an ANSI C port of Google Snappy compression
library. Google Snappy is a compression library designed for speed
rather than compression ratios.

%description -l pl.UTF-8
Ten pakiet zawiera port ANSI C biblioteki kompresji Google Snappy.
Google Snappy to biblioteka kompresji zaprojektowana z myślą bardziej
o szybkości niż współczynniku kompresji.

%package devel
Summary:	Header files for csnappy library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki csnappy
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for csnappy library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki csnappy.

%prep
%setup -q -n %{name}-%{gitref}

%build
%{__make} libcsnappy.so \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmcppflags} -Wall -pedantic %{!?debug:-DNDEBUG}" \
	LDFLAGS="%{rpmldflags} -Wl,--no-undefined"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_libdir}/libcsnappy.so

%files devel
%defattr(644,root,root,755)
%{_includedir}/csnappy.h
