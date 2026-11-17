# Customer Service Chatbot (RAG)

Chatbot layanan pelanggan yang menjawab pertanyaan berdasarkan dokumen perusahaan (PDF, DOCX, TXT, dan FAQ JSON) dengan pendekatan Retrieval-Augmented Generation (RAG). Model bahasa berjalan lokal melalui Ollama, jadi tidak membutuhkan API berbayar.

## Fitur

- Memuat basis pengetahuan dari file PDF, DOCX, TXT, dan FAQ (`faq.json`).
- Hybrid retrieval: menggabungkan semantic search (ChromaDB + `all-MiniLM-L6-v2`) dan keyword search (BM25).
- Re-ranking hasil pencarian dengan cross-encoder `ms-marco-MiniLM-L-6-v2`.
- Query rewriting: pertanyaan lanjutan diubah menjadi pertanyaan lengkap berdasarkan riwayat percakapan.
- Memori percakapan per sesi (hingga 10 giliran terakhir).
- Menjawab "informasi belum tersedia" jika konteks yang relevan tidak ditemukan.
- Antarmuka chat berbasis React dengan dukungan Markdown.

## Arsitektur

```
Pertanyaan user (React)
        │  POST /chat
        ▼
FastAPI ──► Query rewriting (Ollama)
        ──► Hybrid search: ChromaDB (semantic) + BM25 (keyword)
        ──► Re-ranking (cross-encoder), ambil 3 konteks teratas
        ──► Prompt builder + riwayat percakapan
        ──► Ollama (qwen3:4b)
        ▼
Jawaban ke user
```

## Teknologi

| Bagian | Teknologi |
| --- | --- |
| Backend | Python, FastAPI, Uvicorn |
| LLM | Ollama (`qwen3:4b`) |
| Vector database | ChromaDB |
| Embedding dan re-ranking | Sentence Transformers |
| Keyword search | rank-bm25 |
| Pemrosesan dokumen | pypdf, python-docx |
| Frontend | React 19, Vite, Tailwind CSS, shadcn/ui, Axios |

## Struktur folder

```
Backend/
├── main.py            # Endpoint FastAPI (/chat)
├── Chatbot.py         # Alur utama: retrieval → prompt → LLM
├── ingest.py          # Memuat dokumen ke ChromaDB
├── config.py          # Model, path database, parameter retrieval
├── memory.py          # Riwayat percakapan per sesi
├── Knowledge/         # Dokumen basis pengetahuan
├── loaders/           # Loader PDF, DOCX, TXT, FAQ
├── processing/        # Chunking dan tokenisasi
└── services/          # Hybrid search, BM25, re-ranker, query rewriter
Frontend/
└── src/               # Komponen React (chat, sidebar, layout)
```

## Cara menjalankan

### Prasyarat

- Python 3.10+
- Node.js 18+
- [Ollama](https://ollama.com) sudah terpasang

### 1. Siapkan model Ollama

```bash
ollama pull qwen3:4b
```

### 2. Backend

```bash
cd Backend
python -m venv venv
venv\Scripts\activate        # Windows (macOS/Linux: source venv/bin/activate)
pip install -r requirements.txt
python ingest.py             # memuat dokumen di folder Knowledge ke ChromaDB
uvicorn main:app --reload
```

Backend berjalan di `http://127.0.0.1:8000`.

### 3. Frontend

```bash
cd Frontend
npm install
npm run dev
```

Buka `http://localhost:5173` di browser.

## Menambah pengetahuan

Taruh file PDF, DOCX, atau TXT di `Backend/Knowledge/`, atau tambahkan pasangan tanya-jawab di `faq.json`, lalu jalankan ulang `python ingest.py`.

## Konfigurasi

Parameter utama ada di `Backend/config.py`:

| Parameter | Nilai | Keterangan |
| --- | --- | --- |
| `MODEL_NAME` | `qwen3:4b` | Model Ollama untuk menjawab |
| `EMBEDDING_MODEL` | `all-MiniLM-L6-v2` | Model embedding |
| `RERANK_MODEL` | `cross-encoder/ms-marco-MiniLM-L-6-v2` | Model re-ranking |
| `TOP_K` | `10` | Jumlah kandidat dari tiap metode pencarian |
| `FINAL_TOP_K` | `3` | Jumlah konteks setelah re-ranking |

## Screenshot

_Tambahkan screenshot tampilan chat di sini._

## Penulis

Bertus, mahasiswa Sistem Informasi, Universitas Multimedia Nusantara
[LinkedIn](https://www.linkedin.com/in/bertus-s-50878b324) · [GitHub](https://github.com/Bertusss1)
