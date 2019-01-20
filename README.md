### Virtual Dedicated Server
Вам потребуется [виртуальный сервер](https://ru.wikipedia.org/wiki/VPS) в Европе с которого будут доступны заблокированные в России ресурсы, но при этом приемлимый пинг. 
Параметры сервера - минимальные, по сути нам нужен удаленный роутер с публичным IP адресом. 
* **Микро VDS в Нидерландах** *
  * виртуализация KVM 
  * 1 ядро Intel(R) Xeon(R) CPU E5-2680 v2 @ 2.80GHz
  * 768 МБ оперативной памяти
  * 10 ГБ места на SSD-диске
  * IPv4 адрес, 8ТБ трафика
  * 150руб в месяц
[VDS.SH](https://vds.sh) - при заказе обратите внимание, что от языка сайта зависит валюта оплаты - RUB/EUR и регистрация компании - Россия/Европа

![MicroVDS](/img/001.png)


## openvpn-install
Этот скрипт позволит вам настроить собственный VPN-сервер не более, чем за минуту, даже если вы ранее не использовали OpenVPN. 
Он был разработан, чтобы быть максимально ненавязчивым и универсальным.

### Installation
Run the script and follow the assistant:

`wget https://git.io/vpn -O openvpn-install.sh && bash openvpn-install.sh`

Once it ends, you can run it again to add more users, remove some of them or even completely uninstall OpenVPN.

### I want to run my own VPN but don't have a server for that
You can get a little VPS from just $1/month at [VirMach](https://billing.virmach.com/aff.php?aff=4109&url=billing.virmach.com/cart.php?gid=1).

### Donations

If you want to show your appreciation, you can donate via [PayPal](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=VBAYDL34Z7J6L) or [cryptocurrency](https://pastebin.com/raw/M2JJpQpC). Thanks!
