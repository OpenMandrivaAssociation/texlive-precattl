%global tl_name precattl
%global tl_revision 76924

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0.0
Release:	%{tl_revision}.1
Summary:	Prepare special catcodes from token list
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/precattl
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/precattl.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/precattl.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Allow users to write code that contains tokens with unusual catcodes.

