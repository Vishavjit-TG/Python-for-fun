from docx import Document

def docx_to_txt(input_file, output_file):
    print(f"Reading: {input_file}")
    
    doc = Document(input_file)
    with open(output_file, "w", encoding="utf-8") as txt_file:
        for para in doc.paragraphs:
            txt_file.write(para.text + "\n")  # Write each paragraph on a new line

    print(f"Text extracted and saved as: {output_file}")

# Convert a single file
docx_to_txt("merged_output.docx", "merged_output.txt")
