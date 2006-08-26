Summary:	PulseAudio Volume Control
Summary(pl):	PulseAudio Volume Control - sterowanie g³o¶no¶ci± PulseAudio
Name:		pavucontrol
Version:	0.9.3
Release:	1
License:	GPL v2+
Group:		Applications/Sound
Source0:	http://0pointer.de/lennart/projects/pavucontrol/%{name}-%{version}.tar.gz
# Source0-md5:	fbbaf95f3224e1441077381fa350a413
Patch0:		%{name}-desktop.patch
URL:		http://0pointer.de/lennart/projects/pavucontrol/
BuildRequires:	gtkmm-devel >= 2.4
BuildRequires:	libglademm-devel >= 2.4
BuildRequires:	libsigc++-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 0.9.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PulseAudio Volume Control (pavucontrol) is a simple GTK+ based volume
control tool ("mixer") for the PulseAudio sound server. In contrast to
classic mixer tools this one allows you to control both the volume of
hardware devices and of each playback stream seperately.

%description -l pl
PulseAudio Volume Control (pavucontrol) to proste, oparte na GTK+,
narzêdzie do regulacji g³o¶no¶ci ("mikser") dla serwera d¼wiêku
PulseAudio. W przeciwieñstwie do klasycznych mikserów pozwala
regulowaæ g³o¶no¶æ urz±dzeñ sprzêtowych, jak i ka¿dego odtwarzanego
strumienia osobno.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-lynx
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/pavucontrol
%{_datadir}/pavucontrol
%{_desktopdir}/pavucontrol.desktop
