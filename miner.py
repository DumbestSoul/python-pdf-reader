import math
import fitz # for doing operations on PDF
from tkinter import PhotoImage


class PDFMiner:
    def __init__(self, filepath):
        self.filepath = filepath
        self.pdf = fitz.open(self.filepath)
        self.first_page = self.pdf.load_page(0)
        self.width, self.height = self.first_page.rect.width, self.first_page.rect.height
        zoomdict = {800:0.8, 700:0.6, 600:1.0, 500:1.0}
        width = int(math.floor(self.width/100.0) * 100)
        self.zoom=zoomdict[width]

    def get_metadata(self):
        metadata = self.pdf.metadata
        numPages = self.pdf.page_count

        return metadata, numPages
    
    def get_page(self, page_num):
        page=self.pdf.load_page(page_num)

        if self.zoom:
            mat = fitz.Matrix(self.zoom, self.zoom)
            pix= page.get_pixmap(matrix=mat)

        else:
            pix=page.get_pixmap()

        pix1=fitz.Pixmap(pix, 0) if pix.alpha else pix
        imgdata = pix1.tobytes("ppm")

        return PhotoImage(data=imgdata)
    
    def get_text(self, page_num):
        page=self.pdf.load_page(page_num)
        text=page.getText('text')

        return text

