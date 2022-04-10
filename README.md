# Project Timer

Sovelluksen avulla voit helposti pitää kirjaa eri projekteihin tai kursseihin käyttämääsi aikaa. Kirjattuja työaikoja pystyy tarkastelemaan statistiikkojen sekä kuvaajien muodossa.

## Python-versiosta

Testit suoritettu python-versioilla `3.8.3` sekä `3.10.4`. Varsinkin vanhempien python-versioiden kanssa sovellus voi toimia virheellisesti, tai olla toimimatta lainkaan.

## Dokumentaatio

[tuntikirjanpito.md](https://github.com/Capslock01/ot-harjoitustyo/blob/master/dokumentaatio/tuntikirjanpito.md)

[vaativuusmaarittely.md](https://github.com/Capslock01/ot-harjoitustyo/blob/master/dokumentaatio/vaatimusmaarittely.md)

[changelog.md](https://github.com/Capslock01/ot-harjoitustyo/blob/master/dokumentaatio/changelog.md)

## Asennus

1. Asenna vaadittavat moduulit:
```
poetry install
```
2. Alusta sovellus:
```
ei implementoitu
```
3. Käynnistä sovellus:
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
poetry run invoke pylint-test
```