# Taisteluiden pelaamisavustin DnD pöytäroolipeliä varten

(2020 tsoha-projekti)

(Lopullinen palautus)

Ohjelmassa voi:
 - tehdä kaiken, mitä viime palautuksessa pystyi
 - Pelin johtaja voi poistaa omia hahmojaan encounterin initiative listasta
 - "Powers" -sivulla voi lisätä vomia, joita pelaajat voi käyttää
 - pelin sivulla pelaaja voi lisätä itselleen voimia, ja katsoa mitä voimia hahmollaan on pienehköstä menusta
 - Kun initiative arvot on syötetty, pelaaja näkee encounter sivulla kaikki voimansa selkeästi
 
Ohjelma on käytettävissä sen alkuperäiseen tarkoitukseen, eli projekti jossain määrin onnistui. Lopussa tuli paljon ongelmia nettisivujen kanssa, niin nettisivujen estetiikka on "nostalginen". Käyttöliittymä on toivottavasti riittävän selkeä siitä riippumatta. Sivujen toiminnallisuus on siis:
 - pelaajan perpektiivistä:
 
Ohjelmassa voi liittyä pelin johtajan peliympäristöön, lisätä hahmolle olennaiset voimat, ja sitten taistelutilanteissa syöttää pelin johtajan luomalle encounter sivulle initiativen, jonka jälkeen pelaaja näkee milloin hänen vuoro on suhteessa muihin ja mitä hänen voimat ovat.
 - Pelin johtajan perspektiivistä:
 
Ohjelmassa voi luoda peliympäristön, jonne pelaajat voivat liittyä. Kun tulee taistelun aika, voi johtaja lisätä uuden encounterin, jonne hän voi lisätä kaikkien tapahtuman vihollisten initiativet. Tämän jälkeen pelin johtaja näkee liikumisvuoron. Johtaja voi myös poistaa omia hahmojaan listasta, niin hän voi selkeästi seurata taistelua.

 - voimista:

Voimien lisäämisen voisi periaatteessa tehdä johtaja tai pelaaja. Käyttäjät voivat lisätä voimia, sillä roolipeleissä on satoja voimia, ja usein pelin johtaja saattaa keksiä itse uusia. On siis käytännöllistä, että ohjelman käyttäjät voivat itse lisätä uusia voimia hakemistoon.

Testaus: Ohjelmaa voi testata osoitteessa https://rpgcombattracker.herokuapp.com/
Testausta varten voi luoda uuden käyttäjän sign up napilla. Suosittelen luomaan 2 käyttäjää, niin voi kokeilla peliä pelaajan ja sen luojan perspektiivistä. Joitakin voimia on jo lisätty, niin testausta varten ei uusia tarvitse paljon luoda. 

(3. palautus)
Ohjelmassa voi:
 - tehdä kaiken, mitä viime palautuksessa pystyi
 - pelin sivuilla voi nimetä hahmonsa, jos on pelaaja
 - "encounter" alueella voi laittaa numeron (käytössä olisi fyysisesti heitetty nopan heitto) hahmon initiative arvoksi
 - Pelin luoja voi lisätä vihollisia, ja merkitä niiden 'initiative' arvot
 - arvon lisäämisen jälkeen näkyy lista, jossa on kaikki 'encounter':iin osallistuvien 'initiative' arvot

Ohjelma on hieman palautuksesta jäljessä. Ohjelmalla on käytännössä 2 tärkeää toimintoa: Näyttää initiative arvot, ja näyttää pelaajille mitä he voivat tehdä. Näistä initiative on toteutettu, toinen vaatii vielä työtä (ja mitään testattavaa toisesta ei vielä ole).

Testaus: Ohjelmaa voi testata osoitteessa https://rpgcombattracker.herokuapp.com/
Testausta varten voi luoda uuden käyttäjän sign up napilla. Suosittelen luomaan 2 käyttäjää, niin voi kokeilla peliä pelaajan ja sen luojan perspektiivistä

(2. palautus)
Ohjelmassa voi:
- luoda käyttäjän
- kirjautua sisään
- luoda pelin (jolloin on myös pelin johtaja)
- etsiä ja liittyä peleihin
- luoda tapahtumaympäristöjä (eivät vielä tee mitään)

Kaikki tausta työ, joka vaaditaan ohjelman päätoiminnallisuuden kannalta on tehty, mutta itse toiminnallisuudesta ei ole vielä toteutettu mitään.

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
