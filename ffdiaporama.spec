# This spec is based on Alberto Altieri's work in MIB with
# heavy modifications

%define		oname	ffDiaporama
%define		year	2012
%define		date	0305

Name:		ffdiaporama
Version:	1.2
Release:	%mkrel 1
Summary:	A tool to create video sequences from images, titles, music
License:	GPLv2
Group:		Video
URL:		http://ffdiaporama.tuxfamily.org
Source0:	http://ffdiaporama.tuxfamily.org/download.php?f=Stable/%{version}_%{year}%{date}/%{name}_%{version}.%{year}.%{date}.tar.gz
BuildRequires:	qt4-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(exiv2)
Requires:	ffmpeg
Requires:	exiv2

%description
ffDiaporama is an application of creation of videos sequences established by
titles, images, photos, movie clip and music.

These sequences are assembled in slide show by means of transitions of
sequence to produce complete videos

Main features:
* Refocused of images and photos and refocused and cutting of video clips
* Note (addition of text) for images, photos, sequences and animations
* Graphic filters on the images and the videos (passage in black and
  white, dust removal, equalization of colors, etc.)
* Creation of animation by zoom, rotation or Ken Burns Effect on part of
  images or photos
* Correction of the images and the videos during the animations
  (luminosity, contrast, gamma, colors, etc.)
* Transitions between sequence with definition of the transition type,
  sequence by sequence.
* Addition of a background sound (wav, mp3 or ogg) with customizable
  effects of volume, fade in/out and passage in pause, sequence by
  sequence.
* Generation of usable videos by most of the current videos equipments
  (DVD player/smartphone, multimedia box, hard drive, etc.) but also
  publishable on the main video sharing Web sites (YouTube, Dailymotion,
  etc.)

%prep
%setup -q -c

%build
%qmake_qt4 %{oname}.pro
%make

%install
%__rm -rf %{buildroot}
%__make install INSTALL_ROOT=%{buildroot}
desktop-file-install --vendor="" \
       --dir=%{buildroot}%{_datadir}/applications/ \
       --add-category="GTK"  \
       ffDiaporama.desktop

%clean
%__rm -rf %{buildroot}

%files
%doc licences.txt
%{_bindir}/%{oname}
%{_datadir}/%{oname}
%{_datadir}/mime/packages/%{oname}-mime.xml
%{_datadir}/applications/%{oname}.desktop

