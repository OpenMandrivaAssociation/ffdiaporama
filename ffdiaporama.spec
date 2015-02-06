%define debug_package	%{nil}
%define oname   ffDiaporama
Name:           ffdiaporama
Version:        2.2
Release:        0.2
Summary:        Movie creator from photos and video clips
License:        GPLv2
URL:            http://ffdiaporama.tuxfamily.org
Group:          Video
# this is devel version
Source:         http://download.tuxfamily.org/%{name}/Packages/Stable/%{name}-2014.07.01.tar.gz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  desktop-file-utils
BuildRequires:  pkgconfig(exiv2)
BuildRequires:  pkgconfig(Qt5Svg)
BuildRequires:  pkgconfig(Qt5Help)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  qt5-macros
BuildRequires:  qmake5



Requires:       ffmpeg
Requires:       qt5-database-plugin-sqlite
Suggests:       ffdiaporama-texturemate
Suggests:       ffdiaporama-openclipart

%description
ffDiaporama is an application for creating video sequences consisting of
* titles, fixed or animated.
* images or photos, fixed or animated.
* movie clips
* music

These sequences are assembled into a slide show by means of transitions
to produce complete videos
The following options are available:

* Reframing of images and photos
* Cutting of video clips
* Adding text, notes to images, photos, sequences and animations
* Graphical filters on the images and the videos (conversion into
  black and white, dust removal, equalization of colors, etc.)
* Creation of animation by zoom, rotation or Ken Burns Effect on
  images or photos
* Correction of the images and the videos during animations
  (luminosity, contrast, gamma, colors, etc.)
* Transitions between sequences with definition of the transition type,
  sequence by sequence.
* Addition of a background sound (wav, mp3 or ogg) with customizable
  effects for volume, fade in/out and passage in pause, sequence by sequence.
* Generation of videos usable on most current video equipment
  (DVD player/smartphone, multimedia box, hard drive, etc.)
  but also publishable on the main video-sharing Websites
  (YouTube, Dailymotion, etc.)
* Video formats from QVGA (320×240) to Full HD (1920×1080)
  by way of the DVD and HD 720 formats.
* Image geometry (aspect ratio) : 4:3, 16:9 or 2.35:1 (cinema)
* Possible formats for rendering : avi, mpg, mp4, webm, mkv

%prep
%setup -q -n %{oname}
perl -pi -e "s|Categories=GTK;GNOME;Qt;KDE;AudioVideo|Categories=GTK;GNOME;Qt;KDE;AudioVideo;|" ffDiaporama.desktop

chmod -x authors.txt BUILDVERSION.txt changelog-en.txt changelog-fr.txt licences.txt \
  readme.txt licence.rtf ffDiaporama.xml ffDiaporama.desktop Devices.xml ffDiaporama-mime.xml \
  locale/LOCALEVERSION.TXT locale/WIKIVERSION.TXT


%build
%qmake_qt5 %{oname}.pro
%make

%install
%makeinstall INSTALL_ROOT=%{buildroot}
mkdir -p %{buildroot}%{_datadir}%{oname}/locale
install locale/*  %{buildroot}%{_datadir}/%{oname}/locale/

desktop-file-validate %{buildroot}%{_datadir}/applications/%{oname}.desktop

(cd %{buildroot} && find . -name '*.q*') | sed -e 's|^.||' | sed -e \
    's:\(.*/locale/\)\([_a-z_A-Z]\+\)\(.q\):%lang(\2) \1\2\3:' >> %{name}.lang
    
find %{buildroot}%{_datadir}/%{oname}/locale  -name '*.ts' -exec chmod -x {} \;

%files -f %{name}.lang
%doc authors.txt BUILDVERSION.txt changelog-en.txt changelog-fr.txt licences.txt readme.txt licence.rtf ffDiaporama.xml Devices.xml
%{_datadir}/%{oname}/*.txt
%{_datadir}/%{oname}/*.xml
%{_datadir}/%{oname}/*.rtf
%{_datadir}/%{oname}/locale/*.TXT
%{_datadir}/%{oname}/locale/*.ts

%{_bindir}/%{oname}
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/mime/packages/%{oname}-mime.xml
%{_iconsdir}/hicolor/*/apps/%{name}.png