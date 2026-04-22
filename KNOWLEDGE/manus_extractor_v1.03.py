# manus_extractor_v1.03.py - ORQUESTRADOR DE CONHECIMENTO MESHWAVE (INCREMENTAL)
# Protocolo: .txt -> .proc -> .bak | Processa apenas links novos comparando com o .bak anterior.
# info.sevenrock.com.br | 2026-04-21 11:15

import os
import time
import re
import urllib.request
import subprocess
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

# ========================= CONFIGURAÇÕES GLOBAIS =========================
BASE_DIR = os.getcwd()
KNOWLEDGE_DIR = os.path.join(BASE_DIR, "KNOWLEDGE")
WAIT_PER_LINK = 360
HEADLESS = True
README_PATH = os.path.join(KNOWLEDGE_DIR, "README.md")

options = Options()
if HEADLESS: options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--window-size=1920,1200")

driver = None

def init_driver():
    global driver
    if driver is None:
        driver = webdriver.Chrome(options=options)
        driver.set_page_load_timeout(120)

def close_driver():
    global driver
    if driver:
        driver.quit()
        driver = None

def git_sync(msg):
    try:
        subprocess.run(["git", "add", "."], cwd=BASE_DIR, check=True)
        subprocess.run(["git", "commit", "-m", msg], cwd=BASE_DIR, check=True)
        subprocess.run(["git", "push", "origin", "main"], cwd=BASE_DIR, check=True)
    except Exception as e:
        print(f"⚠️ Erro Git: {e}")

def extract_and_save(url, output_dir):
    try:
        driver.get(url)
        time.sleep(10)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        title_tag = soup.find('h1') or soup.find('title')
        title = title_tag.get_text(strip=True)[:100] if title_tag else "Interacao"
        safe_title = re.sub(r'[<>:"/\\|?*]', '_', title)
        folder = os.path.join(output_dir, f"{datetime.now().strftime('%Y%m%d')}_{safe_title}")
        os.makedirs(folder, exist_ok=True)
        with open(os.path.join(folder, "conteudo.md"), 'w', encoding='utf-8') as f:
            f.write(f"# {title}\nURL: {url}\n\n{soup.get_text(separator='\\n')}")
        driver.save_screenshot(os.path.join(folder, "SCREENSHOT.png"))
        print(f"   ✅ Extraído: {safe_title}")
        return True
    except Exception as e:
        print(f"   ❌ Erro no link {url}: {e}")
        return False

# ========================= LÓGICA INCREMENTAL =========================
def run_mission():
    while True:
        files = [f for f in os.listdir(KNOWLEDGE_DIR) if f.startswith("manus_links_") and f.endswith(".txt")]
        if not files:
            print("📭 Sem tarefas pendentes.")
            break
        
        target_file = files[0]
        account_name = target_file.replace("manus_links_", "").replace(".txt", "")
        txt_path = os.path.join(KNOWLEDGE_DIR, target_file)
        bak_path = os.path.join(KNOWLEDGE_DIR, f"manus_links_{account_name}.bak")
        proc_path = os.path.join(KNOWLEDGE_DIR, f"manus_links_{account_name}.proc")

        # Lê links do arquivo atual
        with open(txt_path, 'r') as f:
            current_links = [l.strip() for l in f if l.strip().startswith("http")]
        
        # Lê links já processados do .bak (se existir)
        processed_links = []
        if os.path.exists(bak_path):
            with open(bak_path, 'r') as f:
                processed_links = [l.strip() for l in f if l.strip().startswith("http")]
        
        # Identifica apenas os novos
        new_links = [l for l in current_links if l not in processed_links]
        
        if not new_links:
            print(f"ℹ️ Nenhum link novo para {account_name}. Atualizando .bak e removendo .txt")
            os.rename(txt_path, bak_path) # Sobrescreve bak com o txt consolidado
            continue

        # LOCK: .txt -> .proc
        print(f"🚀 {len(new_links)} novos links encontrados para {account_name}. Iniciando...")
        os.rename(txt_path, proc_path)
        git_sync(f"Lock: Incremental {account_name}")
        
        output_account_dir = os.path.join(KNOWLEDGE_DIR, account_name)
        os.makedirs(output_account_dir, exist_ok=True)
        
        init_driver()
        for link in new_links:
            extract_and_save(link, output_account_dir)
        
        # UNLOCK: .proc -> .bak (Consolidado)
        # O novo .bak será a lista completa (current_links)
        with open(bak_path, 'w') as f:
            for link in current_links:
                f.write(link + "\n")
        
        os.remove(proc_path)
        git_sync(f"Finish: {account_name} ({len(new_links)} novos links)")
        print(f"🏁 Lote incremental {account_name} finalizado.")

if __name__ == "__main__":
    try:
        run_mission()
    finally:
        close_driver()
