
import paho.mqtt.client as mqtt
import random
import time

# ==================================
# KONFIGURASI MQTT
# ==================================

BROKER = "localhost"
PORT = 1883

TOPIC_SUHU = "iot/2410020011/sensor/suhu"
TOPIC_RELAY = "iot/2410020011/aktuator/relay"
TOPIC_PWM = "iot/2410020011/aktuator/pwm"

# ==================================
# SIMULASI GPIO ESP32
# ==================================

GPIO_RELAY = 26
GPIO_LED = 2

relay_status = "OFF"
pwm_value = 0

# ==================================
# KONEKSI MQTT
# ==================================

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("ESP32 SIMULASI TERHUBUNG MQTT")

        client.subscribe(TOPIC_RELAY)
        client.subscribe(TOPIC_PWM)

        print("Subscribe topic relay:", TOPIC_RELAY)
        print("Subscribe topic PWM:", TOPIC_PWM)
    else:
        print("Koneksi gagal. Kode:", rc)


# ==================================
# MENERIMA PERINTAH DARI DASHBOARD
# ==================================

def on_message(client, userdata, msg):
    global relay_status, pwm_value

    pesan = msg.payload.decode()

    if msg.topic == TOPIC_RELAY:
        if pesan == "ON":
            relay_status = "ON"
            print("GPIO 26: RELAY MENYALA")

        elif pesan == "OFF":
            relay_status = "OFF"
            print("GPIO 26: RELAY MATI")

    elif msg.topic == TOPIC_PWM:
        try:
            pwm_value = int(float(pesan))
            pwm_value = max(0, min(255, pwm_value))

            print("GPIO 2: PWM =", pwm_value)
            print("Kecerahan LED:", round(pwm_value / 255 * 100), "%")

        except ValueError:
            print("Nilai PWM tidak valid:", pesan)


# ==================================
# MEMBUAT CLIENT MQTT
# ==================================

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

print("Menghubungkan ke broker MQTT...")

client.connect(BROKER, PORT, 60)

client.loop_start()

# ==================================
# SIMULASI SENSOR DHT22
# MENGIRIM SUHU SETIAP 3 DETIK
# ==================================

try:
    while True:

        suhu = round(random.uniform(25.0, 35.0), 1)

        client.publish(TOPIC_SUHU, str(suhu))

        print("--------------------------------")
        print("SIMULASI SENSOR DHT22")
        print("Suhu:", suhu, "°C")
        print("Relay:", relay_status)
        print("PWM:", pwm_value)
        print("Data dikirim ke Node-RED")
        print("--------------------------------")

        time.sleep(3)

except KeyboardInterrupt:
    print("\nSimulasi ESP32 dihentikan.")
    client.loop_stop()
    client.disconnect()
