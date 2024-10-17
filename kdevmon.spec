%define name    kdevmon
%define version 0.4.7
%define svnrel  840945
%define release %mkrel -c %svnrel 3

Summary:	A utility for monitoring the throughput of one network device
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPLv2+
Group:		Monitoring
Source:		%{name}-r%{svnrel}.tar.bz2
URL: 		https://websvn.kde.org/trunk/playground/network/kdevmon/
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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.4.7-0.840945.3mdv2011.0
+ Revision: 619955
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.4.7-0.840945.2mdv2010.0
+ Revision: 429666
- rebuild

* Sat Aug 02 2008 Funda Wang <fwang@mandriva.org> 0.4.7-0.840945.1mdv2009.0
+ Revision: 260731
- swtich to kde4 version
- switch to /opt

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jan 03 2008 Thierry Vignaud <tv@mandriva.org> 0.4.6-10mdv2008.1
+ Revision: 142124
- kdedesktop2mdkmenu.pl is no more
- kill re-definition of %%buildroot on Pixel's request
- import kdevmon

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Wed May 10 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.4.6-10mdk
- Remove Hardcoded Packager tag

* Wed May 10 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.4.6-9mdk
- Rebuild to generate categories

* Wed Dec 28 2005 Anssi Hannula <anssi@mandriva.org> 0.4.6-8mdk
- fix x86_64 build

* Mon Dec 26 2005 Laurent Culioli <laurent@mandrakesoft.com> 0.4.6-7mdk
- Remove redundant Buildrequires
- use mkrel

* Wed Aug 24 2005 Laurent MONTEL <lmontel@mandriva.com> 0.4.6-6mdk
- Rebuild for add signature

* Mon Dec 20 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.4.6-5mdk
- Add patch1 fix crash 

* Mon Jun 14 2004 Laurent MONTEL <lmontel@mandrakesoft.com> 0.4.6-4mdk
- Rebuild

* Wed May 28 2003 Laurent MONTEL <lmontel@mandrakesoft.com> 0.4.6-3mdk
- fix spec file.

* Mon Aug 19 2002 Laurent Culioli <laurent@pschit.net> 0.4.6-2mdk
- Rebuild with gcc3.2

* Fri Jun 07 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 0.4.6-1mdk
- new version

* Tue Jan 22 2002 Laurent Culioli <laurent@mandrakesoft.com> 0.4.5-2mdk
- rebuild

* Fri Nov 16 2001 Laurent Culioli <laurent@mandrakesoft.com> 0.4.5-1mdk
- updated to 0.4.5

* Thu Sep 06 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 0.4.4-2mdk
- Rebuild 

* Mon Jul 16 2001 Laurent Culioli <laurent@mandrakesoft.com> 0.4.4-1mdk
- first package




