%global tl_name liturg
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Support for typesetting Catholic liturgical texts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/liturg
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/liturg.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/liturg.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/liturg.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The packages offers simple macros for typesetting Catholic liturgical
texts, particularly Missal and Breviary texts. The package assumes
availability of Latin typesetting packages.

