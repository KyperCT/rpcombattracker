# Taisteluiden pelaamisavustin DnD pöytäroolipeliä varten

(2020 tsoha-projekti)

(2. palautus)
Ohjelmassa voi:
- luoda käyttäjän
- kirjautua sisään
- luoda pelin (jolloin on myös pelin johtaja)
- etsiä ja liittyä peleihin
- luoda tapahtumaympäristöjä (eivät vielä tee mitään)

Kaikki tausta työ, joka vaaditaan ohjelman päätoiminnallisuuden kannalta on tehty, mutta itse toiminnallisuudesta ei ole vielä toteutettu mitään.

Testaus: Ohjelmaa voi testata osoitteessa https://rpgcombattracker.herokuapp.com/
Testausta varten voi luoda uuden käyttäjän tai käyttää valmista käyttäjää
usrname: user2
password: password2

(1. palautus)
Avustus ohjelma pyötäroolipelejä (pääasiassa dnd) varten.
 - Käyttäjä voi olla pelaaja, pelin johtaja tai ylläpitäjä
 - Käyttäjä voi luoda tunnuksen, luoda hahmon, ja liittyä peliin
 - Pelin johtaja voi luoda uusia pelejä
 - Ohjelma kertoo pelaajille toimintavuorot ja mitä pelaajat voivat tehdä vuorollaan
 - Käyttäjät kertovat ohjelmalle, mitä vuorollaan tapahtui, ja ohjelman toiminta muuttuu sen mukaisesti
 - Pelin johtaja voi lisätä omat hahmonsa (viitataan termillä "Monster")
 - Käyttäjien lisäämiä loitsuja, toimintoja, hahmoja tms. voi hakea hakutoiminnolla
 - Ohjelma jollain yksinkertaisella tavalla visualisoi pelin tapahtumia helpottaakseen toimintojen hahmottamista (Tämä on matalalla prioriteeteissa ja on hyvin mahdollisesti liian haastava toteuttaa taitotasollani)

Pöytäroolipelien haastavin opittava ominaisuus on usein niiden taistelujärjestelmä, ja tämä on varsinkin totta DnD:n kohdalla. Uusimmassa versiossa tästä pelistä taistelusta on tehty suhteellisen yksinkertaista, mutta pelaajille voi olla haastavaa seurata sitä, mitä kaikkea he voivat tehdä, sillä usein mahdollisten toimintojen kirjo on laaja. Ohjelman tavoitteena olisi pääasiassa tehdä pelin pelaamisesta helpompaa laskemalla peliin liittyvää matematiikkaa pelaajien puolesta ja selkeästi esittämällä pelaajille, mitä he voivat tehdä. Pelin johtajalla on usein myös monta asiaa seurattavana, joten toisena tavoitteena olisi myös helpottaa johtajan elämää esittämällä hänelle tärkeät toiminnot, niin ettei johtajan tarvitse muistaa kaikkea ulkoa.
