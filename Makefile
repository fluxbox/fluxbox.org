toc:
	@echo yo.

cr-news:
	python3 utils/news2hugo/news2hugo.py -o content/news < data/fluxbox-news.yaml

cr-manpages: content/help/man-fluxbox.md
cr-manpages: content/help/man-fluxbox-apps.md
cr-manpages: content/help/man-fluxbox-keys.md
cr-manpages: content/help/man-fluxbox-menu.md
cr-manpages: content/help/man-fluxbox-remote.md
cr-manpages: content/help/man-fluxbox-style.md
cr-manpages: content/help/man-client-patterns.md
cr-manpages: content/help/man-fbrun.md
cr-manpages: content/help/man-fbsetbg.md
cr-manpages: content/help/man-fbsetroot.md
cr-manpages: content/help/man-startfluxbox.md

content/help/man-%.md: $(FLUXBOX_SRC)/doc/asciidoc/%.txt
	asciidoctor -b docbook -o - $^ |\
	pandoc -f docbook -t markdown_strict - -o - |\
	python3 utils/number-manpages.py $(notdir $@) > $@
