# Docker Tag Images, Using Python Slim Buster.
FROM kenzo404/lynxuser:Buster
# =========================================
#              Lynx - Userbot
# =========================================
RUN git clone -b KENZO-404-Lynx-Deploy https://github.com/KENZO-404/Lynx-Userbot /root/userbot
RUN mkdir /root/userbot/.bin
RUN pip install --upgrade pip setuptools
WORKDIR /root/userbot

# Install Requirements Packages
RUN pip3 install -r https://raw.githubusercontent.com/KENZO-404/Lynx-Userbot/KENZO-404-Lynx-Deploy/requirements.txt

# Finishim
CMD ["python3","-m","userbot"]
