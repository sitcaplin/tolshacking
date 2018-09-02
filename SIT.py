TOOLS

def menu():

    print("""
========================================================================================================================
||.########..#######...#######..##........######....##....##.########...#######...##....##.##.###.......##..########''||
||....##....##.....##.##.....##.##.......##....##...##....##.##....##.##.......##.##...##..##.##.##.....##.##......##.||
||....##....##.....##.##.....##.##.......##.........##....##.##....##.##..........##..##...##.##..##....##.##.........||
||....##....##.....##.##.....##.##........######....########.########.##..........####.....##.##...##...##.##...#####.||
||....##....##.....##.##.....##.##.............##...##....##.##....##.##..........##..##...##.##....##..##.##......##.||
||....##....##.....##.##.....##.##.......##....##...##....##.##....##.##.......##.##...##..##.##.....##.##.##......##.||
||....##.....#######...#######..########..######....##....##.##....##...#######...##....##.##.##......####..#######...||
========================================================================================================================
Created By SIT_GM
Blogs: http://www.x7sit.me
Team:Shutdown Indo Team
Copyright: @SIT2018
================
Selamat Datang!
================
::::::::::::::::::::::::::::::::::
00. Silahkan Pilih TOOLS Hacking
::::::::::::::::::::::::::::::::::
1. Install Nmap 
2. Install Hydra
3. Install SQLMap
4. Install Metasploit
5. Install ngrok
6. Install Kali Nethunter
7. Install angryFuzzer
8. Install Red_Hawk
9. Install Weeman
10.Install IPGeoLocation
11.Install Cupp
12.Instagram Bruteforcer (instahack)
13.Twitter Bruteforcer   (TwitterSniper)
14.Install Ubuntu
15.Install Fedora
16.Install viSQL
17.Install Hash-Buster
18.Install D-TECT
19.Install routersploit
==========================================
99. Keluar
==========================================
""")

loop = True

while loop:
    menu()
    what = input("#: ")
    if what == "00":
        print("================================")
        print("This will install: nmap, hydra, sqlmap, metasploit, ngrok, angryFuzzer, red_hawk, weeman, IPGeoLocation, cupp, instahack, TwitterSniper, Hash-Buster, D-TECT, routersploit and viSQL with one click.")
        print("----------------")
        hm = input("[?] Apakah anda ingin melanjutkan? (y/n): ")
        print("================================")
        if hm == "Y":
            print("========================================================")
            print("[+] Silahkan di tunggu...")
            print("Perintah sedang di proses.")
            print("========================================================")
            os.system("pkg update")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y python2")
            os.system("pkg install -y wget")
            os.sysetm("pkg install -y nmap")
            os.system("plg install -y hydra ")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg install wget")
            os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
            os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
            os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
            os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
            os.system("cd /data/data/com.termux/files/home && bundle install")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
            os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
            os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home && pip2 install requests")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y php")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y python2")
            os.system("pkg install -y git")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
            os.system("cd /data/data/com.termux/files/home && cd weeman")
            os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
            os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
            os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
            os.system("cd /data/data/com.termux/files/home")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pkg install -y nano")
            os.system("pip install requests")
            os.system("pip install beautifulsoup4")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python")
            os.system("pip install mechanicalsoup")
            os.system("pkg install -y nano")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            os.system("clear")
            print("========================================")
            print("[+] everything Install Sukses :)")
            print("[+] Senang bisa Hacking <3")
            print("========================================")
        else:
            rmenu = input("[?] Kembali ke Menu? (y/n): ")
            if rmenu == "Y":
                menu()
            else:
                break
    if what == "1":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y nmap")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] nmap Install Sukses :)")
        print("[+] Klik 'nmap' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "2":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y hydra")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] hydra Install Sukses :)")
        print("[+] Klik 'hydra untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "3":
        os.system("cd /data/data/com.termux/files/home")
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/sqlmapproject/sqlmap.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] SQLMap Install Sukses :)")
        print("[+] Klik sqlmap folder and type 'python2 sqlmap.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "4":
        os.system("pkg install -y wget")
        os.system("cd /data/data/com.termux/files/home && wget https://Auxilus.github.io/metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && bash metasploit.sh")
        os.system("cd /data/data/com.termux/files/home && cd metasploit-framework")
        os.system("cd /data/data/com.termux/files/home && gem install bundle --pre")
        os.system("cd /data/data/com.termux/files/home && bundle config build.nokogiri --use-system-libraries")
        os.system("cd /data/data/com.termux/files/home && bundle install")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Metasploit Install Sukses :)")
        print("[+] Klik 'msfconsole' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "5":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/themastersunil/ngrok.git")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] ngrok Install Sukses :)")
        print("[+] Klik ngrok folder and type './ngrok http 80' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "6":
        os.system("pkg update -y")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Hax4us/Nethunter-In-Termux.git")
        os.system("cd /data/data/com.termux/files/home && cd Nethunter-In-Termux && chmod +x kalinethunter")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] Nethunter Install Sukses :)")
        print("[+] Klik Nethunter-In-Termux folder and type './kalinethunter' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "7":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/ihebski/angryFuzzer.git")
        os.system("cd /data/data/com.termux/files/home && cd angryFuzzer")
        os.system("cd /data/data/com.termux/files/home && pip2 install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home && pip2 install requests")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] angryFuzzer Install Sukses :)")
        print("[+] Klik angryFuzzer folder and type 'python2 angryFuzzer.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "8":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y php")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Tuhinshubhra/RED_HAWK")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] RED_HAWK Install Sukses :)")
        print("[+] Klik RED_HAWK folder and type 'php rhawk.php' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "9":
        os.system("pkg update -y")
        os.system("pkg install -y python2")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/evait-security/weeman.git")
        os.system("cd /data/data/com.termux/files/home && cd weeman")
        os.system("cd /data/data/com.termux/files/home && chmod +x weeman.py")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] weeman Install Sukses  :)")
        print("[+] Klik weeman folder and type 'python2 weeman.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "10":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/maldevel/IPGeoLocation.git")
        os.system("cd /data/data/com.termux/files/home && cd IPGeoLocation")
        os.system("cd /data/data/com.termux/files/home && pip install -r requirements.txt")
        os.system("cd /data/data/com.termux/files/home")
        print("====================================")
        print("[+] IPGeoLocation Install Sukses :)")
        print("[+] Klik IPGeoLocation folder and type 'python ipgeolocation.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "11":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Mebus/cupp.git")
        print("====================================")
        print("[+] Cupp Install Sukses :)")
        print("[+] Klik cupp folder and type 'python cupp3.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "12":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pkg install -y nano")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/avramit/instahack.git")
        print("====================================")
        print("[+] Instahack Install Sukses :)")
        print("[+] Klik instahack folder and type 'python hackinsta.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "13":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python")
        os.system("pip install mechanicalsoup")
        os.system("pkg install -y nano")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/abdallahelsokary/TwitterSniper.git")
        print("====================================")
        print("[+] TwitterSniper Install Sukses :)")
        print("[+] Klik TwitterSniper folder and type 'python TwitterSniper.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "14":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/Neo-Oli/termux-ubuntu.git")
        os.system("cd /data/data/com.termux/files/home && cd termux-ubuntu && bash ubuntu.sh")
        print("====================================")
        print("[+] Ubuntu Install Sukses :)")
        print("[+] Klik termux-ubuntu folder and type './start.sh' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "15":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y wget")
        os.system("apt update && apt install wget -y && /data/data/com.termux/files/usr/bin/wget https://raw.githubusercontent.com/nmilosev/termux-fedora/master/termux-fedora.sh")
        print("====================================")
        print("[+] Fedora Install Sukses :)")
        print("[+] Klik 'sh termux-fedora.sh f26_arm64' or 'sh termux-fedora.sh f26_arm' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "16":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/blackvkng/viSQL.git")
        print("====================================")
        print("[+] viSQL Install Sukses :)")
        print("[+] Klik viSQL folder and type 'python2 viSQL.py --help' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "17":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/UltimateHackers/Hash-Buster.git")
        print("====================================")
        print("[+] Hash-Buster Install Sukses :)")
        print("[+] Klik Hash-Buster folder and type 'python2 hash.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "18":
        os.system("pkg update -y")
        os.system("pkg install -y git")
        os.system("pkg install -y python2")
        os.system("cd /data/data/com.termux/files/home && git clone https://github.com/shawarkhanethicalhacker/D-TECT.git")
        print("====================================")
        print("[+] Hash-Buster Install Sukses :)")
        print("[+] Klik Hash-Buster folder and type 'python2 hash.py' untuk memulai.")
        print("====================================")
        rmenu = input("[?] Kembali ke Menu? (y/n): ")
        if rmenu == "Y":
            menu()
        else:
            break
    elif what == "19":
            os.system("pkg update -y")
            os.system("pkg install -y git")
            os.system("pkg install -y python2")
            os.system("cd /data/data/com.termux/files/home && git clone https://github.com/reverse-shell/routersploit.git")
            os.system("cd /data/data/com.termux/files/home && cd routersploit")
            os.system("pip2 install -r requirements.txt")
            os.system("pip2 install -r requirements-dev.txt")
            os.system("pip2 install -r requests")
            print("====================================")
            print("[+] routersploit Install Sukses :)")
            print("[+] Klik routersploit folder and type 'python2 rsf.py' untuk memulai.")
            print("====================================")
            rmenu = input("[?] Kembali ke Menu? (y/n): ")
            if rmenu == "Y":
                menu()
            else:
                break
    elif what == "99":
        print("TERIMAKASIH")
        break