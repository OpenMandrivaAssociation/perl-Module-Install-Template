%define upstream_name    Module-Install-Template
%define upstream_version 0.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Treat module source code as a template
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Template)
BuildRequires: perl(Test::Compile)
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/tt_pm_to_blib

