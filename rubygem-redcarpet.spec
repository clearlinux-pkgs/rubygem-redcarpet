#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-redcarpet
Version  : 3.2.3
Release  : 5
URL      : https://rubygems.org/downloads/redcarpet-3.2.3.gem
Source0  : https://rubygems.org/downloads/redcarpet-3.2.3.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: rubygem-redcarpet-bin
Requires: rubygem-redcarpet-lib
BuildRequires : ruby
BuildRequires : rubygem-mini_portile
BuildRequires : rubygem-nokogiri
BuildRequires : rubygem-rake-compiler
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rubygems-tasks
BuildRequires : rubygem-test-unit

%description
Redcarpet is written with sugar, spice and everything nice
============================================================

%package bin
Summary: bin components for the rubygem-redcarpet package.
Group: Binaries

%description bin
bin components for the rubygem-redcarpet package.


%package lib
Summary: lib components for the rubygem-redcarpet package.
Group: Libraries

%description lib
lib components for the rubygem-redcarpet package.


%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n redcarpet-3.2.3
gem spec %{SOURCE0} -l --ruby > rubygem-redcarpet.gemspec

%build
gem build rubygem-redcarpet.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
redcarpet-3.2.3.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/redcarpet-3.2.3
ruby -I"lib:test" test*/test_*.rb
ruby -I"lib:test" test*/*_test.rb
popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/cache/redcarpet-3.2.3.gem
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Object/cdesc-Object.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Markdown/cdesc-Markdown.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Markdown/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Markdown/render-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Markdown/renderer-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/Base/cdesc-Base.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/Base/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/HTML/cdesc-HTML.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/HTML/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/HTML_TOC/cdesc-HTML_TOC.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/HTML_TOC/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/ManPage/block_code-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/ManPage/cdesc-ManPage.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/ManPage/codespan-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/ManPage/double_emphasis-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/ManPage/emphasis-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/ManPage/header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/ManPage/linebreak-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/ManPage/list-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/ManPage/list_item-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/ManPage/normal_text-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/ManPage/paragraph-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/Safe/block_code-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/Safe/cdesc-Safe.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/Safe/html_escape-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/Safe/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/SmartyHTML/cdesc-SmartyHTML.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/SmartyPants/cdesc-SmartyPants.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/SmartyPants/postprocess-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/SmartyPants/render-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/StripDown/cdesc-StripDown.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/StripDown/header-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/StripDown/image-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/StripDown/link-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/StripDown/paragraph-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/XHTML/cdesc-XHTML.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/XHTML/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/Render/cdesc-Render.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/Redcarpet/cdesc-Redcarpet.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/RedcarpetCompat/cdesc-RedcarpetCompat.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/RedcarpetCompat/list_to_truthy_hash-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/RedcarpetCompat/new-c.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/RedcarpetCompat/parse_extensions_and_renderer_options-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/RedcarpetCompat/rename_extensions-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/RedcarpetCompat/text-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/RedcarpetCompat/to_html-i.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/cache.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/ext/redcarpet/page-Makefile.ri
/usr/lib64/ruby/gems/2.2.0/doc/redcarpet-3.2.3/ri/page-COPYING.ri
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/redcarpet-3.2.3/gem.build_complete
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/redcarpet-3.2.3/gem_make.out
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/COPYING
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/Gemfile
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/README.markdown
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/Rakefile
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/bin/redcarpet
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/.RUBYARCHDIR.time
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/Makefile
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/autolink.c
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/autolink.h
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/autolink.o
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/buffer.c
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/buffer.h
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/buffer.o
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/extconf.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/houdini.h
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/houdini_href_e.c
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/houdini_href_e.o
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/houdini_html_e.c
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/houdini_html_e.o
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/html.c
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/html.h
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/html.o
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/html_blocks.h
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/html_smartypants.c
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/html_smartypants.o
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/markdown.c
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/markdown.h
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/markdown.o
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/rc_markdown.c
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/rc_markdown.o
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/rc_render.c
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/rc_render.o
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/redcarpet.h
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/stack.c
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/stack.h
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/stack.o
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/lib/redcarpet.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/lib/redcarpet/compat.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/lib/redcarpet/render_man.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/lib/redcarpet/render_strip.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/redcarpet.gemspec
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/test/benchmark.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/test/custom_render_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/test/html5_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/test/html_render_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/test/html_toc_render_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/test/markdown_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/test/pathological_inputs_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/test/redcarpet_compat_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/test/safe_render_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/test/smarty_html_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/test/smarty_pants_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/test/stripdown_render_test.rb
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/test/test_helper.rb
/usr/lib64/ruby/gems/2.2.0/specifications/redcarpet-3.2.3.gemspec

%files bin
%defattr(-,root,root,-)
/usr/bin/redcarpet

%files lib
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.2.0/extensions/x86_64-linux/2.2.0/redcarpet-3.2.3/redcarpet.so
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/ext/redcarpet/redcarpet.so
/usr/lib64/ruby/gems/2.2.0/gems/redcarpet-3.2.3/lib/redcarpet.so
