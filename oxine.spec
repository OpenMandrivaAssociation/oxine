%define name oxine
%define version 0.7.1
%define tarballver %version
%define release %mkrel 7
%define xinever 1-0.beta9
Summary: OSD-based xine video player frontend
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/oxine/%{name}-%{tarballver}.tar.gz
# (Anssi 04/2008) xvdr/xineliboutput support, from SVN, adapted to 0.7.1
Patch0: oxine-0.7.1-xvdr.patch
License: GPL
URL: http://oxine.sf.net
Group: Video
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libxine-devel >= %xinever
BuildRequires: liblirc-devel
BuildRequires: X11-devel
BuildRequires: libhal-devel
BuildRequires: libcdio-devel
BuildRequires: libcurl-devel
BuildRequires: libexif-devel
BuildRequires: gtk2-devel
BuildRequires: imagemagick-devel
BuildRequires: eject
Requires: xine-plugins >= %xinever
Requires: eject
Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils

%description
oxine is a lightweight, purely osd based xine frontend for set-top
boxes and home entertainment systems.

%prep
%setup -q -n %name-%tarballver
%patch0 -p1

%build
%configure2_5x --enable-vdr
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std 
#OXINE_SKINDIR=%buildroot%_datadir/oxine/skins DEFAULT_SKIN=%buildroot%_datadir/oxine/skins/default
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=Oxine
Comment=OSD Xine Video Player
Exec=%name %U
Icon=video_section
Terminal=false
Type=Application
StartupNotify=true
Categories=X-MandrivaLinux-Multimedia-Video;Video;Player;
MimeType=video/mpeg;video/msvideo;video/quicktime;video/x-avi;video/x-ms-asf;video/x-ms-wmv;video/x-msvideo;application/x-ogg;audio/x-mp3;audio/x-mpeg;video/x-fli;audio/x-wav;
EOF

%find_lang %name

%if %mdkversion < 200900
%post
%update_menus
%update_desktop_database
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%clean_desktop_database
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr(-,root,root)
%doc README TODO AUTHORS ChangeLog doc/*.pdf doc/*.html
%_bindir/%name
%_datadir/%name
%_datadir/applications/mandriva-*


