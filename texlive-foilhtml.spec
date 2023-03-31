Name:		texlive-foilhtml
Version:	61937
Release:	2
Summary:	Interface between foiltex and LaTeX2HTML
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/foilhtml
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foilhtml.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foilhtml.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foilhtml.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides integration between FoilTeX and LaTeX2HTML, adding
sectioning commands and elements of logical formatting to
FoilTeX and providing support for FoilTeX commands in
LaTeX2HTML.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/foilhtml/foilhtml.cfg
%{_texmfdistdir}/tex/latex/foilhtml/foilhtml.sty
%doc %{_texmfdistdir}/doc/latex/foilhtml/foilhtml-96.perl
%doc %{_texmfdistdir}/doc/latex/foilhtml/foils-97.perl
%doc %{_texmfdistdir}/doc/latex/foilhtml/foils.perl
%doc %{_texmfdistdir}/doc/latex/foilhtml/readme.v12
#- source
%doc %{_texmfdistdir}/source/latex/foilhtml/foilhtml.drv
%doc %{_texmfdistdir}/source/latex/foilhtml/foilhtml.dtx
%doc %{_texmfdistdir}/source/latex/foilhtml/foilhtml.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
