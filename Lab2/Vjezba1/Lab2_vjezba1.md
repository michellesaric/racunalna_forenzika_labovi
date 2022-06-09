Prvo je trebalo instalirat WinHex priko poveznice. Kad se instalira, otvori se editor:

![WinHex editor](image.png)

Nakon toga, preko File -> Open se otvore ova tri datoteke koje smo downloadali:

![Winhex editor sa otvorenim datotekama](image.png)

Kako pročitat koji je tip datoteke ? -> pogledamo prva dva hexa unutar editora za svaki file te ih onda potražimo u tablici potpisa. Ta prva dva hexa predstavljaju potpis datoteke i tako možemo otkrit koji je tip datoteke

# file1

Za prvi file, ovo je njegov potpis:

![Potpis prve datoteke](image.png)

Kada to potražimo u tablici, vidit ćemo da je ovo neki kompresirani file(.zip, .rar)

![Lista potpisa](image.png)

To možemo provjerit tako što promijenimo ime datoteci i otvorimo je:

![file1.zip](image.png)
![Sadržaj file1](image.png)

# file2.txt

Potpis za drugu datoteku:

![Potpis druge datoteke](image.png)

Kad potražimo u tablici, vidit ćemo da je to .vhdx file, tj. Windows Virtual PC Windows 8 Virtual Hard Disk file format

![Lista potpisa](image.png)

Nakon promjene imena:

![file2.vhdx](image.png)
Yeah...neću van ovo otvorit

# file3

Potpis za treću datoteku:

![Potpis treće datoteke](image.png)

Kada se potraži u tablici, vidimo da je ovo .PDF file

![Lista potpisa](image.png)

Provjera tako što promijenimo ime datoteci:

![file3.pdf](image.png)
![It empty](image.png)
