%define name    kdevmon
%define version 0.4.6
%define release %mkrel 10

Summary:	A utility for monitoring the throughput of one network device
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Monitoring
Source:		%{name}-%{version}-2.tar.bz2
Patch1:		kdevmon-0.4.6-fix-crash.patch.bz2

URL: 		http://www.Informatik.Uni-Oldenburg.DE/~bigboss/kdevmon/
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
export QTDIR=%_prefix/lib/qt3
export QTLIB=$QTDIR/%_lib
export KDEDIR=%_libdir

CFLAGS="%optflags" CXXFLAGS="%optflags" \
./configure  \
            --disable-rpath \
	    --prefix=%_prefix \
	    --mandir=%_mandir \
	    --datadir=%_datadir \
	    --disable-debug \
		--enable-final

%make

%install

%makeinstall
install -d %buildroot/%_menudir/
kdedesktop2mdkmenu.pl Kdevmon "Applications/Monitoring"  %buildroot/%_datadir/applnk/Internet/kdevmon.desktop %buildroot/%_menudir/kdevmon

%{find_lang} %{name}

%post
%{update_menus}

%postun
%{clean_menus}

%files -f %{name}.lang
%defattr (-,root,root)
%doc AUTHORS COPYING INSTALL ChangeLog README TODO 
%_menudir/*
%_bindir/kdevmon

%_datadir/applnk/Internet/kdevmon.desktop

%dir %_docdir/HTML/en/kdevmon/
%_docdir/HTML/en/kdevmon/*

%_datadir/icons/locolor/*


