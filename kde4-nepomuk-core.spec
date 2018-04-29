%define		_state		stable
%define		orgname		nepomuk-core
%define		qt_ver		4.8.3

Summary:	Nepomuk Core utilities and libraries
Summary(pl.UTF-8):	Narzędzia i biblioteki Nepomuk Core
Name:		kde4-nepomuk-core
Version:	4.14.3
Release:	7
License:	LGPL v2.1 or LGPL v3
Group:		X11/Applications
Source0:	http://download.kde.org/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	8c25048fce09e23469b2fb149331a58a
URL:		http://www.kde.org/
BuildRequires:	QtCore-devel >= %{qt_ver}
BuildRequires:	QtDBus-devel >= %{qt_ver}
BuildRequires:	acl-devel
BuildRequires:	attr-devel
BuildRequires:	automoc4
BuildRequires:	cmake >= 2.8.6
BuildRequires:	doxygen
BuildRequires:	ebook-tools-devel
BuildRequires:	exiv2-devel >= 0.21
BuildRequires:	ffmpeg-devel >= 1.0
BuildRequires:	kde4-baloo-devel >= %{version}
BuildRequires:	kde4-kdegraphics-mobipocket-devel >= %{version}
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	kde4-kfilemetadata-devel >= %{version}
BuildRequires:	libdbusmenu-qt-devel
BuildRequires:	pkgconfig
BuildRequires:	poppler-qt4-devel >= 0.12.1
BuildRequires:	qt4-build >= %{qt_ver}
BuildRequires:	shared-desktop-ontologies-devel >= 0.10.51
BuildRequires:	soprano-devel >= 2.9.3
BuildRequires:	strigi-devel
BuildRequires:	taglib-devel >= 1.4
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	zlib-devel
Requires:	QtCore >= %{qt_ver}
Requires:	QtDBus >= %{qt_ver}
Requires:	exiv2-libs >= 0.21
Requires:	ffmpeg-libs >= 1.0
Requires:	kde4-kdegraphics-mobipocket >= %{version}
Requires:	kde4-kdelibs >= %{version}
Requires:	kde4-kfilemetadata >= %{version}
Requires:	poppler-qt4 >= 0.12.1
Requires:	shared-desktop-ontologies >= 0.10.51
Requires:	soprano >= 2.9.3
Requires:	taglib >= 1.4
Suggests:	kde4-baloo >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Nepomuk Core utilities and libraries.

%description -l pl.UTF-8
Narzędzia i biblioteki Nepomuk Core.

%package devel
Summary:	Development files for Nepomuk Core
Summary(pl.UTF-8):	Pliki programistyczne Nepomuk Core
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= %{qt_ver}
Requires:	QtDBus-devel >= %{qt_ver}
Requires:	kde4-kdelibs-devel >= %{version}
Requires:	soprano-devel >= 2.9.3

%description devel
Development files for Nepomuk Core.

%description devel -l pl.UTF-8
Pliki programistyczne Nepomuk Core.

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

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/nepomuk2-rcgen
%attr(755,root,root) %{_bindir}/nepomukbackup
%attr(755,root,root) %{_bindir}/nepomukbaloomigrator
%attr(755,root,root) %{_bindir}/nepomukcleaner
%attr(755,root,root) %{_bindir}/nepomukcmd
%attr(755,root,root) %{_bindir}/nepomukctl
%attr(755,root,root) %{_bindir}/nepomukfileindexer
%attr(755,root,root) %{_bindir}/nepomukfilewatch
%attr(755,root,root) %{_bindir}/nepomukindexer
%attr(755,root,root) %{_bindir}/nepomukmigrator
%attr(755,root,root) %{_bindir}/nepomuksearch
%attr(755,root,root) %{_bindir}/nepomukserver
%attr(755,root,root) %{_bindir}/nepomukservicestub
%attr(755,root,root) %{_bindir}/nepomukshow
%attr(755,root,root) %{_bindir}/nepomuk-simpleresource-rcgen
%attr(755,root,root) %{_bindir}/nepomukstorage
%attr(755,root,root) %{_libdir}/kde4/libexec/kde_nepomuk_filewatch_raiselimit
%attr(755,root,root) %{_libdir}/kde4/nepomukepubextractor.so
%attr(755,root,root) %{_libdir}/kde4/nepomukexiv2extractor.so
%attr(755,root,root) %{_libdir}/kde4/nepomukffmpegextractor.so
%attr(755,root,root) %{_libdir}/kde4/nepomukmobiextractor.so
%attr(755,root,root) %{_libdir}/kde4/nepomukodfextractor.so
%attr(755,root,root) %{_libdir}/kde4/nepomukoffice2007extractor.so
%attr(755,root,root) %{_libdir}/kde4/nepomukofficeextractor.so
%attr(755,root,root) %{_libdir}/kde4/nepomukplaintextextractor.so
%attr(755,root,root) %{_libdir}/kde4/nepomukpopplerextractor.so
%attr(755,root,root) %{_libdir}/kde4/nepomuktaglibextractor.so
%attr(755,root,root) %{_libdir}/libkdeinit4_nepomukserver.so
%attr(755,root,root) %{_libdir}/libnepomukcommon.so
%attr(755,root,root) %{_libdir}/libnepomukextractor.so
%attr(755,root,root) %{_libdir}/libnepomukcore.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnepomukcore.so.4
%attr(755,root,root) %{_libdir}/libnepomukcleaner.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libnepomukcleaner.so.4
%{_desktopdir}/kde4/nepomukbackup.desktop
%{_desktopdir}/kde4/nepomukcleaner.desktop
%{_datadir}/apps/fileindexerservice
%{_datadir}/apps/nepomukfilewatch
%{_datadir}/apps/nepomukstorage
%{_datadir}/autostart/nepomukserver.desktop
%{_datadir}/autostart/nepomukbaloomigrator.desktop
%{_datadir}/dbus-1/interfaces/org.kde.NepomukServer.xml
%{_datadir}/dbus-1/interfaces/org.kde.nepomuk.*.xml
%{_datadir}/dbus-1/system-services/org.kde.nepomuk.filewatch.service
%{_datadir}/kde4/services/nepomuk*.desktop
%{_datadir}/kde4/servicetypes/nepomukcleaningjob.desktop
%{_datadir}/kde4/servicetypes/nepomukextractor.desktop
%{_datadir}/kde4/servicetypes/nepomukservice2.desktop
%{_datadir}/kde4/servicetypes/nepomukservice.desktop
%{_datadir}/ontology/kde/kext.ontology
%{_datadir}/ontology/kde/kext.trig
%{_datadir}/ontology/kde/kuvo.ontology
%{_datadir}/ontology/kde/kuvo.trig
%{_datadir}/ontology/kde/nrio.ontology
%{_datadir}/ontology/kde/nrio.trig
%{_datadir}/polkit-1/actions/org.kde.nepomuk.filewatch.policy
/etc/dbus-1/system.d/org.kde.nepomuk.filewatch.conf

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libnepomukcore.so
%attr(755,root,root) %{_libdir}/libnepomukcleaner.so
%{_includedir}/Nepomuk2
%{_includedir}/nepomuk2
%{_libdir}/cmake/NepomukCore
