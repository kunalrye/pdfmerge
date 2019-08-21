import PyPDF2
from PyPDF2 import PdfFileMerger

def merge_pdf(pdfs, output_file):
    """
    filenames: list of file names to be merged
    output_file: name of output file to be saved as
    """
    merger = PdfFileMerger()
    for pdf in pdfs:
        merger.append(pdf)
    merger.write(output_file)
    merger.close()

# mit_notes = ['MITRES_6_007S11_lec01.pdf', 'MITRES_6_007S11_lec02.pdf', 'MITRES_6_007S11_lec03.pdf', 'MITRES_6_007S11_lec04.pdf','MITRES_6_007S11_lec05.pdf', 'MITRES_6_007S11_lec06.pdf', 'MITRES_6_007S11_lec07.pdf', 'MITRES_6_007S11_lec08.pdf', 'MITRES_6_007S11_lec09.pdf', 'MITRES_6_007S11_lec10.pdf', 'MITRES_6_007S11_lec11.pdf', 'MITRES_6_007S11_lec12.pdf', 'MITRES_6_007S11_lec13.pdf', 'MITRES_6_007S11_lec14.pdf', 'MITRES_6_007S11_lec15.pdf', 'MITRES_6_007S11_lec16.pdf', 'MITRES_6_007S11_lec17.pdf', 'MITRES_6_007S11_lec18.pdf', 'MITRES_6_007S11_lec19.pdf', 'MITRES_6_007S11_lec20.pdf', 'MITRES_6_007S11_lec21.pdf', 'MITRES_6_007S11_lec22.pdf', 'MITRES_6_007S11_lec23.pdf', 'MITRES_6_007S11_lec24.pdf', 'MITRES_6_007S11_lec25.pdf', 'MITRES_6_007S11_lec26.pdf']
# merge_pdf(mit_notes, 'mit_OCW.pdf')