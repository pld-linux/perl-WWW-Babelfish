%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	WWW-Babelfish perl module
Summary(pl):	Modu� perla WWW-Babelfish
Name:		perl-WWW-Babelfish
Version:	0.02
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/WWW/WWW-Babelfish-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
WWW-Babelfish - perl module for translation via babelfish.

%description -l pl
WWW-Babelfish - modu� do t�umaczenia z wykorzystaniem babelfish.

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
