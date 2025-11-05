from PyPDF2 import PdfMerger
import os

merger = PdfMerger()
pdfs = []

print("📌 Example path format:")
print(r"C:\Users\SHREE\Downloads\file1.pdf\n")

# Ask how many PDFs to merge
while True:
    try:
        n = int(input("How many PDF files do you want to merge?\n"))
        break
    except ValueError:
        print("❌ Please enter a valid number!")

# Take full file paths
for i in range(n):
    while True:
        file_path = input(f"Enter FULL PATH of PDF {i + 1} (include .pdf): ").strip()

        # ✅ Check if file exists
        if os.path.isfile(file_path):
            pdfs.append(file_path)
            break
        else:
            print(f"❌ File not found: {file_path}")
            print("👉 Please give correct path. Example:")
            print(r"C:\Users\SHREE\Downloads\somefile.pdf")

# ✅ Merge files
for pdf in pdfs:
    merger.append(pdf)

output_name = "merged2-pdf.pdf"
merger.write(output_name)
merger.close()

print(f"\n✅ PDFs merged successfully!")
print(f"📂 Output file: {output_name}")
