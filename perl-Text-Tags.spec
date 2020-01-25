#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Text
%define	pnam	Tags
Summary:	Text::Tags - parses "folksonomy" space-separated tags
Summary(pl.UTF-8):	Text::Tags - analiza "folksonomicznych" znaczników oddzielonych spacjami
Name:		perl-Text-Tags
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Text/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b7ea1c0bc4729df0d9abcffead238faf
URL:		http://search.cpan.org/dist/Text-Tags/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Parses "folksonomies", which are simple
space-separated-but-optionally-quoted tag lists. See
Text::Tags::Parser for the actual module; Text::Tags may be
used in a future version of the distribution.

%description -l pl.UTF-8
Moduł ten analizuje "folksonomie", czyli proste listy znaczników
oddzielonych spacjami i opcjonalnie ujętych w cudzysłowy. Właściwy
moduł to Text::Tags::Parser. Text::Tags być może będzie użyty w
kolejnych wersjach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
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
%doc Changes README
%{perl_vendorlib}/Text/*.pm
%{perl_vendorlib}/Text/Tags
%{_mandir}/man3/*
