# Jak instalovat
Python3 a pip musí být nainstalované,
git nemusí být nainstalovaný, ale je to doporučované.

1. Stahování repozitáře

- Pokud máte git
```
git clone https://github.com/C2Coder/jacserial
```

- pokud nemáte, stáhněte si zip

2. Instalace modulu pomocí pip

```
pip install https://github.com/C2Coder/jacserial/archive/refs/tags/v1.1.zip
```

3. Knihovna pro Jaculus
- Zkopírujte si knihovnu (jacserial.ts) ze složky jaculus-lib a dejte si jí do složky src/libs ve vašem jaculus projektu
- Jaculus knihovna má dvě funkce, 
    - jacserial.send() a do argumentu dáte string, který chcete poslat.
    - jacserial.send_RoboPlace_cmd() a do argumentu dáte string, který chcete poslat do RoboPlace, který vám můsí běžet na vašem pc.
- Python modul se používá stejně jako PySerial modul (jacserial je upravená kopie PySerial)

- Ukázka kódu je ve složce examples, pokud něco budete potřebovat, napište mi na discord (@C2Coder)

4. To je vše
