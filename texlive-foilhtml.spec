%global tl_name foilhtml
%global tl_revision 61937

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.2
Release:	%{tl_revision}.1
Summary:	Interface between foiltex and LaTeX2HTML
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/foilhtml
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/foilhtml.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/foilhtml.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/foilhtml.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides integration between FoilTeX and LaTeX2HTML, adding sectioning
commands and elements of logical formatting to FoilTeX and providing
support for FoilTeX commands in LaTeX2HTML.

