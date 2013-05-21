%define	name	jigdo
%define	version	0.7.3
%define	release	13
%define Summary	Jigsaw Download

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Networking/File transfer
URL:		http://atterer.net/jigdo/
Source0:	http://atterer.net/jigdo/%{name}-%{version}.tar.bz2
Patch0:		jigdo-0.7.3-gcc43.patch
Patch1:		jigdo-0.7.3-link.patch
Source11:	%{name}-16.png
Source12:	%{name}-32.png
Source13:	%{name}-48.png
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
BuildRequires:	db-devel mawk
BuildRequires:	pkgconfig(gtk+-2.0) gettext-devel libcurl-devel libbzip2-devel

%description
Jigsaw Download, or short jigdo, is an intelligent tool that can be used on the
pieces of any chopped-up big file to create a special "template" file which
makes reassembly of the file very easy for users who only have the pieces.

What makes jigdo special is that there are no restrictions on what
offsets/sizes the individual pieces have in the original big image. This makes
the program very well suited for distributing CD/DVD images (or large zip/tar
archives) because you can put the files on the CD on an FTP server - when jigdo
is presented the files along with the template you generated, it is able to
recreate the CD image.

%prep
%setup -q
%patch0 -p1
%patch1 -p0

%build
autoconf
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std


mkdir %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Jigdo
Comment=%{Summary}
Exec=%{name} %U
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;Network;FileTransfer;
EOF

install -m644 %{SOURCE11} -D %{buildroot}%{_miconsdir}/%{name}.png
install -m644 %{SOURCE12} -D %{buildroot}%{_iconsdir}/%{name}.png
install -m644 %{SOURCE13} -D %{buildroot}%{_liconsdir}/%{name}.png

%{find_lang} %{name}

%clean
rm -rf %{buildroot}

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%files -f %{name}.lang
%defattr(-,root,root)
%doc README doc/jigdo-file.* doc/TechDetails.txt
%{_bindir}/%{name}*
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_mandir}/man1/%{name}*
%{_liconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_miconsdir}/%{name}.png




%changelog
* Tue May 08 2012 Crispin Boylan <crisb@mandriva.org> 0.7.3-13
+ Revision: 797443
- Rebuild

  + Bogdano Arendartchuk <bogdano@mandriva.com>
    - build with db5 (from fwang | 2011-04-12 11:14:51 +0200)

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.3-11mdv2011.0
+ Revision: 612448
- the mass rebuild of 2010.1 packages

* Sat Jan 30 2010 Funda Wang <fwang@mandriva.org> 0.7.3-10mdv2010.1
+ Revision: 498578
- build with db4.8

* Thu Oct 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.3-9mdv2010.0
+ Revision: 455870
- rebuild for new curl SSL backend

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Feb 24 2009 Emmanuel Andry <eandry@mandriva.org> 0.7.3-7mdv2009.1
+ Revision: 344540
- fix gcc43 build with P0 from gentoo
- switch to db4.7

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Sun Jan 13 2008 Emmanuel Andry <eandry@mandriva.org> 0.7.3-5mdv2008.1
+ Revision: 150439
- use db4.6

  + Thierry Vignaud <tv@mandriva.org>
    - drop old menu
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Tue Aug 28 2007 Thierry Vignaud <tv@mandriva.org> 0.7.3-4mdv2008.0
+ Revision: 73046
- kill desktop-file-validate's 'warning: key "Encoding" in group "Desktop Entry" is deprecated'

