#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# tests are network-dependent and interactive
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	WWW
%define		pnam	Babelfish
Summary:	WWW::Babelfish - Perl extension for translation via Babelfish or Google
Summary(pl.UTF-8):	WWW::Babelfish - rozszerzenie Perla do tłumaczenia z użyciem Babelfish lub Google
Name:		perl-WWW-Babelfish
Version:	0.16
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/WWW/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	21f881470fd159c6732b4da866648452
URL:		http://search.cpan.org/dist/WWW-Babelfish/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-IO-String
BuildRequires:	perl-libwww
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Babelfish - Perl module for translation via Babelfish or Google.

%description -l pl.UTF-8
WWW::Babelfish - moduł Perla do tłumaczenia z wykorzystaniem serwisu
Babelfish lub Google.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL %{!?with_tests: </dev/null } \
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
%{perl_vendorlib}/WWW/Babelfish.pm
# empty autosplit.ix
#%dir %{perl_vendorlib}/auto/WWW/Babelfish
#%%{perl_vendorlib}/auto/WWW/Babelfish/autosplit.ix
%{_mandir}/man3/*
