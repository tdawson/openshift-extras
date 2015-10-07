%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global srcname openshift-extras
%global commit                  c64d09e528ca433832c6b6e6f5c7734a9cc8ee6f
%global shortcommit             %(c=%{commit}; echo ${c:0:7})

Name:           oo-install
Version:        3.0.0
Release:        0.3%{?dist}
Summary:        Ansible wrapper for OpenShift Enterprise 3 installation
License:        ASL 2.0
URL:            http://github.com/openshift/openshift-extras/tree/enterprise-3.0/oo-install
Source0:        https://github.com/openshift/openshift-extras/archive/%{commit}/openshift-extras-%{commit}.tar.gz

BuildArch:      noarch

BuildRequires: python-setuptools
Requires:      ansible
Requires:      python-click
Requires:      python-ecdsa
Requires:      python-jinja2
Requires:      python-markupsafe
Requires:      python-paramiko
Requires:      python-crypto
Requires:      python-setuptools
Requires:      PyYAML

%description
Ansible wrapper for OpenShift Enterprise 3 installation.

%prep
%setup -q -n %{srcname}-%{commit}
mv oo-install/src/* .
mv ooinstall/{ansible.cfg,installer.cfg.template.yml} .
rm -rf oo-install/


%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

# Uncomment once tests are working
#%check
#%{__python} ./tests/test_simple.py

%files
%doc ansible.cfg installer.cfg.template.yml LICENSE README.md
%{python_sitelib}/*
%{_bindir}/oo-install

%changelog
* Tue Oct 06 2015 Troy Dawson <tdawson@redhat.com> - 3.0.0-0.3
- Put example configs in doc

* Tue Oct 06 2015 Troy Dawson <tdawson@redhat.com> - 3.0.0-0.2
- Fix dependencies

* Tue Oct 06 2015 Troy Dawson <tdawson@redhat.com> - 3.0.0-0.1
- Initial Package
