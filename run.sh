clear

echo "[+] Installing dependancies "
echo "[+] Refreshing database"
sudo apt update -y  
sudo apt install python3-tk -y  
echo "[+] Installing Tkinter "
pip3 install -r requirements.txt

echo "Running Application"
python3 main.py
