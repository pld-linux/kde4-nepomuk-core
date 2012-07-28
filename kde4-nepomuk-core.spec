# $Revision:$, $Date:$
Summary:	Nepomuk Core utilities and libraries
Name:		nepomuk-core
Version:	4.9.0
Release:	0.1
License:	LGPLv2 or LGPLv3
URL:		http://www.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	doxygen
BuildRequires:	kdelibs4-devel >= %{version}
BuildRequires:	pkgconfig
BuildRequires:	shared-desktop-ontologies => 0.10.0
BuildRequires:	soprano-devel => 2.8.0
Requires:	%{name}-libs = %{version}-%{release}

%description
Nepomuk Core utilities.

%package devel
Summary:	Developer files for %{name}
Requires:	%{name}-libs = %{version}-%{release}

%description devel
Nepomuk Core development files and libraries.

%package libs
Summary:	Runtime libraries for %{name}
Requires:	%{name} = %{version}-%{release}
Requires:	kdelibs4%{?_isa} >= %{version}

%description libs
Nepomuk Core libraries.

%prep
%setup -q

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

%files
%defattr(644,root,root,755)
%doc ontologies/README
%{_kde4_appsdir}/fileindexerservice/
%{_kde4_appsdir}/nepomukfilewatch/
%{_kde4_appsdir}/nepomukstorage/
# this one maybe in -devel?  --rex
%{_kde4_bindir}/nepomuk-simpleresource-rcgen
%{_kde4_bindir}/nepomukbackup
%{_kde4_bindir}/nepomukindexer
%{_kde4_bindir}/nepomukserver
%{_kde4_bindir}/nepomukservicestub
%{_kde4_libdir}/libkdeinit4_nepomukserver.so
%{_kde4_datadir}/applications/kde4/nepomukbackup.desktop
%{_kde4_datadir}/autostart/nepomukserver.desktop
%{_kde4_datadir}/kde4/services/*.desktop
%{_kde4_datadir}/kde4/servicetypes/nepomukservice.desktop
%{_kde4_datadir}/ontology/kde/
%{_datadir}/dbus-1/interfaces/*.xml

%files devel
%defattr(644,root,root,755)
%{_kde4_libdir}/libnepomuksync.so
%{_kde4_libdir}/libnepomukcore.so
%{_kde4_libdir}/cmake/NepomukCore/
%{_kde4_includedir}/nepomuk2/
%{_kde4_includedir}/Nepomuk2/

%post libs -p /sbin/ldconfig
%postun libs -p /sbin/ldconfig

%files libs
%defattr(644,root,root,755)
%{_kde4_libdir}/kde4/*.so
%{_kde4_libdir}/libnepomukcommon.so
%{_kde4_libdir}/libnepomukcore.so.*
%{_kde4_libdir}/libnepomuksync.so.*


