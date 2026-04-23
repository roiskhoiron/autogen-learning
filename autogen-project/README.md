# 🤖 Petualangan Robot Pintar: Membuat Tim Pembuat Kode!

Halo teman-teman! Di sini kita akan belajar cara membuat "Tim Robot" yang bisa diajak mengobrol dan bekerja sama untuk membuat program komputer. Yuk, ikuti langkah-langkahnya!

## 🎒 Persiapan (Alat yang Dibutuhkan)

Sebelum mulai, kita butuh beberapa alat "ajaib":
1. **Python**: Ini adalah bahasa yang dimengerti oleh robot.
2. **Kunci Ajaib (API Key)**: Supaya robotnya punya "otak" untuk berpikir.

## 🚀 Langkah 1: Memasang "Mesin" Robot

Buka kotak hitam (Terminal/Command Prompt) di komputermu, lalu ketik perintah ini:

```bash
# 1. Buat rumah untuk robot (Virtual Environment)
python3 -m venv venv

# 2. Masuk ke dalam rumahnya
source venv/bin/activate

# 3. Berikan robot "buku pintar" (Install Library)
pip install autogen-agentchat autogen-ext[openai] python-dotenv
```

## 🏗️ Langkah 2: Membangun Markas Robot

Kita sudah membuat folder-folder keren supaya robotnya tidak bingung:
- `agents/`: Tempat istirahat para robot (Coder & Reviewer).
- `tasks/`: Buku tugas yang harus dikerjakan robot.
- `config.py`: Pengaturan supaya robot tahu cara terhubung ke internet.
- `.env`: Tempat menyimpan "Kunci Ajaib" rahasiamu.

## 👥 Langkah 3: Mengenal Tim Robot Kita

Di dalam markas ini, ada dua robot hebat:
1. **Robot Penulis (Coder)**: Dia yang menulis kode-kode komputer.
2. **Robot Pemeriksa (Reviewer)**: Dia yang mengecek apakah tulisan Robot Penulis sudah benar atau ada yang salah.

Mereka akan saling mengobrol sampai tugasnya selesai!

## 🏁 Langkah 4: Menjalankan Petualangan

Untuk melihat mereka bekerja, cukup ketik:

```bash
python3 autogen-project/main.py
```

Lihatlah di layarmu, robot-robot itu akan mulai saling menyapa dan bekerja sama menyelesaikan tugas matematika (seperti membuat deret angka Fibonacci)!

## 🌈 Hasil Kerja Robot (Contoh)

Penasaran bagaimana robotnya bekerja? Ini adalah contoh saat kita meminta robot membuat deret angka Fibonacci:

1. **Si Penulis (Coder)** membuat kode seperti ini:
   ```python
   # Kode ajaib untuk menghitung angka
   sequence = [0, 1]
   for i in range(2, 10):
       next_val = sequence[-1] + sequence[-2]
       sequence.append(next_val)
   print(sequence)
   ```
2. **Si Pemeriksa (Reviewer)** akan melihat kode itu dan berkata: *"Wah, kodenya sudah bagus dan rapi!"*
3. **Hasil Akhirnya**: Robot akan mengeluarkan deret angka: `[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]`

Keren, kan? Robot kita bisa mengerjakan PR matematika kita! 🥳

---
**Tips Keren:** Kalau robotnya bilang "Exceeded Quota", artinya robotnya sedang lelah dan butuh istirahat sebentar sebelum bisa berpikir lagi! 😴
