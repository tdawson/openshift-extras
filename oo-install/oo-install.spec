%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

%global import_path github.com/openshift/openshift-extras
# %commit is intended to be set by tito custom builders provided
# in the .tito/lib directory. The values in this spec file will not be kept up to date.
%{!?commit:
%global commit c64d09e528ca433832c6b6e6f5c7734a9cc8ee6f
}

Name:           oo-install
Version:        3.0.3
Release:        1%{?dist}
Summary:        Ansible wrapper for OpenShift Enterprise 3 installation
License:        ASL 2.0
URL:            http://github.com/openshift/openshift-extras/tree/enterprise-3.0/oo-install
Source0:        https://%{import_path}/archive/%{commit}/%{name}-%{version}.tar.gz
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
%setup -q
mv src/* .

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root %{buildroot}

# Uncomment once tests are working
#%check
#%{__python} ./tests/test_simple.py

%files
%{python_sitelib}/*
%{_bindir}/oo-install

%changelog
* Mon Oct 12 2015 Troy Dawson <tdawson@redhat.com> 3.0.3-1
- fixup sources (tdawson@redhat.com)
- fixup prep (tdawson@redhat.com)

* Mon Oct 12 2015 Troy Dawson <tdawson@redhat.com> 3.0.2-1
- update spec file to work with tito (tdawson@redhat.com)

* Mon Oct 12 2015 Troy Dawson <tdawson@redhat.com> 3.0.1-1
- Inial import to tito

* Tue Oct 06 2015 Troy Dawson <tdawson@redhat.com> - 3.0.0-0.4
- Those weren't really example configs, put them back

* Tue Oct 06 2015 Troy Dawson <tdawson@redhat.com> - 3.0.0-0.3
- Put example configs in doc

* Tue Oct 06 2015 Troy Dawson <tdawson@redhat.com> - 3.0.0-0.2
- Fix dependencies

* Tue Oct 06 2015 Troy Dawson <tdawson@redhat.com> - 3.0.0-0.1
- Initial Package
