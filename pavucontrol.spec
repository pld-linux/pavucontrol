Summary:	PulseAudio Volume Control
Summary(pl.UTF-8):	PulseAudio Volume Control - sterowanie głośnością PulseAudio
Name:		pavucontrol
Version:	0.9.10
Release:	2
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	http://0pointer.de/lennart/projects/pavucontrol/%{name}-%{version}.tar.gz
# Source0-md5:	b966eb31ec7fd6afa0f1ed7d5ba480b3
URL:		http://0pointer.de/lennart/projects/pavucontrol/
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.9
BuildRequires:	gettext-devel
BuildRequires:	gtkmm-devel >= 2.16.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcanberra-gtk-devel >= 0.16
BuildRequires:	libglademm-devel >= 2.4.0
BuildRequires:	libsigc++-devel >= 2.0.0
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.16
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
