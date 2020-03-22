import 'package:FrontendPrototype/pages/HomePage.dart';
import 'package:FrontendPrototype/pages/MapPage.dart';
import 'package:flutter/material.dart';

/* Default-Drawer to use on Scaffolds
  ======================================
  This Widget can be used in any Scaffold to have a common drawer across the app.
  TODO: highlight selected item
*/
class DssDrawer extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Drawer(
      child: ListView(
        padding: EdgeInsets.zero,
        children: <Widget>[
          DrawerHeader(
            child: Center( child: Text('Digitale Spurensuche') ),
            decoration: BoxDecoration(
              color: Theme.of(context).primaryColor,
            ),
          ),
          ListTile(
            title: Text("Startseite"),
            subtitle: Text("Startseite der Anwendung"),
            leading: Icon(Icons.apps),
            onTap: () { Navigator.pushReplacementNamed(context, HomePage.route); },
          ),
          ListTile(
            title: Text("Karte"),
            subtitle: Text("Gehen Sie auf die digitale Spurensuche"),
            leading: Icon(Icons.map),
            onTap: () { Navigator.pushReplacementNamed(context, MapPage.route); },
          ),
          ListTile(
            title: Text("Anmelden"),
            subtitle: Text("Melden Sie sich an"),
            leading: Icon(Icons.lock),
            onTap: () {},
          ),
          ListTile(
            title: Text("Impressum"),
            subtitle: Text("Rechtliche Hinweise"),
            leading: Icon(Icons.receipt),
            onTap: () {},
          ),
          ListTile(
            title: Text("Datenschutz"),
            subtitle: Text("Hinweise zum Datenschutz"),
            leading: Icon(Icons.warning),
            onTap: () {},
          ),
        ],
      ),
    );
  }
}