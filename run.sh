clear

echo "[+] Installing dependancies "
echo "[+] Refreshing database"
sudo pacman -Syy 

sudo pacman -S python-pmw 
echo "[+] Installing Tkinter "
pip3 install -r requirements.txt

echo "Running Application"
cd ImagEncDec
python3 enc_dec.py  
