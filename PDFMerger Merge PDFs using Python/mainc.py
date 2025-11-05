from PyPDF2 import PdfMerger   # Import PdfMerger class to merge PDF files
import os                      # Import os module to check file path existence

# Create a PdfMerger object for merging PDF files
merger = PdfMerger()

# Empty list to store all valid PDF file paths entered by user
pdfs = []

# Show example path format to help user enter correct path
print("📌 Example path format:")
print(r"C:\Users\SHREE\Downloads\file1.pdf\n")

# Ask user how many PDF files they want to merge
while True:  # Loop continues until valid input is given
    try:
        n = int(input("How many PDF files do you want to merge?\n"))
        break  # Exit loop if valid number
    except ValueError:
        print("❌ Please enter a valid number!")  # Error if user types non-numeric value

# Loop to take full PDF file paths one by one
for i in range(n):
    while True:  # Keep asking until valid path is entered
        file_path = input(f"Enter FULL PATH of PDF {i + 1} (include .pdf): ").strip()

        # ✅ Check if file exists at the given path
        if os.path.isfile(file_path):
            pdfs.append(file_path)  # Add file path to list
            break                   # Exit inner loop once valid file found
        else:
            # Error message if file is not found
            print(f"❌ File not found: {file_path}")
            print("👉 Please give correct path. Example:")
            print(r"C:\Users\SHREE\Downloads\somefile.pdf")

# ✅ Loop through all file paths and add each PDF to the merger
for pdf in pdfs:
    merger.append(pdf)

# Name of merged output file
output_name = "merged2-pdf.pdf"

# Save the merged PDF file
merger.write(output_name)

# Close the merger object to free system resources
merger.close()

# Final success messages
print(f"\n✅ PDFs merged successfully!")
print(f"📂 Output file: {output_name}")
