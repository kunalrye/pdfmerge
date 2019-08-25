import PyPDF2
from PyPDF2 import PdfFileMerger
from os import listdir
from os.path import isfile, join

def merge_pdf(folder_path, output_file):
    """
    folder_path: path for folder of pdfs that will be merged
    output_file: name of output pdf to be saved as
    """
    pdf_files = [f for f in listdir(folder_path) if isfile(join(folder_path, f))]
    merger = PdfFileMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()


# merge_pdf("/Users/kunal/Downloads/pdf_test", "test.pdf")