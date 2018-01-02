Name:		texlive-mwe
Version:	0.4
Release:	1
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
%{_texmfdistdir}/tex/latex/mwe
%doc %{_texmfdistdir}/doc/latex/mwe
#- source
%doc %{_texmfdistdir}/source/latex/mwe

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
