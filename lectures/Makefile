TEXFILES := $(shell ls L*.tex 2>/dev/null)
PDFLATEX := pdflatex

all: $(TEXFILES:.tex=.pdf)

%.pdf: %.tex *.cls
	$(PDFLATEX) $<
	$(PDFLATEX) $<  # a second time for the table of contents...


book.pdf: L*.pdf
	@tp="/tmp/tmp.pdf"; \
	td="/tmp/data"; \
	for i in L*.pdf; do \
	    echo "Bookmarking $$i"; \
	    printf "BookmarkBegin\nBookmarkTitle: %s\nBookmarkLevel: 1\nBookmarkPageNumber: 1\n" "$${i%.*}"> "$$td"; \
	    pdftk "$$i" update_info "$$td" output "$$tp"; \
	    mv "$$tp" "$$i"; \
	done; \
	pdftk *.pdf cat output book.pdf

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.synctex.gz *.toc *.vrb *.blg *.bbl
	rm -rf models_cpmpy/__pycache__

# check for unused images; remove IPython checkpoints across the repo
distclean:
	find .. -type d -name .ipynb_checkpoints -prune -exec rm -rf {} +
	@for img in images/*; do \
		imgname=$$(basename $$img); \
		base=$${imgname%.*}; \
		found=0; \
		for tex in $(TEXFILES); do \
			grep -q "images/$$base" $$tex && found=1; \
		done; \
		if [ $$found -eq 0 ]; then \
			echo "rm $$img"; \
		fi; \
	done

# check that each CPMpy model runs on this computer
cpmpy:
	cd models_cpmpy && python test_all_scripts.py
