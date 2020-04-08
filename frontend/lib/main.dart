import 'package:FrontendPrototype/pages/HomePage.dart';
import 'package:FrontendPrototype/pages/MapPage.dart';
import 'package:FrontendPrototype/pages/MarkerDetailPage.dart';
import 'package:flutter/material.dart';

import 'package:google_maps/google_maps.dart';
import 'model/location.dart';
import 'model/storage.dart' as storage;

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  // This widget is the root of the application. Define theme, routes, ... here.
  @override
  Widget build(BuildContext context) {
    Location l = Location('1', 'Mathildenhöhe', new LatLng(49.876571, 8.667285), 'Die Darmstädter Künstlerkolonie war einerseits eine größtenteils mäzenatisch finanzierte Gruppe von Künstlern, die zwischen 1899 und 1914 – idealerweise bei übereinstimmenden künstlerischen Anschauungen – gemeinsam tätig waren. Andererseits bezeichnet der Begriff auch die Wirkungsstätte und die von den Künstlern errichteten Bauten auf der Mathildenhöhe in Darmstadt, in denen diese lebten und arbeiteten. Für das Ensemble der Künstlerkolonie Mathildenhöhe wird die Anerkennung als UNESCO-Welterbe angestrebt.','Die Darmstädter Künstlerkolonie war einerseits eine größtenteils mäzenatisch finanzierte Gruppe von Künstlern, die zwischen 1899 und 1914 – idealerweise bei übereinstimmenden künstlerischen Anschauungen – gemeinsam tätig waren. Andererseits bezeichnet der Begriff auch die Wirkungsstätte und die von den Künstlern errichteten Bauten auf der Mathildenhöhe in Darmstadt, in denen diese lebten und arbeiteten. Für das Ensemble der Künstlerkolonie Mathildenhöhe wird die Anerkennung als UNESCO-Welterbe angestrebt.');
    l.addImage('https://www.mathildenhoehe.eu/assets/HomePageImages/startseite-achim-mende-mathildenhoehe-hd.jpg');
    l.addImage('https://www.mathildenhoehe.eu/assets/HomePageImages/startseite-achim-mende-russ-kapelle-hd.jpg');
    l.addImage('https://www.mathildenhoehe.eu/assets/HomePageImages/startseite-illumination-ruediger-dunker-hd.jpg');
    l.addImage('https://www.mathildenhoehe.eu/assets/HomePageImages/startseite-hochzeitsturm-hd.jpg');
    l.addImage('https://www.mathildenhoehe.eu/assets/HomePageImages/startseite-portal-museum-kuenstlerkolonie.jpg');
    l.addImage('https://www.mathildenhoehe.eu/assets/Galerie/mathildenhoehe/_resampled/SetHeight600-fmd487198ingoefischer-kl-.jpg');

    storage.locations.add(l);
    return MaterialApp(
      title: 'Digitale Spurensuche',
      theme: ThemeData(
        primarySwatch: Colors.red,
      ),
      routes: <String, WidgetBuilder>{
        // Every page should contain a static const string called route containing its route.
        HomePage.route: (context) => HomePage(),
        MapPage.route: (context) => MapPage(),
        //MarkerDetailPage.route: (context) => MarkerDetailPage(),
      }
    );
  }
}