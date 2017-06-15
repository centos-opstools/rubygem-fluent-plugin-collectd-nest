# Generated from fluent-plugin-collectd-nest-0.1.2.gem by gem2rpm -*- rpm-spec -*-
%global gem_name fluent-plugin-collectd-nest

Name: rubygem-%{gem_name}
Version: 0.1.4
Release: 1%{?dist}
Summary: Output filter plugin to rewrite Collectd JSON output to nested json
Group: Development/Languages
License: MIT
URL: https://github.com/viaq/fluent-plugin-collectd-nest
Source0: https://rubygems.org/gems/%{gem_name}-%{version}.gem
BuildRequires: ruby(release)
BuildRequires: rubygems-devel
BuildRequires: ruby
Requires: rubygem(fluentd) >= 0.10.17
# the following BuildRequires are development dependencies
BuildArch: noarch
Provides: rubygem(%{gem_name}) = %{version}

%description
Output filter plugin to rewrite Collectd JSON output to nested json.


%package doc
Summary: Documentation for %{name}
Group: Documentation
Requires: %{name} = %{version}-%{release}

%description doc
Documentation for %{name}.

%prep
gem unpack %{SOURCE0}

%setup -q -D -T -n  %{gem_name}-%{version}

gem spec %{SOURCE0} -l --ruby > %{gem_name}.gemspec

%build
# Create the gem as gem install only works on a gem file
gem build %{gem_name}.gemspec

# %%gem_install compiles any C extensions and installs the gem into ./%%gem_dir
# by default, so that we can move it into the buildroot in %%install
%gem_install

%install
mkdir -p %{buildroot}%{gem_dir}
cp -a .%{gem_dir}/* \
        %{buildroot}%{gem_dir}/

%files
%dir %{gem_instdir}
%{gem_instdir}/VERSION
%{gem_libdir}
%{gem_instdir}/sample-zeus-config
%exclude %{gem_cache}
%{gem_spec}

%files doc
%doc %{gem_docdir}
%doc %{gem_instdir}/ChangeLog
%{gem_instdir}/Gemfile
%doc %{gem_instdir}/README.md
%{gem_instdir}/Rakefile
%{gem_instdir}/fluent-plugin-collectd-nest.gemspec
%{gem_instdir}/test

%changelog
* Thu Jun 15 2017 Rich Megginson <rmeggins@redhat.com> - 0.1.4-1
- updated field as a string and not an array

* Mon Apr  3 2017 Rich Megginson <rmeggins@redhat.com> - 0.1.3-1
- Remove dsname from nested value field

* Wed Feb 15 2017 Rich Megginson <rmeggins@redhat.com> - 0.1.2-1
- Initial package
