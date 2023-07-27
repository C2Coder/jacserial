# Jak instalovat
Python3 a pip musí být nainstalované.

1. Instalace modulu pomocí pip

```
pip install https://github.com/C2Coder/jacserial/archive/refs/tags/v1.2.zip
```

2. Knihovna pro Jaculus
- Zkopírujte si knihovnu (jacserial.ts) ze složky jaculus-lib a dejte si jí do složky src/libs ve vašem jaculus projektu
- Jaculus knihovna má dvě funkce, 
    - jacserial.send() a do argumentu dáte string, který chcete poslat.
    - jacserial.send_RoboPlace_cmd() a do argumentu dáte string, který chcete poslat do RoboPlace, který vám můsí běžet na vašem pc.
- Python modul se používá stejně jako PySerial modul (jacserial je upravená kopie PySerial) jenom má předanou jednu funkci "readline_jac()", její výstup je string, co poslal ELKS

- Ukázka kódu je ve složce examples, pokud něco budete potřebovat, napište mi na discord (@C2Coder)

3. To je vše
