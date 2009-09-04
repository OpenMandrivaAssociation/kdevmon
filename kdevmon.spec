%define name    kdevmon
%define version 0.4.7
%define svnrel  840945
%define release %mkrel -c %svnrel 2

Summary:	A utility for monitoring the throughput of one network device
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Monitoring
Source:		%{name}-r%{svnrel}.tar.bz2
URL: 		http://websvn.kde.org/trunk/playground/network/kdevmon/
BuildRoot: 	%_tmppath/%{name}-buildroot
BuildRequires:  kdelibs4-devel

%description
Kdevmon is a utility for KDE that monitors the throughput of a network
device. It docks in the systemtray and shows the current network traffic
as a diagram. There also is a resizable main window that provides a
larger traffic diagram and displays the current net speed in bits per
second. Middle-clicking on the dock window or on the main window offers
you an overview of the amount of incoming/outgoing bits and the current
and the maximum bit rate.

%prep
%setup -q -n %name

%build
%cmake_kde4
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files
%defattr (-,root,root)
%doc ChangeLog README TODO 
%_kde_bindir/kdevmon
%_kde_datadir/applications/kde4/kdevmon.desktop
