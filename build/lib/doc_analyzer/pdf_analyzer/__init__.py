from pdf_analyzer_module import PDFAnalyzer
from pdf_analyzer_module import LinkAnalyzer



class PDFAnalyzer(PDFAnalyzer):
    path = PDFAnalyzer.DEFAULT_PATH

    def __init__(self):
        super('path').__init__()