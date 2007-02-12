#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	POE
%define		pnam	Sugar-Args
Summary:	POE::Sugar::Args - get "pretty", OO representation of args
Summary(pl.UTF-8):   POE::Sugar::Args - "ładna", obiektowo zorientowana reprezentacja argumentów
Name:		perl-POE-Sugar-Args
Version:	1.3
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	99b1a0c0abb3a25353603bb79be7d005
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Devel-Caller-Perl
BuildRequires:	perl-Exporter-Lite
BuildRequires:	perl-POE
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module give an OO representation to arguments POE passes to event
states. I will not lie to you. This adds heavy, bulky code underneath.
On the other hand, it makes arguments for POE events much more
palatable. Of course, this is a Sugar module, meaning, it will rot
your program in odd (you'll be hooked) and unexpected ways
(performace), but you took the candy so you can suffer the
consequences. Good luck.

%description -l pl.UTF-8
Ten moduł nadaje obiektowo zorientowaną reprezentację argumentom,
które POE przekazuje do stanów zdarzeń. Autor nie zamierza kłamać -
ten moduł dodaje ciężki, masywny kod. Z drugiej strony, czyni
argumenty zdarzeń POE bardziej smacznymi. Oczywiście jest to moduł
Sugar (cukier), co oznacza, że program zgnije w dziwny i nieoczekiwany
sposób (wydajność), ale używający tego modułu bierze cukierek i może
znosić konsekwencje. Powodzenia.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
touch Makefile.PL
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"POE::Sugar::Args",PL_FILES=>{})' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*
%{_mandir}/man3/*
