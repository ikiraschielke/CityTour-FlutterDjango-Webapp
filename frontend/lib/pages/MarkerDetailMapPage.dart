import 'package:FrontendPrototype/commonWidgets/DssMap.dart';
import 'package:FrontendPrototype/model/location.dart';
import 'package:FrontendPrototype/pages/MarkerDetailPage.dart';
import 'package:flutter/material.dart';

class MarkerDetailMapPage extends StatelessWidget {
  //static const String route = "/markerDetail";

  Location loc;

  MarkerDetailMapPage(this.loc);

  @override
  Widget build(BuildContext context) {

    return Scaffold(
        appBar: AppBar(
          title: Text(loc.name),
        ),
        body: Column(
          children: <Widget>[
            Expanded(
                flex: 1,
                child: Hero(
                  tag: "map",
                  child: DssMap(),
                )
            ),
            SizedBox(height: 30,),
            Expanded(
                flex: 2,
                child: Container(
                  padding: EdgeInsets.fromLTRB(30, 00, 30, 30),
                  child: MarkerDetailPage(loc)
                )
            )
          ],
        )
    );
  }
}