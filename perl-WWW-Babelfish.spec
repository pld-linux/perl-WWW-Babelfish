#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	WWW
%define	pnam	Babelfish
Summary:	WWW::Babelfish Perl module
Summary(cs):	Modul WWW::Babelfish pro Perl
Summary(da):	Perlmodul WWW::Babelfish
Summary(de):	WWW::Babelfish Perl Modul
Summary(es):	Módulo de Perl WWW::Babelfish
Summary(fr):	Module Perl WWW::Babelfish
Summary(it):	Modulo di Perl WWW::Babelfish
Summary(ja):	WWW::Babelfish Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	WWW::Babelfish ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul WWW::Babelfish
Summary(pl):	Modu³ Perla WWW::Babelfish
Summary(pt):	Módulo de Perl WWW::Babelfish
Summary(pt_BR):	Módulo Perl WWW::Babelfish
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl WWW::Babelfish
Summary(sv):	WWW::Babelfish Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl WWW::Babelfish
Summary(zh_CN):	WWW::Babelfish Perl Ä£¿é
Name:		perl-WWW-Babelfish
Version:	0.11
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	99515fcf6f64090abc852ac39a267e71
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-libwww
BuildRequires:	perl-IO-String
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Babelfish - perl module for translation via babelfish.

%description -l pl
WWW::Babelfish - modu³ do t³umaczenia z wykorzystaniem babelfish.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

# tests are network-dependent and interactive
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/WWW/Babelfish.pm
# empty autosplit.ix
#%dir %{perl_vendorlib}/auto/WWW/Babelfish
#%%{perl_vendorlib}/auto/WWW/Babelfish/autosplit.ix
%{_mandir}/man3/*
