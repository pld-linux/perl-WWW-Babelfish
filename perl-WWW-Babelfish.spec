#
# Conditional build:
%bcond_with	tests	# perform "make test"
			# tests are network-dependent and interactive
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	WWW
%define		pnam	Babelfish
Summary:	WWW::Babelfish Perl module
Summary(cs.UTF-8):   Modul WWW::Babelfish pro Perl
Summary(da.UTF-8):   Perlmodul WWW::Babelfish
Summary(de.UTF-8):   WWW::Babelfish Perl Modul
Summary(es.UTF-8):   Módulo de Perl WWW::Babelfish
Summary(fr.UTF-8):   Module Perl WWW::Babelfish
Summary(it.UTF-8):   Modulo di Perl WWW::Babelfish
Summary(ja.UTF-8):   WWW::Babelfish Perl モジュール
Summary(ko.UTF-8):   WWW::Babelfish 펄 모줄
Summary(nb.UTF-8):   Perlmodul WWW::Babelfish
Summary(pl.UTF-8):   Moduł Perla WWW::Babelfish
Summary(pt.UTF-8):   Módulo de Perl WWW::Babelfish
Summary(pt_BR.UTF-8):   Módulo Perl WWW::Babelfish
Summary(ru.UTF-8):   Модуль для Perl WWW::Babelfish
Summary(sv.UTF-8):   WWW::Babelfish Perlmodul
Summary(uk.UTF-8):   Модуль для Perl WWW::Babelfish
Summary(zh_CN.UTF-8):   WWW::Babelfish Perl 模块
Name:		perl-WWW-Babelfish
Version:	0.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bc6293dabcbf5e96435fc8acaf8ac939
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-libwww
BuildRequires:	perl-IO-String
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
WWW::Babelfish - perl module for translation via babelfish.

%description -l pl.UTF-8
WWW::Babelfish - moduł do tłumaczenia z wykorzystaniem babelfish.

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
