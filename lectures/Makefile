TEXFILES := $(shell ls L*.tex 2>/dev/null)
PDFLATEX := pdflatex

all: $(TEXFILES:.tex=.pdf)

%.pdf: %.tex
	$(PDFLATEX) $<
	$(PDFLATEX) $<  # a second time for the table of contents...

clean:
	rm -f *.aux *.log *.nav *.out *.snm *.synctex.gz *.toc *.vrb

# check for unused images
distclean:
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
