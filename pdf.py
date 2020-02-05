from wand.image import Image as wi
import os


def parse_pdf(filepath, resolution=300):
    pdf = wi(filename=filepath, resolution=resolution)
    pdf = pdf.convert("jpeg")
    return pdf


def save_pdf_as_img(pdf, filename):
    page_count = 1
    for img in pdf.sequence:
        page = wi(image=img)
        page.save(filename=filename + str(page_count) + '.jpg')
        page_count += 1
    return page_count


def save_img_as_pdf(file_dir, filename, count, output_dir, output_filename):
    path = os.path.join(file_dir, filename)
    output_path = os.path.join(output_dir, output_filename)
    with wi() as w:
        for i in range(1, count):
            with wi(filename=path + str(i) + '.jpg') as page:
                w.sequence.append(page)
        w.save(filename=output_path)
    return output_path


if __name__ == '__main__':
    path = 'pdf/1580826601.pdf'
