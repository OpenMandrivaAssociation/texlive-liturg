# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/liturg
# catalog-date 2008-09-08 11:32:46 +0200
# catalog-license lppl
# catalog-version 1.0
Name:		texlive-liturg
Version:	1.0
Release:	2
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0-2
+ Revision: 753405
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0-1
+ Revision: 718872
- texlive-liturg
- texlive-liturg
- texlive-liturg
- texlive-liturg

