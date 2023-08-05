from PyPDF2 import PdfReader, PdfWriter
import os

doc_path = 'merge-pdf/doc/'
filenames = os.listdir(doc_path)
filenames.sort()
pdf_writer = PdfWriter()
filenames = list(map(lambda filename: doc_path + filename, filenames))

for filename in filenames:
    pdf_reader = PdfReader(filename)
    for num_page in range(1, len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[num_page])

with open("new-pdf.pdf", "wb") as file:
    pdf_writer.write(file)

pdf_reader = PdfReader("new-pdf.pdf")
print(f"Le nouveau pdf compte {len(pdf_reader.pages)} pages")
