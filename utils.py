import os
import json

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def load_json(nama_file):
    try:
        with open(nama_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        return []
    except Exception as e:
        print(f"Terjadi kesalahan saat membaca file {nama_file}: {e}")
        return []

def save_json(nama_file, data):
    try:
        with open(nama_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4)
        return True
    except Exception as e:
        print(f"Terjadi kesalahan saat menyimpan file {nama_file}: {e}")
        return False
