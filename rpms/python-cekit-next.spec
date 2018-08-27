%if 0%{?rhel}
%global with_python3 0
%else
%global with_python3 1
%endif

%global modname cekit-next

Name:           python-cekit-next
Version:        2.2.0
Conflicts:      python-cekit
Release:        1
Summary:        Container image creation tool - upcoming version
License:        MIT
URL:            https://github.com/cekit/cekit
Source0:        %{url}/archive/develop.tar.gz
BuildArch:      noarch

%global _description \
Cekit helps to build container images from image definition files

%description %_description

%package -n python2-%{modname}
Summary:        %{summary}
Conflicts:      python2-cekit
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-mock
BuildRequires:  python2-pykwalify
BuildRequires:  PyYAML
BuildRequires:  python2-colorlog
BuildRequires:  python-jinja2

%if 0%{?rhel}
BuildRequires:  pytest
Requires:       python-jinja2
Requires:       python-setuptools
Requires:       python-docker-py
%else
BuildRequires:  python2-pytest
Requires:       python2-jinja2
Requires:       python2-setuptools
Requires:       python2-docker
%endif

Requires:       python2-pykwalify
Requires:       python2-colorlog
Requires:       PyYAML
Requires:       docker
Requires:       git
Requires:       bash-completion

%description -n python2-%{modname} %_description

Python 2 version.

%if 0%{?with_python3}
%package -n python3-%{modname}
Summary:        %{summary}
Conflicts:      python3-cekit
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  python3-pytest
BuildRequires:  python3-mock
BuildRequires:  PyYAML
BuildRequires:  python3-pykwalify
BuildRequires:  python3-colorlog
BuildRequires:  python3-jinja2
Requires:       PyYAML
Requires:       docker
Requires:       python3-pykwalify
Requires:       python3-colorlog
Requires:       python3-jinja2
Requires:       python3-setuptools
Requires:       python3-docker
Requires:       git

%description -n python3-%{modname} %_description

Python 3 version.
%endif

%package -n %{modname}-bash-completion
Summary:        %{summary}
Requires:       bash-completion
%description -n %{modname}-bash-completion %_description

Bash completion.

%package -n %{modname}-zsh-completion
Summary:        %{summary}
Requires:       zsh
%description -n %{modname}-zsh-completion %_description

ZSH completion.

%prep
%setup -q -n cekit-develop

%build
%py2_build
%if 0%{?with_python3}
%py3_build
%endif

#%check
#py.test-%{python2_version} -v tests/test_unit*.py
#%if 0%{?with_python3}
#py.test-%{python3_version} -v tests/test_unit*.py
#%endif

%install
mkdir -p %{buildroot}/%{_sysconfdir}/bash_completion.d
cp completion/bash/cekit %{buildroot}/%{_sysconfdir}/bash_completion.d/cekit

mkdir -p %{buildroot}/%{_datadir}/zsh/site-functions
cp completion/zsh/_cekit %{buildroot}/%{_datadir}/zsh/site-functions/_cekit

%py2_install
%if 0%{?with_python3}
%py3_install
%endif

%files -n python2-%{modname}
%doc README.rst
%license LICENSE
%{python2_sitelib}/cekit/
%{python2_sitelib}/cekit-*.egg-info/

%files -n %{modname}-bash-completion
%doc README.rst
%license LICENSE
%{_sysconfdir}/bash_completion.d/cekit

%files -n %{modname}-zsh-completion
%doc README.rst
%license LICENSE
%{_datadir}/zsh/site-functions/_cekit

%if 0%{?with_python3}
%files -n python3-%{modname}
%doc README.rst
%license LICENSE
%{python3_sitelib}/cekit/
%{python3_sitelib}/cekit-*.egg-info/
%endif

# This file ends up in py3 subpackage if enabled, otherwise in py2
%{_bindir}/concreate
%{_bindir}/cekit
%{_bindir}/cekit-cache


%changelog
* Wed Jun 13 2018 David Becvarik <dbecvari@redhat.com> - 2.1.0-1
- 2.1 cekit-next release
