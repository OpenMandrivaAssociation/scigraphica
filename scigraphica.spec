%define	name	scigraphica
%define	version	2.1.0
%define	release	%mkrel 6

Name:		%{name}
Summary:	Data analysis and technical graphics
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sciences/Other
Source0:	%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Buildrequires:	libgtk+extra-2-devel >= 2.0.0
Buildrequires:	termcap-devel imagemagick 
Buildrequires:	readline-devel libscigraphica-devel
Buildrequires:	python-numarray-devel python-numeric-devel
Url:		http://scigraphica.sourceforge.net/

%description
SciGraphica is a scientific application for data analysis and technical 
graphics. It pretends to be a clone of the popular commercial (and expensive)
application "Microcal Origin". It fully supplies plotting features for 2D, 3D 
and polar charts. The aim is to obtain a fully-featured, cross-platform, 
user-friendly, self-growing scientific application. It is free and
open-source, released under the GPL license. 

%prep
%setup -q

%build
%configure2_5x --with-python-numeric-path=%{_includedir}/python%{py_ver}/Numeric/ --disable-imlib
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=scigraphica
Icon=%{name}
Categories=Science;
Name=SciGraphica
Comment=Data Plotting and Visualization
EOF

install -d $RPM_BUILD_ROOT{%{_liconsdir},%{_miconsdir}}
convert pixmaps/sg_icon.xpm -size 16x16 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
convert pixmaps/sg_icon.xpm -size 32x32 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert pixmaps/sg_icon.xpm -size 48x48 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png


%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc AUTHORS ChangeLog TODO examples/*.sg examples/*.dat
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_datadir}/applications/mandriva-*.desktop
%{_datadir}/%{name}
%{_datadir}/gnome/apps/Applications/*
%{_datadir}/gnome/help/%{name}
%{_mandir}/man1/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%dir %{_libdir}/%{name}/%{version}/plugins
%{_libdir}/%{name}/%{version}/plugins/*/*


