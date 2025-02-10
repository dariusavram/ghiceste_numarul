# Joc de Ghicit Numere

## Descriere
Această aplicație este un joc simplu de ghicit numere, implementat în Python folosind Tkinter.  
Utilizatorul trebuie să ghicească un număr aleatoriu între **0 și 1000** în **15 încercări**.  
Aplicația oferă feedback în timp real, indicând dacă numărul introdus este **mai mare** sau **mai mic** decât cel căutat.

## Funcționalități
- **Generare aleatorie a numărului secret** între 0 și 1000.
- **Interfață grafică** bazată pe Tkinter.
- **Feedback în timp real** după fiecare încercare.
- **Afișarea numărului de încercări rămase**.
- **Resetarea jocului** prin apăsarea unui buton.
- **Ieșire din aplicație** prin butonul *Exit*.

## Structura Codului
- `submit()` – verifică dacă utilizatorul a ghicit numărul și oferă feedback.
- `restart()` – resetează jocul și generează un nou număr aleatoriu.
- `exit_app()` – închide aplicația.
- **Interfață grafică**:
  - Un câmp `Entry` pentru introducerea numărului.
  - Butoane pentru **verificare**, **resetare** și **ieșire**.
  - Etichete (`Label`) pentru afișarea mesajelor.

## Compilare și Rulare
1. **Asigură-te că ai Python instalat** (versiunea 3.x).
2. **Rulează scriptul** în terminal:
   ```sh
   python3 joc.py
   ```
3. **Ghicește numărul!** Introdu un număr și apasă *Apasă*.

## Exemplu de Output Vizual
- Dacă numărul este prea mic → *Mai mare*.
- Dacă numărul este prea mare → *Mai mic*.
- Dacă ai ghicit → *Ai ghicit numărul!*.
- Dacă ai pierdut → *Ai pierdut! Numărul era X*.
