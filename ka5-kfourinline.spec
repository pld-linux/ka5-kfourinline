#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.2
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kfourinline
Summary:	kfourinline
Name:		ka5-%{kaname}
Version:	23.08.2
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications/Games
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2685f1f9aaf8185114b9b6f3d0cbb03a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Qml-devel >= 5.11.1
BuildRequires:	Qt5Quick-devel >= 5.11.1
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 3.20
BuildRequires:	gettext-devel
BuildRequires:	ka5-libkdegames-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdnssd-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KFourInLine is a board game for two players based on the Connect-Four
game. The players try to build up a row of four pieces using different
strategies.

%description -l pl.UTF-8
KFourInLine jest grą planszową dla dwóch graczy opartą na grze
Connect-Four (Połącz-Cztery). Gracze starają się zbudować rząd składający
się z czterech elementów używając różnych strategii.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kfourinline
%attr(755,root,root) %{_bindir}/kfourinlineproc
%{_desktopdir}/org.kde.kfourinline.desktop
%{_datadir}/config.kcfg/kwin4.kcfg
%{_iconsdir}/hicolor/128x128/apps/kfourinline.png
%{_iconsdir}/hicolor/16x16/apps/kfourinline.png
%{_iconsdir}/hicolor/22x22/apps/kfourinline.png
%{_iconsdir}/hicolor/32x32/apps/kfourinline.png
%{_iconsdir}/hicolor/48x48/apps/kfourinline.png
%{_iconsdir}/hicolor/64x64/apps/kfourinline.png
%{_datadir}/kfourinline
%{_datadir}/metainfo/org.kde.kfourinline.appdata.xml
%{_datadir}/qlogging-categories5/kfourinline.categories
