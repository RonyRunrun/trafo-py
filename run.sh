#!/bin/bash
set -e  # stop jika ada error

# --- setup virtual environment jika belum ada ---
if [ ! -d ".venv" ]; then
  echo "🔧 Membuat virtual environment .venv ..."
  python3 -m venv .venv
fi

# --- aktifkan virtual environment ---
echo "✅ Mengaktifkan virtual environment..."
source .venv/bin/activate

# --- install dependensi jika uvicorn belum ada ---
if ! command -v uvicorn &> /dev/null; then
  echo "📦 Menginstal FastAPI dan Uvicorn..."
  pip3 install --upgrade pip
  pip3 install fastapi uvicorn
fi

# --- jalankan server FastAPI ---
echo "🚀 Menjalankan FastAPI di http://127.0.0.1:8000 ..."
uvicorn main:app --reload
