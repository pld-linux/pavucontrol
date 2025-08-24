Summary:	PulseAudio Volume Control
Summary(pl.UTF-8):	PulseAudio Volume Control - sterowanie głośnością PulseAudio
Name:		pavucontrol
Version:	6.1
Release:	1
License:	GPL v2+
Group:		X11/Applications/Sound
Source0:	https://www.freedesktop.org/software/pulseaudio/pavucontrol/%{name}-%{version}.tar.xz
# Source0-md5:	51743b9bc9eb01959bf3c770facc6555
URL:		https://www.freedesktop.org/software/pulseaudio/pavucontrol/
BuildRequires:	gcc >= 6:4.6
BuildRequires:	gettext-tools
BuildRequires:	gtkmm4-devel >= 4.0
BuildRequires:	json-glib-devel >= 1.0
BuildRequires:	libcanberra-devel >= 0.16
BuildRequires:	libsigc++3-devel >= 3.0
BuildRequires:	libstdc++-devel >= 6:8
BuildRequires:	meson >= 0.50.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pkgconfig
BuildRequires:	pulseaudio-devel >= 5.0
BuildRequires:	rpmbuild(macros) >= 2.042
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires(post,postun):	desktop-file-utils
Requires:	libcanberra >= 0.16
Requires:	pulseaudio-libs >= 5.0
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
%meson \
	-Dlynx=false

%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/%{name}

%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/nb{_NO,}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database_post

%postun
%update_desktop_database_postun

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc build/doc/README.html
%attr(755,root,root) %{_bindir}/pavucontrol
%{_desktopdir}/org.pulseaudio.pavucontrol.desktop
%{_datadir}/metainfo/org.pulseaudio.pavucontrol.metainfo.xml
