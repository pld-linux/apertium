Summary:	lttoolbox-based translation modules generator
Summary(pl.UTF-8):	Oparty na pakiecie lttoolbox generator modułów tłumaczących
Name:		apertium
Version:	3.9.12
Release:	1
License:	GPL v2+
Group:		Applications/Text
Source0:	https://github.com/apertium/apertium/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b272baa484ac5977a7f9ea09f49c548f
Patch0:		shebang.patch
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
BuildRequires:	lttoolbox-devel >= 3.3.3
BuildRequires:	pcre-cxx-devel >= 6.4
BuildRequires:	pkgconfig >= 1:0.15
Requires:	libxml2 >= 1:2.6.17
Requires:	libxslt-progs
Requires:	lttoolbox >= 3.3.3
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
Requires:	lttoolbox-devel >= 3.3.3
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
%patch -P0 -p1

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+python3(\s|$),#!%{__python3}\1,' \
      scripts/apertium-editdist \
      scripts/apertium-filter-rules \
      scripts/apertium-filter-xml \
      scripts/apertium-genvdix \
      scripts/apertium-genvldix \
      scripts/apertium-genvrdix \
      scripts/apertium-metalrx

%{__sed} -E -i -e '1s,#!\s*/usr/bin/env\s+bash(\s|$),#!/bin/bash\1,' \
      scripts/apertium-filter-dix.in \
      scripts/apertium-metalrx-to-lrx.in \
      scripts/apertium-translate-to-default-equivalent.in


%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

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
%attr(755,root,root) %{_libdir}/libapertium.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libapertium.so.3
%{_datadir}/apertium
%{_mandir}/man1/apertium.1*
%{_mandir}/man1/apertium-*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libapertium.so
%{_libdir}/libapertium.la
%{_includedir}/apertium
%{_pkgconfigdir}/apertium.pc
%{_aclocaldir}/apertium.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libapertium.a
