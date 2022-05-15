# Arkkitehtuurikuvaus

## Rakenne

Sovellus on jaettu viiteen hakemistoon, joista entities ja repos kuuluvat sovellusjogiikan kerrokseen. Database hakemisto sisältää pysyväistalletukseen tarvittavat itse tietokannan käyttöön liittyvät luokat. Gui hakemistossa on käyttöliittymän toteutus.

## Käyttöliittymä

Sovelluksessa on toistaiseksi vain yksi näkymä. Vasemmalla puolella ovat päällekkäin eri projektit, jotka on haettu tietokannasta. Jokaisella projektilla on ajastimenhallintanapit. Oikealla puolella on uuden projektin lisäämiseen tarvittavat toiminnot.

## Luokkakaavio

```mermaid
classDiagram
    GUI <-- MainView
    ProjectController --> MainView
    MainView <-- ProjectRepository
    ProjectRepository <-- Project
    ProjectRepository <-- Projects
    Project <-- ProjectData
    ProjectRepository <-- ProjectData
    Project <-- Timer
    class GUI{
    }
    class MainView{
    }
    class ProjectController{
    }
    class ProjectRepository{
    }
    class Project{
    }
    class Timer{
    }
    class Projects{
    }
    class ProjectData{
    }
```
Käyttöliittymästä vastaa GUI luokka. Tämä käyttää päänäkymän luovaa MainView-luokkaa. Rakenne mahdollistaa useamman näkymän tekemisen, mutta vain yksi on käytössä. Projektien hallintapalkit ovat oma luokkansa, jota vain MainView käyttää.
ProjectRepository on luokka, joka hoitaa tietokantatallennuksen hallitsemisesta, ja hoitaa tiedon säilytyksen ajon aikana. Ohjelman ajon aikana projektit tallennetaan Project-olioina, joille jokaiselle on luotu oma Timer-olio.
Tietokannan käyttöön ProjectRepository käyttää kahta taulua, jotka on tehty SQLalchemya käyttäen Projects- ja ProjectData luokkina. Projects-tauluun tallennetaan vain projektit. ProjectData-tauluun tallennetaan mitatut ajat, joissa viitataan Projects-taulun id-avaimeen.

## Sekvenssikaavio

Projektin luominen, ajastaminen ja tiedon tallentaminen
```mermaid
sequenceDiagram
    participant käyttäjä
    participant index.py
    participant GUI
    participant ProjectRepo
    participant MainView
    participant Project
    participant Timer
    participant Projects
    participant ProjectData
    participant ProjectController
    index.py ->> GUI: GUI.start()
    GUI ->> MainView: init MainView
    MainView ->> ProjectRepo: get_projects()
    ProjectRepo ->> Projects: select(Projects) [tyhjä]
    käyttäjä ->> MainView: _create_project('ohte')
    MainView ->> ProjectRepo: add_project('ohte')
    ProjectRepo ->> Projects: session.add_all([Projects(name = 'ohte')])
    ProjectRepo ->> Project: self._projects.append(Project('ohte', 1))
    ProjectRepo -->> MainView: True [luonti onnistui]
    MainView ->> ProjectController: ProjectController(self._left_frame, project) [project on aiemmin luotu Project olio]
    käyttäjä ->> ProjectController: self._play()
    ProjectController ->> Timer: self._project.timer.start()
    käyttäjä ->> ProjectController: self._stop()
    ProjectController ->> Project: self._project.save()
    Project ->> Timer: self.timer.stop()
    Timer -->> Project: 20 [sekuntia]
    Project ->> ProjectData: ProjectData(project_id = self.id_, time = time, date = datetime.today())
    käyttäjä ->> MainView: _get_statistics(self._right_frame, '') [tyhjä merkkijono hakee kaiken datan]
    MainView ->> ProjectRepository: get_stats('')
    ProjectRepository ->> ProjectData: select(func.sum(ProjectData.time)).where()ProjectData.project_id == project.id_, ProjectData.date.startswith(timestr))
    ProjectData -->> ProjectRepository: 20
    ProjectRepository -->> MainView: '' Projektien kokonaisajat kaikista\n tallennetuista ajoista:\n\n ohte '00:00:20'
```
index.py tiedoston ajaminen käynnistää sovelluksen. Index käynnistää GUI:n, joka käynnistää päänäkymän. Päänäkymä pyytää ProjectReposta tallennetut projektit. ProjectRepo hakee kaikki tietokannassa olevat projektit, ja tallentaa niistä Project-oliot listaan.
Kun käyttäjä luo uuden projektin, ProjectRepo tarkastaa, onko projektin nimi validi, ja luo uuden projektin. MainView luo uudelle projektille ProjectController-olion projektin hallintaan käyttöliittymällä. Kun ProjectControllerista painaa play-nappia, käynnistetään kyseisen projektin Timer.
Stop-nappi ajaa Timerin stop-metodin. ProjectRepo tallentaa mitatun ajan tietokantaan. Nyt projektidatan hakeminen tyhjällä haulla hakee koko historian tallennetuista ajoista. Statistiikoissa näytetään jokaisen ikinä luodun projektin kokonaisajan.
