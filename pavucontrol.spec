#
# Conditional build:
%bcond_with	gtk2	# GTK+ 2.x instead of 3.x
#
Summary:	PulseAudio Volume Control
Summary(pl.UTF-8):	PulseAudio Volume Control - sterowanie głośnością PulseAudio
Name:		pavucontrol
Version:	1.0
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://freedesktop.org/software/pulseaudio/pavucontrol/%{name}-%{version}.tar.xz
# Source0-md5:	0ab6b13542af9b4417438527d2524316
URL:		http://freedesktop.org/software/pulseaudio/pavucontrol/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libsigc++-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.16
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
%if %{with gtk2}
BuildRequires:	gtkmm-devel >= 2.16.0
BuildRequires:	libcanberra-gtk-devel >= 0.16
%else
BuildRequires:	gtkmm3-devel >= 3.0.0
BuildRequires:	libcanberra-gtk3-devel >= 0.16
%endif
Requires:	pulseaudio-libs >= 0.9.16
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PulseAudio Volume Control (pavucontrol) is a simple GTK+ based volume
control tool ("mixer") for the PulseAudio sound server. In contrast to
classic mixer tools this one allows you to control both the volume of
hardware devices and of each playback stream seperately.

%description -l pl.UTF-8
PulseAudio Volume Control (pavucontrol) to proste, oparte na GTK+,
narzędzie do regulacji głośności ("mikser") dla serwera dźwięku
PulseAudio. W przeciwieństwie do klasycznych mikserów pozwala
regulować głośność urządzeń sprzętowych, jak i każdego odtwarzanego
strumienia osobno.

%prep
%setup -q

%build
%{__intltoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_gtk2:--disable-gtk3} \
	--disable-lynx
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/pavucontrol
%{_datadir}/pavucontrol
%{_desktopdir}/pavucontrol.desktop
