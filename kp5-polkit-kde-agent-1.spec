# TODO:
# - libhybris
#
%define		kdeplasmaver	5.11.2
%define		qtver		5.5.1
%define		kpname		polkit-kde-agent-1
#
Summary:	KDE PolicyKit authentication agent
Summary(pl.UTF-8):	Agent uwierzytelniający PolicyKit dla KDE
Name:		kp5-%{kpname}
Version:	5.11.2
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	da706bdb5da82b96711ad94b2edd0700
URL:		https://kde.org/
BuildRequires:	Mesa-libEGL-devel
BuildRequires:	Mesa-libgbm-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5EventDispatcherSupport-devel >= %{qtver}
BuildRequires:	Qt5FontDatabaseSupport-devel >= %{qtver}
#BuildRequires:	Qt5PlatformSupport-devel >= %{qtver}
BuildRequires:	Qt5ThemeSupport-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kcompletion-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdeclarative-devel
BuildRequires:	kf5-kglobalaccel-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kinit-devel
BuildRequires:	kf5-kio-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kf5-knotifications-devel
BuildRequires:	kf5-kpackage-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-kwayland-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kf5-kxmlgui-devel
BuildRequires:	kf5-plasma-framework-devel
BuildRequires:	kp5-kdecoration-devel
BuildRequires:	kp5-kscreenlocker-devel
BuildRequires:	libdrm-devel
BuildRequires:	libepoxy-devel
BuildRequires:	libinput-devel
BuildRequires:	libxcb-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	udev-devel
BuildRequires:	wayland-devel
BuildRequires:	xcb-util-cursor-devel
BuildRequires:	xcb-util-image-devel
BuildRequires:	xcb-util-keysyms-devel
BuildRequires:	xcb-util-wm-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE PolicyKit authentication agent.

%description -l pl.UTF-8
Agent uwierzytelniający PolicyKit dla KDE.

%package devel
Summary:	Header files for %{kpname} development
Summary(pl.UTF-8):	Pliki nagłówkowe dla programistów używających %{kpname}
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for %{kpname} development.

%description devel -l pl.UTF-8
Pliki nagłówkowe dla programistów używających %{kpname}.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
        DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
/etc/xdg/autostart/polkit-kde-authentication-agent-1.desktop
%{_libdir}/polkit-kde-authentication-agent-1
%{_datadir}/knotifications5/policykit1-kde.notifyrc
