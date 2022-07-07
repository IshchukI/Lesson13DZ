import sys
import doc_analyzer


if __name__ == "__main__":
    print("Run mypackage")
    print("Done")
    print(sys.argv)
    if len(sys.argv) > 1:
        pDFAnalyzer = doc_analyzer.PDFAnalyzer(sys.argv[1])

    if len(sys.argv) > 2:
        if (sys.argv[2] =="collect_links" ):
            links = pDFAnalyzer.link_analyzer.collect_links()
            print(f"<<<<<<<{links}>>>>>>>")
        if (sys.argv[2] == "review_link"):
            ans = pDFAnalyzer.link_analyzer.review_link()
            print(f"link is ok: {ans}")
        if (sys.argv[2] == "review_links"):
            ans = pDFAnalyzer.link_analyzer.review_links()
            print(ans)
        if (sys.argv[2] == "clean"):
            pDFAnalyzer.link_analyzer.clean()
            print("all clear")
        if (sys.argv[2] == "make_report"):
            pDFAnalyzer.link_analyzer.make_report()
