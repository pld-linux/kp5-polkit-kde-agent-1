%define		kdeplasmaver	5.24.0
%define		qt_ver		5.5.1
%define		kpname		polkit-kde-agent-1
#
Summary:	KDE PolicyKit authentication agent
Summary(pl.UTF-8):	Agent uwierzytelniający PolicyKit dla KDE
Name:		kp5-%{kpname}
Version:	5.24.0
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	eacdd3ef241f27d7ae68abce49d47a45
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= %{qt_ver}
BuildRequires:	Qt5DBus-devel >= %{qt_ver}
BuildRequires:	Qt5Widgets-devel >= %{qt_ver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	kf5-extra-cmake-modules >= 1.2.0
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kcrash-devel
BuildRequires:	kf5-kdbusaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	polkit-qt5-1-devel >= 0.103.0
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	xz
Requires:	polkit-qt5-1 >= 0.103.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
KDE PolicyKit authentication agent.

%description -l pl.UTF-8
Agent uwierzytelniający PolicyKit dla KDE.

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
%{_datadir}/knotifications5/policykit1-kde.notifyrc
%{systemduserunitdir}/plasma-polkit-agent.service
%attr(755,root,root) %{_prefix}/libexec/polkit-kde-authentication-agent-1
%{_desktopdir}/org.kde.polkit-kde-authentication-agent-1.desktop
