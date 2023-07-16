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

- Pokud jste si stáhli repozitář pomocí gitu
```
pip install ./jacserial
```

- Pokud jste si stáhli zip
```
pip install ./jacserial-master.zip
```
3. Knihovna pro Jaculus
- Zkopírujte si knihovnu (jacserial.ts) ze složky jaculus-lib a dejte si jí do složky src/libs ve vašem jaculus projektu
- Jaculus knihovna má jedinou funkci, jacserial.send() a do argumentu dáte string, který chcete poslat.

- Python modul se používá stejně jako PySerial modul (jacserial je upravená kopie PySerial)

- Ukázka kódu je ve složce examples, pokud něco budete potřebovat, napište mi na discord (@C2Coder)

4. To je vše

