# This spec is based on Alberto Altieri's work in MIB with
# heavy modifications
# debuginfo-without-sources
%define debug_package	%{nil}
%define		oname	ffDiaporama

Name:		ffdiaporama
Version:	2.0.1
Release:	1
Summary:	A tool to create video sequences from images, titles, music
License:	GPLv2
Group:		Video
URL:		http://ffdiaporama.tuxfamily.org
Source0:	http://download.tuxfamily.org/ffdiaporama/Archives/ffdiaporama_2.0.1.tar.gz

BuildRequires:	qt4-devel
BuildRequires:	ffmpeg-devel
BuildRequires:	pkgconfig(taglib)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_mixer)
BuildRequires:	desktop-file-utils
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(qimageblitz)

Requires:	ffmpeg
Requires:	exiv2
Requires:	qt4-common


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
  (DVD player/smart-phone, multimedia box, hard drive, etc.) but also
  publishable on the main video sharing Web sites (YouTube, Dailymotion,
  etc.)

%prep
%setup -q -c
chmod -x licence.rtf licences.txt
find background -name '*.txt' -exec chmod -x {} \;
find locale -name '*.ts' -exec chmod -x {} \;
find luma  -name '*.txt' -exec chmod -x {} \;

%build
%qmake_qt4 PREFIX=/usr %{oname}.pro 
%make

%install
%makeinstall INSTALL_ROOT=%{buildroot}
desktop-file-install --vendor="" \
       --dir=%{buildroot}%{_datadir}/applications/ \
       --add-category="GTK"  \
       ffDiaporama.desktop

# fix attr
chmod -x %{buildroot}%{_datadir}/mime/packages/ffDiaporama-mime.xml
find %{buildroot}%{_datadir}/ffDiaporama -name '*.xml' -exec chmod -x {} \;
find %{buildroot}%{_datadir}/ffDiaporama -name '*.txt' -exec chmod -x {} \;
find %{buildroot}%{_datadir}/ffDiaporama -name '*ffpreset' -exec chmod -x {} \;



%files
%doc licences.txt licence.rtf 
%{_bindir}/%{oname}
%{_datadir}/%{oname}
%{_datadir}/mime/packages/%{oname}-mime.xml
%{_datadir}/applications/%{oname}.desktop
%{_datadir}/icons/hicolor/*/apps/ffdiaporama.png




