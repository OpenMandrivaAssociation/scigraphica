%define	name	scigraphica
%define	version	2.1.0
%define	release	%mkrel 2

Name:		%{name}
Summary:	Data analysis and technical graphics
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sciences/Other
Source0:	%{name}-%{version}.tar.bz2
Buildrequires:	libgtk+extra-2-devel >= 2.0.0
Buildrequires:	termcap-devel ImageMagick 
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
%configure --with-python-numeric-path=/usr/include/python2.5/Numeric/ --disable-imlib
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(scigraphica):command="scigraphica" icon="%{name}.png" \
                 needs="X11" section="Applications/Sciences/Other" title="SciGraphica" \
                 longtitle="Data Plotting and Visualization"
EOF

install -d $RPM_BUILD_ROOT{%{_liconsdir},%{_miconsdir}}
convert pixmaps/sg_icon.xpm -size 16x16 $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
convert pixmaps/sg_icon.xpm -size 32x32 $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
convert pixmaps/sg_icon.xpm -size 48x48 $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png


%post
%update_menus

%postun
%clean_menus

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc AUTHORS ChangeLog TODO examples/*.sg examples/*.dat
%{_bindir}/*
%{_datadir}/pixmaps/*
%{_menudir}/*
%{_datadir}/%{name}
%{_datadir}/gnome/apps/Applications/*
%{_datadir}/gnome/help/%{name}
%{_mandir}/man1/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%dir %{_libdir}/%{name}/%{version}/plugins
%{_libdir}/%{name}/%{version}/plugins/*/*


