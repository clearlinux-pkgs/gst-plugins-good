#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x0668CC1486C2D7B5 (slomo@debian.org)
#
Name     : gst-plugins-good
Version  : 1.12.1
Release  : 19
URL      : https://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-1.12.1.tar.xz
Source0  : https://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-1.12.1.tar.xz
Source99 : https://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-1.12.1.tar.xz.asc
Summary  : Streaming media framework, good plugins, uninstalled
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1
Requires: gst-plugins-good-lib
Requires: gst-plugins-good-data
Requires: gst-plugins-good-doc
Requires: gst-plugins-good-locales
BuildRequires : bzip2-dev
BuildRequires : docbook-xml
BuildRequires : gdk-pixbuf
BuildRequires : glu-dev
BuildRequires : gstreamer-dev
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : libxslt-bin
BuildRequires : mesa-dev
BuildRequires : orc-dev
BuildRequires : pkgconfig(cairo)
BuildRequires : pkgconfig(flac)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(gtk+-x11-3.0)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(libsoup-2.4)
BuildRequires : pkgconfig(x11)
BuildRequires : speex-dev
BuildRequires : valgrind

%description
GStreamer 1.11.x development series
WHAT IT IS
----------
This is GStreamer, a framework for streaming media.

%package data
Summary: data components for the gst-plugins-good package.
Group: Data

%description data
data components for the gst-plugins-good package.


%package doc
Summary: doc components for the gst-plugins-good package.
Group: Documentation

%description doc
doc components for the gst-plugins-good package.


%package lib
Summary: lib components for the gst-plugins-good package.
Group: Libraries
Requires: gst-plugins-good-data

%description lib
lib components for the gst-plugins-good package.


%package locales
Summary: locales components for the gst-plugins-good package.
Group: Default

%description locales
locales components for the gst-plugins-good package.


%prep
%setup -q -n gst-plugins-good-1.12.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1497969245
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1497969245
rm -rf %{buildroot}
%make_install
%find_lang gst-plugins-good-1.0

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/gstreamer-1.0/presets/GstIirEqualizer10Bands.prs
/usr/share/gstreamer-1.0/presets/GstIirEqualizer3Bands.prs
/usr/share/gstreamer-1.0/presets/GstQTMux.prs

%files doc
%defattr(-,root,root,-)
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/ch01.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/ch02.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-1.0.devhelp2
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-3gppmux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-aacparse.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-aasink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-ac3parse.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-agingtv.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-alawdec.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-alawenc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-alpha.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-alphacolor.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-amrparse.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-apedemux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-apev2mux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-aspectratiocrop.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-asteriskh263.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-audioamplify.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-audiochebband.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-audiocheblimit.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-audiodynamic.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-audioecho.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-audiofirfilter.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-audioiirfilter.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-audioinvert.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-audiokaraoke.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-audiopanorama.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-audiowsincband.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-audiowsinclimit.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-auparse.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-autoaudiosink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-autoaudiosrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-autovideosink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-autovideosrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-avidemux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-avimux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-avisubtitle.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-breakmydata.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-cacasink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-cairooverlay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-capssetter.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-cpureport.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-cutter.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-dcaparse.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-deinterlace.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-deinterleave.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-dicetv.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-directsoundsink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-dtmfsrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-dv1394src.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-dvdec.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-dvdemux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-dynudpsink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-edgetv.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-equalizer-10bands.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-equalizer-3bands.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-equalizer-nbands.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-flacdec.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-flacenc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-flacparse.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-flactag.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-flvdemux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-flvmux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-flxdec.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-gamma.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-gdkpixbufdec.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-gdkpixbufoverlay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-gdkpixbufsink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-goom.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-goom2k1.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-hdv1394src.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-icydemux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-id3demux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-id3v2mux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-iirequalizer.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-imagefreeze.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-interleave.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-ismlmux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-jackaudiosink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-jackaudiosrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-jpegdec.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-jpegenc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-level.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-matroskademux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-matroskamux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-matroskaparse.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-mj2mux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-monoscope.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-mp4mux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-mpegaudioparse.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-mulawdec.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-mulawenc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-multifilesink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-multifilesrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-multipartdemux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-multipartmux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-multiudpsink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-navigationtest.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-navseek.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-optv.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-oss4sink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-oss4src.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-osssink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-osssrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-osxaudiosink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-osxaudiosrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-osxvideosink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-1394.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-aasink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-alaw.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-alpha.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-alphacolor.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-apetag.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-audiofx.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-audioparsers.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-auparse.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-autodetect.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-avi.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-cacasink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-cairo.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-cutter.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-debug.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-deinterlace.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-directsound.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-dtmf.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-dv.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-effectv.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-equalizer.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-flac.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-flv.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-flxdec.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-gdkpixbuf.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-goom.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-goom2k1.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-icydemux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-id3demux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-imagefreeze.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-interleave.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-isomp4.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-jack.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-jpeg.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-level.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-matroska.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-monoscope.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-mulaw.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-multifile.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-multipart.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-navigationtest.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-oss4.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-ossaudio.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-osxaudio.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-osxvideo.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-png.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-pulseaudio.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-replaygain.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-rtp.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-rtpmanager.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-rtsp.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-shapewipe.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-shout2.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-smpte.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-soup.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-spectrum.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-speex.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-taglib.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-udp.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-video4linux2.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-videobox.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-videocrop.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-videofilter.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-videomixer.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-vpx.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-waveform.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-wavenc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-wavpack.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-wavparse.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-ximagesrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-plugin-y4menc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-pngdec.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-pngenc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-progressreport.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-pulsesink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-pulsesrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-pushfilesrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-qtdemux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-qtmoovrecover.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-qtmux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-quarktv.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-radioactv.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-revtv.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rganalysis.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rglimiter.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rgvolume.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rippletv.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rndbuffersize.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpL16depay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpL16pay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpL24depay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpL24pay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpac3depay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpac3pay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpamrdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpamrpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpbin.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpbvdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpbvpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpceltdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpceltpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpdec.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpdtmfdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpdtmfmux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpdtmfsrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpdvdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpdvpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpg722depay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpg722pay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpg723depay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpg723pay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpg726depay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpg726pay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpg729depay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpg729pay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpgsmdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpgsmpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpgstdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpgstpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtph261depay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtph261pay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtph263depay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtph263pay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtph263pdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtph263ppay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtph264depay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtph264pay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtph265depay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtph265pay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpilbcdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpilbcpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpj2kdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpj2kpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpjitterbuffer.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpjpegdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpjpegpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpklvdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpklvpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpmp1sdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpmp2tdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpmp2tpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpmp4adepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpmp4apay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpmp4gdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpmp4gpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpmp4vdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpmp4vpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpmpadepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpmpapay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpmparobustdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpmpvdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpmpvpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpmux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpopusdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpopuspay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtppcmadepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtppcmapay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtppcmudepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtppcmupay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpptdemux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpqcelpdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpqdm2depay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtprtxqueue.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtprtxreceive.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtprtxsend.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpsbcdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpsbcpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpsession.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpsirendepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpsirenpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpspeexdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpspeexpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpssrcdemux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpstreamdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpstreampay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpsv3vdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtptheoradepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtptheorapay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpvorbisdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpvorbispay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpvp8depay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpvp8pay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpvp9depay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpvp9pay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpvrawdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpvrawpay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtpxqtdepay.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-rtspsrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-sbcparse.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-scaletempo.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-shagadelictv.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-shapewipe.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-shout2send.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-smpte.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-smptealpha.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-souphttpclientsink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-souphttpsrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-spectrum.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-speexdec.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-speexenc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-splitfilesrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-splitmuxsink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-splitmuxsrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-streaktv.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-taginject.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-testsink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-udpsink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-udpsrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-v4l2radio.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-v4l2sink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-v4l2src.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-vertigotv.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-videobalance.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-videobox.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-videocrop.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-videoflip.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-videomedian.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-videomixer.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-vp8dec.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-vp8enc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-vp9dec.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-vp9enc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-warptv.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-waveformsink.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-wavenc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-wavpackdec.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-wavpackenc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-wavpackparse.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-wavparse.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-webmmux.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-ximagesrc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/gst-plugins-good-plugins-y4menc.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/home.png
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/index.html
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/left-insensitive.png
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/left.png
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/right-insensitive.png
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/right.png
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/style.css
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/up-insensitive.png
/usr/share/gtk-doc/html/gst-plugins-good-plugins-1.0/up.png

%files lib
%defattr(-,root,root,-)
/usr/lib64/gstreamer-1.0/libgstalaw.so
/usr/lib64/gstreamer-1.0/libgstalpha.so
/usr/lib64/gstreamer-1.0/libgstalphacolor.so
/usr/lib64/gstreamer-1.0/libgstapetag.so
/usr/lib64/gstreamer-1.0/libgstaudiofx.so
/usr/lib64/gstreamer-1.0/libgstaudioparsers.so
/usr/lib64/gstreamer-1.0/libgstauparse.so
/usr/lib64/gstreamer-1.0/libgstautodetect.so
/usr/lib64/gstreamer-1.0/libgstavi.so
/usr/lib64/gstreamer-1.0/libgstcairo.so
/usr/lib64/gstreamer-1.0/libgstcutter.so
/usr/lib64/gstreamer-1.0/libgstdebug.so
/usr/lib64/gstreamer-1.0/libgstdeinterlace.so
/usr/lib64/gstreamer-1.0/libgstdtmf.so
/usr/lib64/gstreamer-1.0/libgsteffectv.so
/usr/lib64/gstreamer-1.0/libgstequalizer.so
/usr/lib64/gstreamer-1.0/libgstflac.so
/usr/lib64/gstreamer-1.0/libgstflv.so
/usr/lib64/gstreamer-1.0/libgstflxdec.so
/usr/lib64/gstreamer-1.0/libgstgdkpixbuf.so
/usr/lib64/gstreamer-1.0/libgstgoom.so
/usr/lib64/gstreamer-1.0/libgstgoom2k1.so
/usr/lib64/gstreamer-1.0/libgsticydemux.so
/usr/lib64/gstreamer-1.0/libgstid3demux.so
/usr/lib64/gstreamer-1.0/libgstimagefreeze.so
/usr/lib64/gstreamer-1.0/libgstinterleave.so
/usr/lib64/gstreamer-1.0/libgstisomp4.so
/usr/lib64/gstreamer-1.0/libgstjpeg.so
/usr/lib64/gstreamer-1.0/libgstlevel.so
/usr/lib64/gstreamer-1.0/libgstmatroska.so
/usr/lib64/gstreamer-1.0/libgstmulaw.so
/usr/lib64/gstreamer-1.0/libgstmultifile.so
/usr/lib64/gstreamer-1.0/libgstmultipart.so
/usr/lib64/gstreamer-1.0/libgstnavigationtest.so
/usr/lib64/gstreamer-1.0/libgstoss4.so
/usr/lib64/gstreamer-1.0/libgstossaudio.so
/usr/lib64/gstreamer-1.0/libgstpng.so
/usr/lib64/gstreamer-1.0/libgstpulseaudio.so
/usr/lib64/gstreamer-1.0/libgstreplaygain.so
/usr/lib64/gstreamer-1.0/libgstrtp.so
/usr/lib64/gstreamer-1.0/libgstrtpmanager.so
/usr/lib64/gstreamer-1.0/libgstrtsp.so
/usr/lib64/gstreamer-1.0/libgstshapewipe.so
/usr/lib64/gstreamer-1.0/libgstsmpte.so
/usr/lib64/gstreamer-1.0/libgstsoup.so
/usr/lib64/gstreamer-1.0/libgstspectrum.so
/usr/lib64/gstreamer-1.0/libgstudp.so
/usr/lib64/gstreamer-1.0/libgstvideo4linux2.so
/usr/lib64/gstreamer-1.0/libgstvideobox.so
/usr/lib64/gstreamer-1.0/libgstvideocrop.so
/usr/lib64/gstreamer-1.0/libgstvideofilter.so
/usr/lib64/gstreamer-1.0/libgstvideomixer.so
/usr/lib64/gstreamer-1.0/libgstwavenc.so
/usr/lib64/gstreamer-1.0/libgstwavparse.so
/usr/lib64/gstreamer-1.0/libgstximagesrc.so
/usr/lib64/gstreamer-1.0/libgsty4menc.so

%files locales -f gst-plugins-good-1.0.lang
%defattr(-,root,root,-)

