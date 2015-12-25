Summary:	lttoolbox-based translation modules generator
Summary(pl.UTF-8):	Oparty na pakiecie lttoolbox generator modułów tłumaczących
Name:		apertium
Version:	3.4.0
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	http://downloads.sourceforge.net/apertium/%{name}-%{version}.tar.gz
# Source0-md5:	5aa356d4840d6ffb1490a3b6639930bd
Patch0:		%{name}-opt.patch
URL:		http://www.apertium.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	bash
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 1:2.6.17
BuildRequires:	libxml2-progs >= 1:2.6.17
BuildRequires:	libxslt-progs
BuildRequires:	lttoolbox-devel >= 3.3.1
BuildRequires:	pcre-cxx-devel >= 6.4
BuildRequires:	pkgconfig >= 1:0.15
Requires:	libxml2 >= 1:2.6.17
Requires:	libxslt-progs
Requires:	lttoolbox >= 3.3.1
Requires:	pcre-cxx >= 6.4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apertium is a free/open-source platform for developing rule-based
machine translation systems.

%description -l pl.UTF-8
Apertium to wolnodostępna platforma do tworzenia maszynowych systemów
tłumaczących opartych na regułach.

%package devel
Summary:	Header files for apertium library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki apertium
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
Requires:	libxml2-devel >= 1:2.6.17
Requires:	lttoolbox-devel >= 3.3.1
Requires:	pcre-cxx-devel >= 6.4

%description devel
Header files for apertium library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki apertium.

%package static
Summary:	Static apertium library
Summary(pl.UTF-8):	Statyczna biblioteka apertium
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static apertium library.

%description static -l pl.UTF-8
Statyczna biblioteka apertium.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README README-MODES
%attr(755,root,root) %{_bindir}/apertium
%attr(755,root,root) %{_bindir}/apertium-*
%attr(755,root,root) %{_libdir}/libapertium3-3.4.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libapertium3-3.4.so.0
%{_datadir}/apertium
%{_mandir}/man1/apertium.1*
%{_mandir}/man1/apertium-*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libapertium3.so
%{_libdir}/libapertium3.la
%{_includedir}/apertium-3.4
%{_pkgconfigdir}/apertium.pc
%{_aclocaldir}/apertium.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libapertium3.a
