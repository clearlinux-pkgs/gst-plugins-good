#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v21
# autospec commit: f4a13a5
#
# Source0 file verified with key 0x5D2EEE6F6F349D7C (tim@centricular.com)
#
Name     : gst-plugins-good
Version  : 1.24.11
Release  : 132
URL      : https://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-1.24.11.tar.xz
Source0  : https://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-1.24.11.tar.xz
Source1  : https://gstreamer.freedesktop.org/src/gst-plugins-good/gst-plugins-good-1.24.11.tar.xz.asc
Source2  : 5D2EEE6F6F349D7C.pkey
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause LGPL-2.1 MIT
Requires: gst-plugins-good-data = %{version}-%{release}
Requires: gst-plugins-good-lib = %{version}-%{release}
Requires: gst-plugins-good-license = %{version}-%{release}
Requires: gst-plugins-good-locales = %{version}-%{release}
BuildRequires : buildreq-kde
BuildRequires : buildreq-meson
BuildRequires : bzip2-dev
BuildRequires : gdk-pixbuf
BuildRequires : glu-dev
BuildRequires : gnupg
BuildRequires : gstreamer-dev
BuildRequires : libjpeg-turbo-dev
BuildRequires : mesa-dev
BuildRequires : mpg123-dev
BuildRequires : nasm-bin
BuildRequires : orc-dev
BuildRequires : pkgconfig(cairo-gobject)
BuildRequires : pkgconfig(flac)
BuildRequires : pkgconfig(gdk-pixbuf-2.0)
BuildRequires : pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libpng)
BuildRequires : pkgconfig(libpulse)
BuildRequires : pkgconfig(taglib)
BuildRequires : pkgconfig(valgrind)
BuildRequires : pkgconfig(vpx)
BuildRequires : pkgconfig(xtst)
BuildRequires : qtbase-extras
BuildRequires : speex-dev
BuildRequires : v4l-utils-dev
BuildRequires : valgrind
BuildRequires : wavpack-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Compiling AMRNB:
================
To compile the amrnb plugin, you need the opencore-amrnb development package.
If your distribution does not provide this package, you can download the
source code from "http://sourceforge.net/projects/opencore-amr".

%package data
Summary: data components for the gst-plugins-good package.
Group: Data

%description data
data components for the gst-plugins-good package.


%package lib
Summary: lib components for the gst-plugins-good package.
Group: Libraries
Requires: gst-plugins-good-data = %{version}-%{release}
Requires: gst-plugins-good-license = %{version}-%{release}

%description lib
lib components for the gst-plugins-good package.


%package license
Summary: license components for the gst-plugins-good package.
Group: Default

%description license
license components for the gst-plugins-good package.


%package locales
Summary: locales components for the gst-plugins-good package.
Group: Default

%description locales
locales components for the gst-plugins-good package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 5D2EEE6F6F349D7C' gpg.status
%setup -q -n gst-plugins-good-1.24.11
cd %{_builddir}/gst-plugins-good-1.24.11
pushd ..
cp -a gst-plugins-good-1.24.11 buildavx2
popd
pushd ..
cp -a gst-plugins-good-1.24.11 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1736270042
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dv4l2-gudev=disabled  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dv4l2-gudev=disabled  builddiravx2
ninja -v -C builddiravx2
GOAMD64=v4
CFLAGS="$CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 " CXXFLAGS="$CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 " LDFLAGS="$LDFLAGS -march=x86-64-v4 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dv4l2-gudev=disabled  builddiravx512
ninja -v -C builddiravx512

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :
cd ../buildavx2;
meson test -C builddir --print-errorlogs || : || :
cd ../buildavx512;
meson test -C builddir --print-errorlogs || : || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gst-plugins-good
cp %{_builddir}/gst-plugins-good-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gst-plugins-good/545f380fb332eb41236596500913ff8d582e3ead || :
cp %{_builddir}/gst-plugins-good-%{version}/gst/rtp/dboolhuff.LICENSE %{buildroot}/usr/share/package-licenses/gst-plugins-good/057705e31a95ff560d92f8abc2e62d2894fba796 || :
cp %{_builddir}/gst-plugins-good-%{version}/gst/rtsp/COPYING.MIT %{buildroot}/usr/share/package-licenses/gst-plugins-good/f6e583b41a8e91303bf19c8b17c0086872de5977 || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v4
DESTDIR=%{buildroot}-v4 ninja -C builddiravx512 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
%find_lang gst-plugins-good-1.0
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/gstreamer-1.0/presets/GstIirEqualizer10Bands.prs
/usr/share/gstreamer-1.0/presets/GstIirEqualizer3Bands.prs
/usr/share/gstreamer-1.0/presets/GstQTMux.prs
/usr/share/gstreamer-1.0/presets/GstVP8Enc.prs

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/gstreamer-1.0/libgstadaptivedemux2.so
/V3/usr/lib64/gstreamer-1.0/libgstalaw.so
/V3/usr/lib64/gstreamer-1.0/libgstalpha.so
/V3/usr/lib64/gstreamer-1.0/libgstalphacolor.so
/V3/usr/lib64/gstreamer-1.0/libgstapetag.so
/V3/usr/lib64/gstreamer-1.0/libgstaudiofx.so
/V3/usr/lib64/gstreamer-1.0/libgstaudioparsers.so
/V3/usr/lib64/gstreamer-1.0/libgstauparse.so
/V3/usr/lib64/gstreamer-1.0/libgstautodetect.so
/V3/usr/lib64/gstreamer-1.0/libgstavi.so
/V3/usr/lib64/gstreamer-1.0/libgstcairo.so
/V3/usr/lib64/gstreamer-1.0/libgstcutter.so
/V3/usr/lib64/gstreamer-1.0/libgstdebug.so
/V3/usr/lib64/gstreamer-1.0/libgstdeinterlace.so
/V3/usr/lib64/gstreamer-1.0/libgstdtmf.so
/V3/usr/lib64/gstreamer-1.0/libgsteffectv.so
/V3/usr/lib64/gstreamer-1.0/libgstequalizer.so
/V3/usr/lib64/gstreamer-1.0/libgstflac.so
/V3/usr/lib64/gstreamer-1.0/libgstflv.so
/V3/usr/lib64/gstreamer-1.0/libgstflxdec.so
/V3/usr/lib64/gstreamer-1.0/libgstgdkpixbuf.so
/V3/usr/lib64/gstreamer-1.0/libgstgoom.so
/V3/usr/lib64/gstreamer-1.0/libgstgoom2k1.so
/V3/usr/lib64/gstreamer-1.0/libgstgtk.so
/V3/usr/lib64/gstreamer-1.0/libgsticydemux.so
/V3/usr/lib64/gstreamer-1.0/libgstid3demux.so
/V3/usr/lib64/gstreamer-1.0/libgstimagefreeze.so
/V3/usr/lib64/gstreamer-1.0/libgstinterleave.so
/V3/usr/lib64/gstreamer-1.0/libgstisomp4.so
/V3/usr/lib64/gstreamer-1.0/libgstjack.so
/V3/usr/lib64/gstreamer-1.0/libgstjpeg.so
/V3/usr/lib64/gstreamer-1.0/libgstlevel.so
/V3/usr/lib64/gstreamer-1.0/libgstmatroska.so
/V3/usr/lib64/gstreamer-1.0/libgstmonoscope.so
/V3/usr/lib64/gstreamer-1.0/libgstmpg123.so
/V3/usr/lib64/gstreamer-1.0/libgstmulaw.so
/V3/usr/lib64/gstreamer-1.0/libgstmultifile.so
/V3/usr/lib64/gstreamer-1.0/libgstmultipart.so
/V3/usr/lib64/gstreamer-1.0/libgstnavigationtest.so
/V3/usr/lib64/gstreamer-1.0/libgstoss4.so
/V3/usr/lib64/gstreamer-1.0/libgstossaudio.so
/V3/usr/lib64/gstreamer-1.0/libgstpng.so
/V3/usr/lib64/gstreamer-1.0/libgstpulseaudio.so
/V3/usr/lib64/gstreamer-1.0/libgstqml6.so
/V3/usr/lib64/gstreamer-1.0/libgstreplaygain.so
/V3/usr/lib64/gstreamer-1.0/libgstrtp.so
/V3/usr/lib64/gstreamer-1.0/libgstrtpmanager.so
/V3/usr/lib64/gstreamer-1.0/libgstrtsp.so
/V3/usr/lib64/gstreamer-1.0/libgstshapewipe.so
/V3/usr/lib64/gstreamer-1.0/libgstsmpte.so
/V3/usr/lib64/gstreamer-1.0/libgstsoup.so
/V3/usr/lib64/gstreamer-1.0/libgstspectrum.so
/V3/usr/lib64/gstreamer-1.0/libgstspeex.so
/V3/usr/lib64/gstreamer-1.0/libgsttaglib.so
/V3/usr/lib64/gstreamer-1.0/libgstudp.so
/V3/usr/lib64/gstreamer-1.0/libgstvideo4linux2.so
/V3/usr/lib64/gstreamer-1.0/libgstvideobox.so
/V3/usr/lib64/gstreamer-1.0/libgstvideocrop.so
/V3/usr/lib64/gstreamer-1.0/libgstvideofilter.so
/V3/usr/lib64/gstreamer-1.0/libgstvideomixer.so
/V3/usr/lib64/gstreamer-1.0/libgstvpx.so
/V3/usr/lib64/gstreamer-1.0/libgstwavenc.so
/V3/usr/lib64/gstreamer-1.0/libgstwavpack.so
/V3/usr/lib64/gstreamer-1.0/libgstwavparse.so
/V3/usr/lib64/gstreamer-1.0/libgstximagesrc.so
/V3/usr/lib64/gstreamer-1.0/libgstxingmux.so
/V3/usr/lib64/gstreamer-1.0/libgsty4menc.so
/V4/usr/lib64/gstreamer-1.0/libgstadaptivedemux2.so
/V4/usr/lib64/gstreamer-1.0/libgstalaw.so
/V4/usr/lib64/gstreamer-1.0/libgstalpha.so
/V4/usr/lib64/gstreamer-1.0/libgstalphacolor.so
/V4/usr/lib64/gstreamer-1.0/libgstapetag.so
/V4/usr/lib64/gstreamer-1.0/libgstaudiofx.so
/V4/usr/lib64/gstreamer-1.0/libgstaudioparsers.so
/V4/usr/lib64/gstreamer-1.0/libgstauparse.so
/V4/usr/lib64/gstreamer-1.0/libgstautodetect.so
/V4/usr/lib64/gstreamer-1.0/libgstavi.so
/V4/usr/lib64/gstreamer-1.0/libgstcairo.so
/V4/usr/lib64/gstreamer-1.0/libgstcutter.so
/V4/usr/lib64/gstreamer-1.0/libgstdebug.so
/V4/usr/lib64/gstreamer-1.0/libgstdeinterlace.so
/V4/usr/lib64/gstreamer-1.0/libgstdtmf.so
/V4/usr/lib64/gstreamer-1.0/libgsteffectv.so
/V4/usr/lib64/gstreamer-1.0/libgstequalizer.so
/V4/usr/lib64/gstreamer-1.0/libgstflac.so
/V4/usr/lib64/gstreamer-1.0/libgstflv.so
/V4/usr/lib64/gstreamer-1.0/libgstflxdec.so
/V4/usr/lib64/gstreamer-1.0/libgstgdkpixbuf.so
/V4/usr/lib64/gstreamer-1.0/libgstgoom.so
/V4/usr/lib64/gstreamer-1.0/libgstgoom2k1.so
/V4/usr/lib64/gstreamer-1.0/libgstgtk.so
/V4/usr/lib64/gstreamer-1.0/libgsticydemux.so
/V4/usr/lib64/gstreamer-1.0/libgstid3demux.so
/V4/usr/lib64/gstreamer-1.0/libgstimagefreeze.so
/V4/usr/lib64/gstreamer-1.0/libgstinterleave.so
/V4/usr/lib64/gstreamer-1.0/libgstisomp4.so
/V4/usr/lib64/gstreamer-1.0/libgstjack.so
/V4/usr/lib64/gstreamer-1.0/libgstjpeg.so
/V4/usr/lib64/gstreamer-1.0/libgstlevel.so
/V4/usr/lib64/gstreamer-1.0/libgstmatroska.so
/V4/usr/lib64/gstreamer-1.0/libgstmonoscope.so
/V4/usr/lib64/gstreamer-1.0/libgstmpg123.so
/V4/usr/lib64/gstreamer-1.0/libgstmulaw.so
/V4/usr/lib64/gstreamer-1.0/libgstmultifile.so
/V4/usr/lib64/gstreamer-1.0/libgstmultipart.so
/V4/usr/lib64/gstreamer-1.0/libgstnavigationtest.so
/V4/usr/lib64/gstreamer-1.0/libgstoss4.so
/V4/usr/lib64/gstreamer-1.0/libgstossaudio.so
/V4/usr/lib64/gstreamer-1.0/libgstpng.so
/V4/usr/lib64/gstreamer-1.0/libgstpulseaudio.so
/V4/usr/lib64/gstreamer-1.0/libgstqml6.so
/V4/usr/lib64/gstreamer-1.0/libgstreplaygain.so
/V4/usr/lib64/gstreamer-1.0/libgstrtp.so
/V4/usr/lib64/gstreamer-1.0/libgstrtpmanager.so
/V4/usr/lib64/gstreamer-1.0/libgstrtsp.so
/V4/usr/lib64/gstreamer-1.0/libgstshapewipe.so
/V4/usr/lib64/gstreamer-1.0/libgstsmpte.so
/V4/usr/lib64/gstreamer-1.0/libgstsoup.so
/V4/usr/lib64/gstreamer-1.0/libgstspectrum.so
/V4/usr/lib64/gstreamer-1.0/libgstspeex.so
/V4/usr/lib64/gstreamer-1.0/libgsttaglib.so
/V4/usr/lib64/gstreamer-1.0/libgstudp.so
/V4/usr/lib64/gstreamer-1.0/libgstvideo4linux2.so
/V4/usr/lib64/gstreamer-1.0/libgstvideobox.so
/V4/usr/lib64/gstreamer-1.0/libgstvideocrop.so
/V4/usr/lib64/gstreamer-1.0/libgstvideofilter.so
/V4/usr/lib64/gstreamer-1.0/libgstvideomixer.so
/V4/usr/lib64/gstreamer-1.0/libgstvpx.so
/V4/usr/lib64/gstreamer-1.0/libgstwavenc.so
/V4/usr/lib64/gstreamer-1.0/libgstwavpack.so
/V4/usr/lib64/gstreamer-1.0/libgstwavparse.so
/V4/usr/lib64/gstreamer-1.0/libgstximagesrc.so
/V4/usr/lib64/gstreamer-1.0/libgstxingmux.so
/V4/usr/lib64/gstreamer-1.0/libgsty4menc.so
/usr/lib64/gstreamer-1.0/libgstadaptivedemux2.so
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
/usr/lib64/gstreamer-1.0/libgstgtk.so
/usr/lib64/gstreamer-1.0/libgsticydemux.so
/usr/lib64/gstreamer-1.0/libgstid3demux.so
/usr/lib64/gstreamer-1.0/libgstimagefreeze.so
/usr/lib64/gstreamer-1.0/libgstinterleave.so
/usr/lib64/gstreamer-1.0/libgstisomp4.so
/usr/lib64/gstreamer-1.0/libgstjack.so
/usr/lib64/gstreamer-1.0/libgstjpeg.so
/usr/lib64/gstreamer-1.0/libgstlevel.so
/usr/lib64/gstreamer-1.0/libgstmatroska.so
/usr/lib64/gstreamer-1.0/libgstmonoscope.so
/usr/lib64/gstreamer-1.0/libgstmpg123.so
/usr/lib64/gstreamer-1.0/libgstmulaw.so
/usr/lib64/gstreamer-1.0/libgstmultifile.so
/usr/lib64/gstreamer-1.0/libgstmultipart.so
/usr/lib64/gstreamer-1.0/libgstnavigationtest.so
/usr/lib64/gstreamer-1.0/libgstoss4.so
/usr/lib64/gstreamer-1.0/libgstossaudio.so
/usr/lib64/gstreamer-1.0/libgstpng.so
/usr/lib64/gstreamer-1.0/libgstpulseaudio.so
/usr/lib64/gstreamer-1.0/libgstqml6.so
/usr/lib64/gstreamer-1.0/libgstreplaygain.so
/usr/lib64/gstreamer-1.0/libgstrtp.so
/usr/lib64/gstreamer-1.0/libgstrtpmanager.so
/usr/lib64/gstreamer-1.0/libgstrtsp.so
/usr/lib64/gstreamer-1.0/libgstshapewipe.so
/usr/lib64/gstreamer-1.0/libgstsmpte.so
/usr/lib64/gstreamer-1.0/libgstsoup.so
/usr/lib64/gstreamer-1.0/libgstspectrum.so
/usr/lib64/gstreamer-1.0/libgstspeex.so
/usr/lib64/gstreamer-1.0/libgsttaglib.so
/usr/lib64/gstreamer-1.0/libgstudp.so
/usr/lib64/gstreamer-1.0/libgstvideo4linux2.so
/usr/lib64/gstreamer-1.0/libgstvideobox.so
/usr/lib64/gstreamer-1.0/libgstvideocrop.so
/usr/lib64/gstreamer-1.0/libgstvideofilter.so
/usr/lib64/gstreamer-1.0/libgstvideomixer.so
/usr/lib64/gstreamer-1.0/libgstvpx.so
/usr/lib64/gstreamer-1.0/libgstwavenc.so
/usr/lib64/gstreamer-1.0/libgstwavpack.so
/usr/lib64/gstreamer-1.0/libgstwavparse.so
/usr/lib64/gstreamer-1.0/libgstximagesrc.so
/usr/lib64/gstreamer-1.0/libgstxingmux.so
/usr/lib64/gstreamer-1.0/libgsty4menc.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gst-plugins-good/057705e31a95ff560d92f8abc2e62d2894fba796
/usr/share/package-licenses/gst-plugins-good/545f380fb332eb41236596500913ff8d582e3ead
/usr/share/package-licenses/gst-plugins-good/f6e583b41a8e91303bf19c8b17c0086872de5977

%files locales -f gst-plugins-good-1.0.lang
%defattr(-,root,root,-)

