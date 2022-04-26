# Arkkitehtuurikuvaus

## Luokkakaavio

```mermaid
classDiagram
    GUI <-- MainView
    GUI <-- Statistics
    ProjectController --> MainView
    MainView <-- ProjectService
    ProjectService <-- ProjectRepository
    ProjectRepository <-- Project
    ProjectService <-- Projects
    ProjectService <-- ProjectData
    Project <-- Timer
    class GUI{
    }
    class MainView{
    }
    class ProjectController{
    }
    class Statistics{
    }
    class ProjectService{
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