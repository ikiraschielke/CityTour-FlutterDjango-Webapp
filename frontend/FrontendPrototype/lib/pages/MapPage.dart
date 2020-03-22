import 'package:FrontendPrototype/commonWidgets/DssDrawer.dart';
import 'package:FrontendPrototype/commonWidgets/DssMap.dart';
import 'package:flutter/material.dart';

/* Map's Page
  ======================================
  Page displays a fullscreen Map with markers.
*/
class MapPage extends StatefulWidget {
  static const String route = "/map";

  @override
  _MapPageState createState() => _MapPageState();
}

class _MapPageState extends State<MapPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Digitale Spurensuche"),
      ),
      drawer: DssDrawer(),
      body: Hero(
        tag: "map",
        child: DssMap(),
      )
    );
  }
}
