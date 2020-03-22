# FrontendPrototype

A prototyped frontend for the project.

## Getting Started

This project uses flutter. To run this project you need to use the latest beta branch of flutter with web enabled.


## Project structure
The `main.dart` is start of the application. Declare theme and routes here.
### Pages
Pages are standalone widgets that provide a complete site on their own. All pages are organized inside the `lib/pages` folder. Those files should end with `Page.dart`.
Each page should contain `static const string route = "...";` with it's route declared. These route can be easily accessed from other classes later on.

### Widgets
Widgets are components of eg. Pages showing one action or task. For example the app shares one Drawer on each Page. This Drawer is defined at `lib/commonWidgets`. All components with potential multipurpose use should be defined here. If you need to define a widget for only one specific Page, pace this widget inside the `lib/pages/widgets`.