MAIN=0_diploma
SOURCE=$(MAIN).tex

all: clean
	xelatex --shell-escape $(SOURCE)
	bibtex $(MAIN)
	xelatex --shell-escape $(SOURCE)
	xelatex --shell-escape $(SOURCE)

clean:
	rm -rf auto _* *.aux *.log *.nav *.out *.snm *.toc *~ *.blg *.bbl

cleanall: clean
	rm -rf $(MAIN).pdf
