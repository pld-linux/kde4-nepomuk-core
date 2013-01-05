# $Revision:$, $Date:$
%define         _state          stable
%define         orgname        	nepomuk-core
%define         qtver           4.8.3

Summary:	Nepomuk Core utilities and libraries
Name:		kde4-nepomuk-core
Version:	4.9.5
Release:	1
License:	LGPLv2 or LGPLv3
Group:		X11/Applications
URL:		http://www.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	0182ca4735278484c9b78ec5ecf0b825
BuildRequires:	QtCore-devel >= %{qtver}
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	doxygen
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	libdbusmenu-qt-devel
BuildRequires:	pkgconfig
BuildRequires:	qca-devel
BuildRequires:	shared-desktop-ontologies => 0.10.0
BuildRequires:	soprano-devel => 2.8.0
BuildRequires:	strigi-devel
BuildRequires:	zlib-devel
Requires:	QtCore >= %{qtver}
BuildRoot:      %{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nepomuk Core utilities.

%package devel
Summary:	Developer files for %{name}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Nepomuk Core development files and libraries.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
		-DHTML_INSTALL_DIR=%{_kdedocdir} \
		-DKDE_DISTRIBUTION_TEXT="PLD-Linux" \
		-DKDE4_ENABLE_FINAL=OFF \
		../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nepomuk-simpleresource-rcgen
%attr(755,root,root) %{_bindir}/nepomukbackup
%attr(755,root,root) %{_bindir}/nepomukindexer
%attr(755,root,root) %{_bindir}/nepomukserver
%attr(755,root,root) %{_bindir}/nepomukservicestub
%attr(755,root,root) %{_libdir}/kde4/nepomukbackupsync.so
%attr(755,root,root) %{_libdir}/kde4/nepomukfileindexer.so
%attr(755,root,root) %{_libdir}/kde4/nepomukfilewatch.so
%attr(755,root,root) %{_libdir}/kde4/nepomukqueryservice.so
%attr(755,root,root) %{_libdir}/kde4/nepomukstorage.so
%attr(755,root,root) %{_libdir}/libkdeinit4_nepomukserver.so
%attr(755,root,root) %{_libdir}/libnepomukcommon.so
%attr(755,root,root) %{_libdir}/libnepomukcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnepomukcore.so.?
%attr(755,root,root) %{_libdir}/libnepomuksync.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnepomuksync.so.?
%{_desktopdir}/kde4/nepomukbackup.desktop
%{_datadir}/apps/fileindexerservice
%{_datadir}/apps/nepomukfilewatch
%{_datadir}/apps/nepomukstorage
%{_datadir}/autostart/nepomukserver.desktop
%{_datadir}/dbus-1/interfaces/org.kde.NepomukServer.xml
%{_datadir}/dbus-1/interfaces/org.kde.nepomuk.*.xml
%{_datadir}/kde4/services/nepomuk*.desktop
%{_datadir}/kde4/servicetypes/nepomukservice.desktop
%{_datadir}/ontology/kde/*.ontology
%{_datadir}/ontology/kde/*.trig


%files devel
%defattr(644,root,root,755)
%{_includedir}/Nepomuk2
%{_includedir}/nepomuk2
%{_libdir}/cmake/NepomukCore
%attr(755,root,root) %{_libdir}/libnepomukcore.so
%attr(755,root,root) %{_libdir}/libnepomuksync.so
