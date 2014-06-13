# revision 26422
# category Package
# catalog-ctan /macros/latex/contrib/mwe
# catalog-date 2012-05-15 15:44:48 +0200
# catalog-license lppl1.3
# catalog-version 0.3
Name:		texlive-mwe
Version:	0.3
Release:	7
Summary:	Packages and image files for MWEs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mwe
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mwe.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mwe.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mwe.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The bundle provides several files useful when creating a
minimal working example (MWE). The package itself loads a small
set of packages often used when creating MWEs. In addition, a
range of images are provided, which will be installed in the
TEXMF tree, so that they may be used in any (La)TeX document.
This allows different users to share MWEs which include image
commands, without the need to share image files or to use
replacement code.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mwe/example-grid-100x100bp.eps
%{_texmfdistdir}/tex/latex/mwe/example-grid-100x100bp.jpg
%{_texmfdistdir}/tex/latex/mwe/example-grid-100x100bp.pdf
%{_texmfdistdir}/tex/latex/mwe/example-grid-100x100bp.png
%{_texmfdistdir}/tex/latex/mwe/example-grid-100x100bp.tex
%{_texmfdistdir}/tex/latex/mwe/example-grid-100x100pt.eps
%{_texmfdistdir}/tex/latex/mwe/example-grid-100x100pt.jpg
%{_texmfdistdir}/tex/latex/mwe/example-grid-100x100pt.pdf
%{_texmfdistdir}/tex/latex/mwe/example-grid-100x100pt.png
%{_texmfdistdir}/tex/latex/mwe/example-grid-100x100pt.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-10x16.eps
%{_texmfdistdir}/tex/latex/mwe/example-image-10x16.jpg
%{_texmfdistdir}/tex/latex/mwe/example-image-10x16.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-10x16.png
%{_texmfdistdir}/tex/latex/mwe/example-image-10x16.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-16x10.eps
%{_texmfdistdir}/tex/latex/mwe/example-image-16x10.jpg
%{_texmfdistdir}/tex/latex/mwe/example-image-16x10.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-16x10.png
%{_texmfdistdir}/tex/latex/mwe/example-image-16x10.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-16x9.eps
%{_texmfdistdir}/tex/latex/mwe/example-image-16x9.jpg
%{_texmfdistdir}/tex/latex/mwe/example-image-16x9.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-16x9.png
%{_texmfdistdir}/tex/latex/mwe/example-image-16x9.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-1x1.eps
%{_texmfdistdir}/tex/latex/mwe/example-image-1x1.jpg
%{_texmfdistdir}/tex/latex/mwe/example-image-1x1.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-1x1.png
%{_texmfdistdir}/tex/latex/mwe/example-image-1x1.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-4x3.eps
%{_texmfdistdir}/tex/latex/mwe/example-image-4x3.jpg
%{_texmfdistdir}/tex/latex/mwe/example-image-4x3.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-4x3.png
%{_texmfdistdir}/tex/latex/mwe/example-image-4x3.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-9x16.eps
%{_texmfdistdir}/tex/latex/mwe/example-image-9x16.jpg
%{_texmfdistdir}/tex/latex/mwe/example-image-9x16.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-9x16.png
%{_texmfdistdir}/tex/latex/mwe/example-image-9x16.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-a.eps
%{_texmfdistdir}/tex/latex/mwe/example-image-a.jpg
%{_texmfdistdir}/tex/latex/mwe/example-image-a.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-a.png
%{_texmfdistdir}/tex/latex/mwe/example-image-a.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-a3-landscape.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-a3-landscape.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-a3.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-a3.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-a4-landscape.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-a4-landscape.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-a4.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-a4.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-a5-landscape.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-a5-landscape.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-a5.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-a5.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-b.eps
%{_texmfdistdir}/tex/latex/mwe/example-image-b.jpg
%{_texmfdistdir}/tex/latex/mwe/example-image-b.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-b.png
%{_texmfdistdir}/tex/latex/mwe/example-image-b.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-c.eps
%{_texmfdistdir}/tex/latex/mwe/example-image-c.jpg
%{_texmfdistdir}/tex/latex/mwe/example-image-c.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-c.png
%{_texmfdistdir}/tex/latex/mwe/example-image-c.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-golden-upright.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-golden-upright.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-golden.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-golden.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-letter-landscape.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-letter-landscape.tex
%{_texmfdistdir}/tex/latex/mwe/example-image-letter.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image-letter.tex
%{_texmfdistdir}/tex/latex/mwe/example-image.eps
%{_texmfdistdir}/tex/latex/mwe/example-image.jpg
%{_texmfdistdir}/tex/latex/mwe/example-image.pdf
%{_texmfdistdir}/tex/latex/mwe/example-image.png
%{_texmfdistdir}/tex/latex/mwe/example-image.tex
%{_texmfdistdir}/tex/latex/mwe/mwe.sty
%doc %{_texmfdistdir}/doc/latex/mwe/INSTALL
%doc %{_texmfdistdir}/doc/latex/mwe/README
%doc %{_texmfdistdir}/doc/latex/mwe/mwe.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mwe/mwe.dtx
%doc %{_texmfdistdir}/source/latex/mwe/mwe.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
