%include	/usr/lib/rpm/macros.perl
Summary:	WWW-Babelfish perl module
Summary(pl):	Modu³ perla WWW-Babelfish
Name:		perl-WWW-Babelfish
Version:	0.07
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/WWW-Babelfish-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-libwww
BuildRequires:	perl-IO-String
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW-Babelfish - perl module for translation via babelfish.

%description -l pl
WWW-Babelfish - modu³ do t³umaczenia z wykorzystaniem babelfish.

%prep
%setup -q -n WWW-Babelfish-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/WWW/Babelfish
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/WWW/Babelfish.pm
%{perl_sitelib}/auto/WWW/Babelfish
%{perl_sitearch}/auto/WWW/Babelfish

%{_mandir}/man3/*
