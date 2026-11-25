# Proyek Mini IoT Pertemuan 10

## Dashboard Node-RED untuk Kontrol Relay dan Monitoring Suhu

Proyek ini merupakan tugas individu mata kuliah Pemrograman IoT. Proyek ini dibuat untuk melakukan monitoring suhu dan mengontrol perangkat melalui dashboard Node-RED menggunakan komunikasi MQTT.

## Fitur
- Monitoring suhu secara real-time.
- Grafik perubahan suhu.
- Kontrol Relay ON/OFF.
- Pengaturan kecerahan LED menggunakan PWM (0–255).
- Komunikasi MQTT antara simulasi perangkat dan Node-RED.

## Teknologi yang Digunakan
- Node-RED
- MQTT (Mosquitto)
- Python
- Paho-MQTT

## Struktur File
- `flow_proyek_pertemuan10.json` – Flow Node-RED.
- `python/simulasi_esp32.py` – Program simulasi ESP32.
- `dokumentasi/` – Screenshot dashboard dan video demonstrasi.

## Topik MQTT
- `iot/2410020011/sensor/suhu`
- `iot/2410020011/aktuator/relay`
- `iot/2410020011/aktuator/pwm`

## Identitas
- Nama: Nikmatul Rizkiyah
- NIM: 2410020011
- Mata Kuliah: Pemrograman IoT

