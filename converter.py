import sys
import pdf_converter
import content_processor


def write_text(text, outfile=None):
    if outfile is None:
        out = sys.stdout
    else:
        out = open(outfile, 'w')
    try:
        out.write(text)
    finally:
        if outfile is not None:
            out.close()


if len(sys.argv) < 3:
    sys.exit(1)

convert_type = sys.argv[1]
input_pdf = sys.argv[2]
output_file = None

if len(sys.argv) == 4:
    output_file = sys.argv[3]

if convert_type == 'pdf':
    content = pdf_converter.convert_pdf_to_txt(input_pdf)
else:
    sys.exit(1)


write_text(content_processor.process_content(content), output_file)
