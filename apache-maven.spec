#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : apache-maven
Version  : 3.6.0
Release  : 19
URL      : http://mirrors.ibiblio.org/apache/maven/maven-3/3.6.0/source/apache-maven-3.6.0-src.tar.gz
Source0  : http://mirrors.ibiblio.org/apache/maven/maven-3/3.6.0/source/apache-maven-3.6.0-src.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 MIT
Requires: apache-maven-bin = %{version}-%{release}
Requires: apache-maven-data = %{version}-%{release}
Requires: apache-maven-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : maven-dep
BuildRequires : openjdk
Patch1: maven-script.patch

%description
<!---
Licensed to the Apache Software Foundation (ASF) under one or more
contributor license agreements.  See the NOTICE file distributed with
this work for additional information regarding copyright ownership.
The ASF licenses this file to You under the Apache License, Version 2.0
(the "License"); you may not use this file except in compliance with
the License.  You may obtain a copy of the License at

%package bin
Summary: bin components for the apache-maven package.
Group: Binaries
Requires: apache-maven-data = %{version}-%{release}
Requires: apache-maven-license = %{version}-%{release}

%description bin
bin components for the apache-maven package.


%package data
Summary: data components for the apache-maven package.
Group: Data

%description data
data components for the apache-maven package.


%package license
Summary: license components for the apache-maven package.
Group: Default

%description license
license components for the apache-maven package.


%prep
%setup -q -n apache-maven-3.6.0
%patch1 -p1

%build
## build_prepend content
mkdir %{buildroot}
cp -r /usr/share/apache-maven/.m2 %{buildroot}/.m2
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551206814
export LDFLAGS="${LDFLAGS} -fno-lto"
make  %{?_smp_mflags} || mvn install -Dmaven.repo.local=%{buildroot}/.m2/repository -Drat.skip=true -Dplatform=linux64


%install
export SOURCE_DATE_EPOCH=1551206814
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/apache-maven
cp LICENSE %{buildroot}/usr/share/package-licenses/apache-maven/LICENSE
cp apache-maven/src/main/appended-resources/META-INF/LICENSE.vm %{buildroot}/usr/share/package-licenses/apache-maven/apache-maven_src_main_appended-resources_META-INF_LICENSE.vm
%make_install || :
## install_append content
mkdir -p %{buildroot}/usr/share/apache-maven
tar -xf apache-maven/target/apache-maven-3.6.0-bin.tar.gz -C %{buildroot}/usr/share/apache-maven --strip-components=1
mkdir -p %{buildroot}/usr/bin
for cmd in mvnDebug mvnyjp; do
sed s/@@CMD@@/$cmd/ maven-script >%{buildroot}/usr/bin/$cmd
chmod +x %{buildroot}/usr/bin/$cmd
done
sed s/@@CMD@@/mvn/ maven-script >%{buildroot}/usr/share/apache-maven/bin/mvn-script
ln -sf ../share/apache-maven/bin/mvn-script %{buildroot}/usr/bin/mvn
chmod +x %{buildroot}/usr/share/apache-maven/bin/mvn-script
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mvn
/usr/bin/mvnDebug
/usr/bin/mvnyjp

%files data
%defattr(-,root,root,-)
%exclude /usr/share/apache-maven/lib/jansi-native/freebsd32/libjansi.so
%exclude /usr/share/apache-maven/lib/jansi-native/freebsd64/libjansi.so
%exclude /usr/share/apache-maven/lib/jansi-native/linux32/libjansi.so
%exclude /usr/share/apache-maven/lib/jansi-native/osx/libjansi.jnilib
%exclude /usr/share/apache-maven/lib/jansi-native/windows32/jansi.dll
%exclude /usr/share/apache-maven/lib/jansi-native/windows64/jansi.dll
/usr/share/apache-maven/LICENSE
/usr/share/apache-maven/NOTICE
/usr/share/apache-maven/README.txt
/usr/share/apache-maven/bin/m2.conf
/usr/share/apache-maven/bin/mvn
/usr/share/apache-maven/bin/mvn-script
/usr/share/apache-maven/bin/mvn.cmd
/usr/share/apache-maven/bin/mvnDebug
/usr/share/apache-maven/bin/mvnDebug.cmd
/usr/share/apache-maven/bin/mvnyjp
/usr/share/apache-maven/boot/plexus-classworlds-2.5.2.jar
/usr/share/apache-maven/conf/logging/simplelogger.properties
/usr/share/apache-maven/conf/settings.xml
/usr/share/apache-maven/conf/toolchains.xml
/usr/share/apache-maven/lib/animal-sniffer-annotations-1.14.jar
/usr/share/apache-maven/lib/animal-sniffer-annotations.license
/usr/share/apache-maven/lib/aopalliance-1.0.jar
/usr/share/apache-maven/lib/cdi-api-1.0.jar
/usr/share/apache-maven/lib/checker-compat-qual-2.0.0.jar
/usr/share/apache-maven/lib/checker-compat-qual.license
/usr/share/apache-maven/lib/commons-cli-1.4.jar
/usr/share/apache-maven/lib/commons-io-2.5.jar
/usr/share/apache-maven/lib/commons-lang3-3.8.1.jar
/usr/share/apache-maven/lib/error_prone_annotations-2.1.3.jar
/usr/share/apache-maven/lib/ext/README.txt
/usr/share/apache-maven/lib/guava-25.1-android.jar
/usr/share/apache-maven/lib/guice-4.2.1-no_aop.jar
/usr/share/apache-maven/lib/j2objc-annotations-1.1.jar
/usr/share/apache-maven/lib/jansi-1.17.1.jar
/usr/share/apache-maven/lib/jansi-native/README.txt
/usr/share/apache-maven/lib/jansi-native/linux64/libjansi.so
/usr/share/apache-maven/lib/javax.inject-1.jar
/usr/share/apache-maven/lib/jcl-over-slf4j-1.7.25.jar
/usr/share/apache-maven/lib/jcl-over-slf4j.license
/usr/share/apache-maven/lib/jsr250-api-1.0.jar
/usr/share/apache-maven/lib/jsr250-api.license
/usr/share/apache-maven/lib/jsr305-3.0.2.jar
/usr/share/apache-maven/lib/maven-artifact-3.6.0.jar
/usr/share/apache-maven/lib/maven-builder-support-3.6.0.jar
/usr/share/apache-maven/lib/maven-compat-3.6.0.jar
/usr/share/apache-maven/lib/maven-core-3.6.0.jar
/usr/share/apache-maven/lib/maven-embedder-3.6.0.jar
/usr/share/apache-maven/lib/maven-model-3.6.0.jar
/usr/share/apache-maven/lib/maven-model-builder-3.6.0.jar
/usr/share/apache-maven/lib/maven-plugin-api-3.6.0.jar
/usr/share/apache-maven/lib/maven-repository-metadata-3.6.0.jar
/usr/share/apache-maven/lib/maven-resolver-api-1.3.1.jar
/usr/share/apache-maven/lib/maven-resolver-connector-basic-1.3.1.jar
/usr/share/apache-maven/lib/maven-resolver-impl-1.3.1.jar
/usr/share/apache-maven/lib/maven-resolver-provider-3.6.0.jar
/usr/share/apache-maven/lib/maven-resolver-spi-1.3.1.jar
/usr/share/apache-maven/lib/maven-resolver-transport-wagon-1.3.1.jar
/usr/share/apache-maven/lib/maven-resolver-util-1.3.1.jar
/usr/share/apache-maven/lib/maven-settings-3.6.0.jar
/usr/share/apache-maven/lib/maven-settings-builder-3.6.0.jar
/usr/share/apache-maven/lib/maven-shared-utils-3.2.1.jar
/usr/share/apache-maven/lib/maven-slf4j-provider-3.6.0.jar
/usr/share/apache-maven/lib/org.eclipse.sisu.inject-0.3.3.jar
/usr/share/apache-maven/lib/org.eclipse.sisu.inject.license
/usr/share/apache-maven/lib/org.eclipse.sisu.plexus-0.3.3.jar
/usr/share/apache-maven/lib/org.eclipse.sisu.plexus.license
/usr/share/apache-maven/lib/plexus-cipher-1.7.jar
/usr/share/apache-maven/lib/plexus-component-annotations-1.7.1.jar
/usr/share/apache-maven/lib/plexus-interpolation-1.25.jar
/usr/share/apache-maven/lib/plexus-sec-dispatcher-1.4.jar
/usr/share/apache-maven/lib/plexus-utils-3.1.0.jar
/usr/share/apache-maven/lib/slf4j-api-1.7.25.jar
/usr/share/apache-maven/lib/slf4j-api.license
/usr/share/apache-maven/lib/wagon-file-3.2.0.jar
/usr/share/apache-maven/lib/wagon-http-3.2.0-shaded.jar
/usr/share/apache-maven/lib/wagon-provider-api-3.2.0.jar

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/apache-maven/LICENSE
/usr/share/package-licenses/apache-maven/apache-maven_src_main_appended-resources_META-INF_LICENSE.vm
