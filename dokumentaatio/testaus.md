# Testausdokumentti

Ohjelman testaus on suoritettu niin käytännössä kuin automaattisilla unit- ja integraatiotesteillä.

## Unit- ja integraatiotestaus

### ProjectRepo

`ProjectRepo`-luokan testit tehdään luokalla [TestProjectRepo](/src/tests/repo_test.py). Testit poistavat tietokannasta kaiken mitä sinne tallentavat.

### Entity-luokat

`Project`-luokkaa testataan testiluokalla [TestProject](/src/tests/project_test.py). Samalla testataan nopeasti myös `Timer`-luokkaa. Tämän testaus tapahtuu kuitenkin pääasiassa luokalla [TestTimer](/src/tests/timer_test.py). Testit kestävät muutaman sekunnin, sillä timerista täytyy testata, että se mittaa ajat oikein.

### Testikattavuus

Ohjelman haarautumakattavuus poislukien käyttöliittymä on 76%.

![](/dokumentaatio/coverage.png)

## Järjestelmätestaus

### Asennus

Sovellus on asennettu Linux-ympäristöön kahdella eri koneella ja eri Linux-distribuutiolla. Tässä on noudatettu [käyttöohjetta](/dokumentaatio/kayttoohjeet.md).

### Toiminnallisuus

[Määrittelydokumenttiin](/dokumentaatio/vaatimusmaarittely.md) valmiiksi merkityt ominaisuudet on testattu käyttöohjeen mukaisesti oikeilla sekä virheellisillä syötteillä.

# Sovellukseen jääneet laatuongelmat

- Sovellus ei ilmaise täysin selvästi, jos uutta projektia luodessa projekti on olemassa inaktiivisessa tilassa, jolloin sovellus ei luo uutta projektia, vaan aktivoi inaktiivisen projektin.