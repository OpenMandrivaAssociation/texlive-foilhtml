# revision 21855
# category Package
# catalog-ctan /macros/latex/contrib/foilhtml
# catalog-date 2007-01-05 16:07:21 +0100
# catalog-license lppl
# catalog-version 1.2
Name:		texlive-foilhtml
Version:	1.2
Release:	8
Summary:	Interface between foiltex and LaTeX2HTML
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/foilhtml
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foilhtml.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foilhtml.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/foilhtml.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.2-2
+ Revision: 752006
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.2-1
+ Revision: 718476
- texlive-foilhtml
- texlive-foilhtml
- texlive-foilhtml
- texlive-foilhtml

