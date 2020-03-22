import 'package:FrontendPrototype/commonWidgets/DssDrawer.dart';
import 'package:flutter/material.dart';

import 'MapPage.dart';

/* Starting Page
  ======================================
  Simple Start Page with fullscreen Menu.
  TODO: Connect Buttons to routes
*/
class HomePage extends StatelessWidget {
  static const String route = "/";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Digitale Spurensuche"),
      ),
      drawer: DssDrawer(),
      body: Column(
        children: <Widget>[
          _fullScreenMenuEntry(AssetImage('assets/img/markers.jpg'), "Wegpunkt", () { Navigator.pushReplacementNamed(context, MapPage.route); }),
          _fullScreenMenuEntry(AssetImage('assets/img/map.jpg'), "Routen", () {})
        ],
      ),
    );
  }
}

// Menu item widget filling fullScreenMenu widget
Widget _fullScreenMenuEntry (ImageProvider image, String text, Function clickCallback) {
  return Expanded(
    flex: 1,
    child: Stack(
      children: <Widget>[
        Container(
          decoration: BoxDecoration(
            image: DecorationImage(
              image: image,
              fit: BoxFit.cover
            )
          ),
        ),
        Positioned.fill(
          child: Material(
            color: Colors.transparent,
            child: InkWell(
              onTap: () { clickCallback(); },
              hoverColor: Colors.white30,
              child: Center(
                child: Text(text, 
                  style: TextStyle(
                    color: Colors.white, 
                    fontSize: 150, 
                    shadows: <Shadow>[
                      Shadow(
                        offset: Offset(10.0, 10.0),
                        blurRadius: 10.0,
                        color: Color.fromARGB(180, 0, 0, 0),
                      ),
                    ]
                  ),
                ),
              ),
            ),
          ),
        ), 
      ],
    ) 
  );
}