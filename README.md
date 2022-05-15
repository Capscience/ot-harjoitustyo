# Project Timer

Sovelluksen avulla voit helposti pitää kirjaa eri projekteihin tai kursseihin käyttämääsi aikaa. Kirjattuja työaikoja pystyy tarkastelemaan statistiikkojen sekä kuvaajien muodossa.

## Release

Viimeisin:

[Loppupalautus](https://github.com/Capslock01/ot-harjoitustyo/releases/tag/viikko7)

Aiemmat versiot:

[versio 1.1](https://github.com/Capslock01/ot-harjoitustyo/releases/tag/viikko6)

[versio 1.0](https://github.com/Capslock01/ot-harjoitustyo/releases/tag/viikko5)

## Python-versiosta

Testit suoritettu python-versiolla `3.8.3`. Varsinkin vanhempien python-versioiden kanssa sovellus voi toimia virheellisesti, tai olla toimimatta lainkaan.

## Dokumentaatio

[kayttoohjeet.md](/dokumentaatio/kayttoohjeet.md)

[tuntikirjanpito.md](/dokumentaatio/tuntikirjanpito.md)

[vaativuusmaarittely.md](/dokumentaatio/vaatimusmaarittely.md)

[changelog.md](/dokumentaatio/changelog.md)

[arkkitehtuuri.md](/dokumentaatio/arkkitehtuuri.md)

## Asennus

1. Asenna vaadittavat moduulit:
```
poetry install
```
2. Käynnistä sovellus:
```
poetry run invoke start
```

## Invoke-komennot

Sovelluksen voi käynnistää komennolla:
```
poetry run invoke start
```

Unittestit voi ajaa komennolla:
```
poetry run invoke test
```

Testien kattavuusraportin voi luoda komennolla:
```
poetry run invoke coverage-report
```

Pylint-testin voi ajaa komennolla:
```
poetry run invoke lint
```

Tietokannan voi nollata (poistaa) komennolla:
```
poetry run invoke reset
```
