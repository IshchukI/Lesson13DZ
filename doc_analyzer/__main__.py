import sys
import doc_analyzer


if __name__ == "__main__":
    print("Run mypackage")
    print("Done")
    print(sys.argv)
    pDFAnalyzer = doc_analyzer.PDFAnalyzer(sys.argv[1])
    if (sys.argv[2] =="collect_links" ):
        links = pDFAnalyzer.link_analyzer.collect_links()
        print(f"<<<<<<<{links}>>>>>>>")
    if (sys.argv[2] == "review_link"):
        pDFAnalyzer.link_analyzer.review_link()
    if (sys.argv[2] == "review_links"):
        pDFAnalyzer.link_analyzer.review_links()
    if (sys.argv[2] == "clean"):
        pDFAnalyzer.link_analyzer.clean()
    if (sys.argv[2] == "make_report"):
        pDFAnalyzer.link_analyzer.make_report()
