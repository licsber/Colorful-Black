import pdf
import color
import os


class Pdf:
    def __init__(self, file_dir, filename, output_path):
        self.file_dir = file_dir
        self.filename = filename
        self.pdf = pdf.parse_pdf(filepath=os.path.join(file_dir, filename))
        self.page_count = 0
        self.output_path = output_path

    def extract(self, tmp_dir='tmp/'):
        return pdf.save_pdf_as_img(pdf=self.pdf, filename=tmp_dir + self.filename)

    def convert(self):
        if self.page_count == 0:
            return
        color.mix_img(file_dir='tmp/', filename=self.filename, count=self.page_count)
        return

    def save(self):
        return pdf.save_img_as_pdf(file_dir='tmp/', filename=self.filename,
                                   count=self.page_count, output_dir=self.output_path, output_filename=self.filename)

    def get_output_filename(self):
        self.page_count = self.extract()
        self.convert()
        self.save()
        return self.filename


if __name__ == '__main__':
    test = Pdf('/Users/licsber/PycharmProjects/五彩斑斓的黑/pdf', '1580826601.pdf', 'output')
    print(test.get_output_filename())
