# Redis Demo Task API

## Deskripsi Proyek

Proyek ini adalah REST API sederhana untuk manajemen task menggunakan Flask sebagai web framework dan Redis sebagai penyimpanan data in-memory.

API ini mengikuti prinsip Clean Architecture dengan pemisahan layer:

- domain
- interfaces
- infrastructure
- use_cases
- web

## Fitur Sistem

- Menambahkan task (POST /task)
- Mengambil task berdasarkan ID (GET /task/<id>)
- Penyimpanan data menggunakan Redis
- Struktur kode terorganisir menggunakan Clean Architecture

## Struktur Folder Proyek

```
redis-demo/
│
├── app/
│   ├── domain/
│   ├── interfaces/
│   ├── infrastructure/
│   ├── use_cases/
│   └── web/
│
├── main.py
├── requirements.txt
└── README.md
```

## Cara Instalasi

1. Pastikan Python sudah terpasang (3.8+).
2. Pastikan Redis berjalan di `localhost:6379`.
3. Buat virtual environment (opsional):
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\\Scripts\\activate  # Windows
   ```
4. Install dependensi:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan Aplikasi

1. Jalankan Redis server jika belum berjalan:
   ```bash
   redis-server --port 6379
   ```
2. Jalankan aplikasi:
   ```bash
   python main.py
   ```
3. API akan tersedia di `http://127.0.0.1:5000`.

## Contoh Penggunaan API

- Menambahkan task:

  ```bash
  curl -X POST http://127.0.0.1:5000/task \
    -H "Content-Type: application/json" \
    -d '{"title": "Belajar Flask"}'
  ```

- Mengambil task berdasarkan ID:
  ```bash
  curl http://127.0.0.1:5000/task/{task_id}
  ```

## Teknologi yang Digunakan

- Python
- Flask
- Redis
- redis-py

## Penulis

- Nama: Hanifa Ramadhani
- Project: redis-demo

## Daftar Prompt yang Digunakan

- Buatkan project Python dengan Clean Architecture dan Redis sebagai data store
- Struktur app/domain, interfaces, infrastructure, use_cases, web
- Tambahkan `main.py` di root
- Gunakan Flask untuk API dan redis-py untuk koneksi Redis
- Redis harus connect ke localhost:6379
- Buat Task entity (id, title, completed)
- Implementasikan TaskRepository interface dan RedisRepository
- TaskService menangani business logic
- Tentukan endpoint POST /task dan GET /task/<id>
- Sertakan contoh operasi Redis set/get
