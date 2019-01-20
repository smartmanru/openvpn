## Поднимаем свой OpenVPN сервер за пару минут.
![preview](/img/003.png)
### VDS: Virtual Dedicated Server
Вам потребуется [виртуальный сервер](https://ru.wikipedia.org/wiki/VPS) в Европе с которого будут доступны заблокированные в России ресурсы, но при этом приемлимый пинг. 
Параметры сервера - минимальные, по сути нам нужен удаленный роутер с публичным IP адресом. 

* [**Микро VDS в Нидерландах от VDS.SH**](https://vds.sh) 
  * 1 ядро Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz
  * 768 МБ оперативной памяти
  * виртуализация KVM 
  * 10 ГБ места на SSD-диске
  * IPv4 адрес, 8ТБ трафика
  * 150руб в месяц
  
❗️ **От языка сайта зависит регистрация компании - Россия/Европа.**

### Initial configuration
💿 Ставим Centos7 без предустановленного ПО.
После оплаты начнется инициализация виртуального сервера и установка операционной системы.
Процесс займет несколько минут.

![startconfing](/img/002.png)

📝 По окончании появится кнопка "Инструкция" - нажимаем и сохраняем данные для управления сервером

> **Активация Виртуального сервера**
>  - Здравствуйте, Кевин!
>  Настоящим письмом уведомляем, что на ваше имя был зарегистрирован Виртуальный Сервер.
>  Предлагаем распечатать данное сообщение для удобства использования в дальнейшем.

> **Информация о cервере:** - 🔐
>   * IP-адрес сервера: 91.xxx.xxx.xxx
>   * Пользователь: root
>   * Пароль: 0xm1Jej3xxxx

> **VMmanager - внешняя панель управления сервером** - 🔐
>    - Ссылка: https://vm-nl.vds.sh/vmmgr
>    - Пользователь: yourname
>    - Пароль: gjQeB212xxxx

### SSH: Secure Shell
🛠 Устанавливаем пакет утилит [PuTTY](https://www.putty.org)

* Запускаем PuTTY
* Вводим IP-адрес сервера и жмем 'Open'
* На Security Alert жмем "Да"
* Вводим пользователя(root) и пароль

Загружаем и запускаем скрипт настройки OpenVPN
```bash 
wget https://raw.githubusercontent.com/mediatube/openvpn/master/openvpn-install.sh

bash openvpn-install.sh
```
Задаем параметры отвечая на вопросы скрипта
![startconfing](/img/002.png)
Запускаем установку нажатием любой кнопки, в конце будет сгенерирован конфиг для клиента:
```bash
Your client configuration is available at: /root/client-amst-udp1.1.ovpn
```
Копируем конфиг с сервера на компьютер
Из командной строки Windows:
```bash
scp root@91.xxx.xxx.xxx:/root/client-amst-udp1.1.ovpn C:\Users\slavikmipt
```
Устанавливаем [PuTTY](https://www.putty.org)
Подключаемся к серверу по SSH под root
Запускаем openvpn-installer.py
Копируем конфиг
scp root@s7.mediatube.xyz:client-ne-udp1.2.ovpn C:\Users\slavikmipt
### OpenVPN Client
Устанавливаем клиент OpenVPN
https://openvpn.net/community-downloads/

Импортируем конфиг и подключаемся к VPN
**TODO:**
### RSA keypair
Генерируем ключи, защищаем ssh

### close 22 port
