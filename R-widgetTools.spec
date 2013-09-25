%global packname  widgetTools
%global rlibdir  %{_libdir}/R/library

%define debug_package %{nil}

Name:             R-%{packname}
Version:          1.38.0
Release:          1
Summary:          Creates an interactive tcltk widget
Group:            Sciences/Mathematics
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/widgetTools_1.38.0.tar.gz
Requires:         R-methods R-utils R-tcltk 
Requires:         R-Biobase 
BuildRequires:    R-devel Rmath-devel texlive-collection-latex R-methods R-utils R-tcltk
BuildRequires:    R-Biobase 

%description
This packages contains tools to support the construction of tcltk widgets

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

#%check
#%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help


%changelog
* Thu Feb 16 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.32.0-1
+ Revision: 775491
- Import R-widgetTools
- Import R-widgetTools



