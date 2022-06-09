## Vježba 1

Prvo je trebalo instalirat WinHex priko poveznice. Kad se instalira, otvori se editor:

![WinHex editor](assets/WinHexEditor.png)

Nakon toga, preko File -> Open se otvore ova tri datoteke koje smo downloadali:

![Winhex editor sa otvorenim datotekama](assets/WinHexEditorSaOtovrenimDatotekama.png)

Kako pročitat koji je tip datoteke ? -> pogledamo prva dva hexa unutar editora za svaki file te ih onda potražimo u tablici potpisa. Ta prva dva hexa predstavljaju potpis datoteke i tako možemo otkrit koji je tip datoteke

# file1

---

Za prvi file, ovo je njegov potpis:

![Potpis prve datoteke](assets/file1_Potpis.png)

Kada to potražimo u tablici, vidit ćemo da je ovo neki kompresirani file(.zip, .rar)

![Lista potpisa](assets/zip_potpis.png)

To možemo provjerit tako što promijenimo ime datoteci i otvorimo je:

![file1.zip](assets/file1_renamed.png)
![Sadržaj file1](assets/file1_content.png)

# file2.txt

---

Potpis za drugu datoteku:

![Potpis druge datoteke](assets/file2_Potpis.png)

Kad potražimo u tablici, vidit ćemo da je to .vhdx file, tj. Windows Virtual PC Windows 8 Virtual Hard Disk file format

![Lista potpisa](assets/vhdx_potpis.png)

Nakon promjene imena:

![file2.vhdx](assets/file2_renamed.png)
Yeah...neću van ovo otvorit

# file3

---

Potpis za treću datoteku:

![Potpis treće datoteke](assets/file3_Potpis.png)

Kada se potraži u tablici, vidimo da je ovo .PDF file

![Lista potpisa](assets/pdf_potpis.png)

Provjera tako što promijenimo ime datoteci:

![file3.pdf](assets/file3_renamed.png)
![It empty](assets/it_empty.png)
