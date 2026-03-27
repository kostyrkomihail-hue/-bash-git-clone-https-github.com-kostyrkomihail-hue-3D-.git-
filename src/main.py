
python

-- coding: utf-8 --
"""
Єдиний файл програми з базовим захистом.
"""

import hashlib
import os
import sys

🔹 Прив’язка до пристрою (Device Binding)
def getdeviceid():
    # Для Android можна використати ANDROID_ID або інший унікальний параметр
    return hashlib.sha256(os.uname().nodename.encode()).hexdigest()

AUTHORIZEDDEVICE = "ТВОЙХЕШ_ПРИСТРОЮ"  # сюди вставляється хеш твого пристрою

def check_license():
    currentdevice = getdevice_id()
    if currentdevice != AUTHORIZEDDEVICE:
        print("❌ Ліцензія недійсна. Програма не може працювати.")
        sys.exit(1)
    else:
        print("✅ Ліцензія підтверджена. Програма працює.")

🔹 Основна функція
def main():
    check_license()
    print("Привіт, 3D‑проект у єдиному файлі!")
    # Тут можна додати 3D‑логіку, аналітику, AR/VR, таблиці тощо

if name == "main":
    main()
