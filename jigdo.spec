%define	name	jigdo
%define	version	0.7.3
%define	release	%mkrel 7
%define Summary	Jigsaw Download

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
Group:		Networking/File transfer
URL:		http://atterer.net/jigdo/
Source0:	http://atterer.net/jigdo/%{name}-%{version}.tar.bz2
Patch0:		jigdo-0.7.3-gcc43.patch
Source11:	%{name}-16.png
Source12:	%{name}-32.png
Source13:	%{name}-48.png
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
License:	GPL
BuildRequires:	db4.7-devel w3c-libwww-devel openssl-devel mawk
BuildRequires:	gtk2-devel gettext-devel libcurl-devel libbzip2-devel

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
Categories=GTK;Network;FileTransfer;X-MandrivaLinux-Internet-FileTransfer;
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


