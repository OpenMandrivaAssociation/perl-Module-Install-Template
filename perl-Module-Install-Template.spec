%define upstream_name    Module-Install-Template
%define upstream_version 0.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Treat module source code as a template
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Template)
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(UNIVERSAL::require)
BuildArch:	noarch

%description
This module, if used in the Makefile.PL as shown in the synopsis, treats
module source code files as templates and processes them with the the
Template manpage Toolkit during 'make' time.

That is, 'lib/' is expected to contain templates, and 'blib/lib/' will
contain the resulting files as processed by the Template Toolkit.

This only happens on the author's side. The end-user will not notice any of
it.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*
%{_bindir}/tt_pm_to_blib

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 655056
- rebuild for updated spec-helper

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 474654
- update to 0.08

* Thu Sep 17 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 444068
- import perl-Module-Install-Template


* Thu Sep 17 2009 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist
