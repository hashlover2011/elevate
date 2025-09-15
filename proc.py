import os;import random;import time
def kill_process():
    random_list = ["update-notifier", "gnome-software", "snapd", "deja-dup-monitor", "cache"]
    while True:
        if random.choice(random_list) == "cache":
            print("[*] Cleaning cache...")
            os.system("sync; echo 3 | tee /proc/sys/vm/drop_caches")
        else:
            r = random.choice(random_list)
            print(f"[*] Killing {r}.")
            time.sleep(2)
            os.system(f"killall {r}")
        time.sleep(30)
kill_process()
