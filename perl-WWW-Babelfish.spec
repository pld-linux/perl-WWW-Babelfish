%define	pdir	WWW
%define	pnam	Babelfish
%include	/usr/lib/rpm/macros.perl
Summary:	WWW-Babelfish perl module
Summary(pl):	Modu³ perla WWW-Babelfish
Name:		perl-WWW-Babelfish
Version:	0.10
Release:	3

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-libwww
BuildRequires:	perl-IO-String
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW-Babelfish - perl module for translation via babelfish.

%description -l pl
WWW-Babelfish - modu³ do t³umaczenia z wykorzystaniem babelfish.

%prep
%setup -q -n WWW-Babelfish-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/WWW/Babelfish.pm
%{perl_sitelib}/auto/WWW/Babelfish
%{_mandir}/man3/*
