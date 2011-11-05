# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/liturg
# catalog-date 2008-09-08 11:32:46 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-liturg
Version:	1.0
Release:	1
Summary:	Support for typesetting Catholic liturgical texts
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/liturg
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/liturg.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/liturg.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/liturg.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
The packages offers simple macros for typesetting Catholic
liturgical texts, particularly Missal and Breviary texts. The
package assumes availability of Latin typesetting packages.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/liturg/liturg.sty
%doc %{_texmfdistdir}/doc/latex/liturg/README
%doc %{_texmfdistdir}/doc/latex/liturg/liturg.pdf
%doc %{_texmfdistdir}/doc/latex/liturg/test.tex
#- source
%doc %{_texmfdistdir}/source/latex/liturg/liturg.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
