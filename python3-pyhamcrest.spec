#
# Conditional build:
%bcond_without	doc	# Sphinx documentation

Summary:	Hamcrest framework for matcher objects
Summary(pl.UTF-8):	Szkielet Hamcrest do obiektów dopasowujących
Name:		python3-pyhamcrest
Version:	2.0.2
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pyhamcrest/
Source0:	https://files.pythonhosted.org/packages/source/p/pyhamcrest/PyHamcrest-%{version}.tar.gz
# Source0-md5:	7a086f0b067f8d38958ec32f054559b4
URL:		https://pypi.org/project/PyHamcrest/
BuildRequires:	python3-modules >= 1:3.5
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-sphinx_rtd_theme
BuildRequires:	sphinx-pdg-3
%endif
Requires:	python3-modules >= 1:3.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PyHamcrest is a framework for writing matcher objects, allowing you to
declaratively define "match" rules. There are a number of situations
where matchers are invaluable, such as UI validation, or data
filtering, but it is in the area of writing flexible tests that
matchers are most commonly used.

%description -l pl.UTF-8
PyHamcrest to szkielet do pisania obiektów dopasowujących,
pozwalających deklaratywnie definiować reguły dopasowań. Jest wiele
sytuacji, gdzie dopasowywanie jest bezcenne, np. sprawdzanie
poprawności w interfejsie użytkownika, filtrowanie danych, ale
najczęściej jest przydatne w obszarze pisania elastycznych testów.

%package apidocs
Summary:	API documentation for Python pyhamcrest module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona pyhamcrest
Group:		Documentation

%description apidocs
API documentation for Python pyhamcrest module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona pyhamcrest.

%prep
%setup -q -n PyHamcrest-%{version}

%build
%py3_build

%if %{with doc}
PYTHONPATH=$(pwd)/src \
%{__make} -C doc html \
	SPHINXBUILD=sphinx-build-3
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/python3-pyhamcrest-%{version}
cp -a examples/*.py $RPM_BUILD_ROOT%{_examplesdir}/python3-pyhamcrest-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.txt LICENSE.txt README.rst
%{py3_sitescriptdir}/hamcrest
%{py3_sitescriptdir}/PyHamcrest-%{version}-py*.egg-info
%{_examplesdir}/python3-pyhamcrest-%{version}

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/_build/html/{_static,*.html,*.js}
%endif
