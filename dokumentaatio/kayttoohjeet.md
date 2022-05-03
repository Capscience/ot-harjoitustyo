# Käyttöohjeet

## Asennus

Varmista ensin, että koneelta löytyy poetry komennolla
```
poetry --version
```
Kun poetry on asennettuna, aja sovelluksen hakemistossa komento
```
poetry install
```

Nyt sovelluksen voi käyttistää komennolla
```
poetry run invoke start
```

## Käyttö
___

### Projektin luominen
___

Ensimmäistä kertaa käynnistyessään ohjelma luo tyhjän tietokannan. Uuden projektin voi luoda oikeasta reunasta kohdasta "Luo uusi projekti". Projektin nimi kirjoitetaan tekstikenttään, ja sen tulisi muodostua yhdestä lyhyestä sanasta (ei välttämätöntä). Projekti lisätään "Lisää projekti" napista, jolloin oikealle puolelle tulee näkyviin kyseisen projektin hallintapalkki. Luotujen projektien hallintapalkit haetaan tietokannasta, kun sovelluksen avaa seuraavan kerran.

### Projektien ajastaminen
___

Hallintapalkin nappi "Play" käynnistää ajastimen. "Pause" pysäyttää ajastimen väliaikaisesti. "Stop" -nappi nollaa ajastimen, ja tallentaa ajastimessa näkyvän ajan tietokantaan.

### Statistiikkojen hakeminen
___

Ikkunan oikeassa reunassa on kohta "Statistiikat". Sovellus hakee käynnistyessään oletuksena meneillään olevan kuukauden tiedot. Painamalla "Hae tiedot" ilman, että tekstikenttään on kirjoitettu mitään, voidaan hakea kaikki tallennetut tiedot. Tietyn kuukauden tiedot voidaan hakea kirjoittamalla vuosi ja kuukausi tekstikenttään ennen hakunapin painamista. Aika tulee kirjoittaa muodossa YYYY-MM, tai YYYY-MM-DD. Esimerkiksi vuoden 2022 toukokuun tilastot saa haulla `2022-05`, ja päivän 3.5.2022 haulla `2022-05-03`.

### Projektin poistaminen
___

### HUOM! Projektin poistaminen poistaa myös kyseisen projektin tallennetut datat!
Projektin poistaminen tapahtuu oikean reunan kohdasta "Poista projekti". Projektin nimi kirjoitetaan tekstikenttään, ja painetaan "Poista projekti". Projektin hallintapalkki katoaa, ja tiedot poistetaan tietokannasta.