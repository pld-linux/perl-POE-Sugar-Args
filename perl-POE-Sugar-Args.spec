#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	POE
%define	pnam	Sugar-Args
Summary:	POE::Sugar::Args - Get "pretty", OO representation of args.
#Summary(pl):	
Name:		perl-POE-Sugar-Args
Version:	1.2
Release:	1
# same as perl
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{!?_without_tests:1}0
BuildRequires:	perl(Devel::Caller::Perl)
BuildRequires:	perl-Exporter-Lite
BuildRequires:	perl-POE
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module give an OO representation to arguments POE passes to event
states. I will not lie to you. This adds heavy, bulky code underneath.
On the other hand, it makes arguments for POE events much more
palatable. Of course, this is a Sugar module, meaning, it will rot your
program in odd (you'll be hooked) and unexpected ways (performace), but
you took the candy so you can suffer the consequences. Good luck.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
#%{__perl} Build.PL \
#	config="sitelib=%{perl_vendorlib} sitearch=%{perl_vendorarch}"
#./Build
touch Makefile.PL
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"POE::Sugar::Args",PL_FILES=>{})' \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

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
