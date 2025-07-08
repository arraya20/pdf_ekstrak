from PyPDF2 import PdfReader, PdfWriter

def extract_pages(input_pdf_path, output_pdf_path, start_page, end_page):
    try:
        reader = PdfReader(input_pdf_path)
        writer = PdfWriter()

        # PyPDF2/pypdf menggunakan indeks berbasis 0, jadi halaman 50-60 adalah indeks 49-59
        for i in range(start_page - 1, end_page):
            if i < len(reader.pages): # Pastikan halaman ada
                writer.add_page(reader.pages[i])
            else:
                print(f"Peringatan: Halaman {i+1} tidak ditemukan di PDF.")
                break # Hentikan jika melebihi jumlah halaman yang tersedia

        with open(output_pdf_path, 'wb') as output_file:
            writer.write(output_file)
        print(f"Halaman {start_page}-{end_page} berhasil diekstrak ke '{output_pdf_path}'")
    except FileNotFoundError:
        print(f"Kesalahan: File '{input_pdf_path}' tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

# --- Konfigurasi Anda ---
input_file = "/path/to/file"  # Ganti dengan path ke file PDF Anda
output_file = "path/to/file" # Ganti dengan path dan nama file keluaran
halaman_mulai = 26
halaman_akhir = 37
# -------------------------

extract_pages(input_file, output_file, halaman_mulai, halaman_akhir)