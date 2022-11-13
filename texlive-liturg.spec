Name:		texlive-liturg
Version:	15878
Release:	1
Summary:	Support for typesetting Catholic liturgical texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/liturg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/liturg.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/liturg.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/liturg.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The packages offers simple macros for typesetting Catholic
liturgical texts, particularly Missal and Breviary texts. The
package assumes availability of Latin typesetting packages.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/liturg/liturg.sty
%doc %{_texmfdistdir}/doc/latex/liturg/README
%doc %{_texmfdistdir}/doc/latex/liturg/liturg.pdf
%doc %{_texmfdistdir}/doc/latex/liturg/test.tex
#- source
%doc %{_texmfdistdir}/source/latex/liturg/liturg.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
