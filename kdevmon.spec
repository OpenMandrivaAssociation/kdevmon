%define name    kdevmon
%define version 0.4.6
%define release %mkrel 12

Summary:	A utility for monitoring the throughput of one network device
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Monitoring
Source:		%{name}-%{version}-2.tar.bz2
Patch1:		kdevmon-0.4.6-fix-crash.patch.bz2

URL: 		http://www.Informatik.Uni-Oldenburg.DE/~bigboss/kdevmon/
BuildRoot: 	%_tmppath/%{name}-buildroot
BuildRequires:  kdelibs-devel

%description
Kdevmon is a utility for KDE that monitors the throughput of a network device.
It docks in Kicker (the panel of KDE 2)  and shows the current network traffic
as a diagram. There also is a resizable main window that provides a larger
traffic diagram and displays the current net speed in bits per second.
Middle-clicking on the dock window or on the main window offers
you an overview of the amount of incoming/outgoing bits and the current and
the maximum bit rate.

%prep
%setup -q
%patch1 -p1 -b .fix_crash

%build
%configure_kde3
%make

%install
rm -fr %buildroot
%makeinstall_std

%{find_lang} %{name} --with-html

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr (-,root,root)
%doc AUTHORS COPYING INSTALL ChangeLog README TODO 
%_kde3_bindir/kdevmon
%_kde3_datadir/applnk/Internet/kdevmon.desktop
%_kde3_iconsdir/locolor/*/*/*
