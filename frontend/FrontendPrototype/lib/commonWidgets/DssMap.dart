import 'package:FrontendPrototype/commonWidgets/VideoPlayerScreen.dart';
import 'package:FrontendPrototype/pages/MarkerDetailPage.dart';
import 'package:FrontendPrototype/pages/MarkerDetailMapPage.dart';
import 'package:flutter/material.dart';
import 'package:google_maps/google_maps.dart' hide Icon;

import 'dart:html';
import 'dart:ui' as ui;

import '../model/storage.dart' as storage;

/* Widget displaying Google Maps
  ======================================
  This Widget is a Map showing Markers to visit.
  TODO: Show Marker depening on REST Api
*/

class DssMap extends StatelessWidget {

  @override
  Widget build(BuildContext context) {
    return getMap(context);
  }

  Widget getMap(BuildContext context) {
    String htmlId = "7";


    // ignore: undefined_prefixed_name
    ui.platformViewRegistry.registerViewFactory(htmlId, (int viewId) {

      // not yet gps tracked position
      final myLatlng = new LatLng(49.8716584, 8.6475092);

      // common map settings. Using these settings results in showing Darmstadt in fullscreen
      final mapOptions = new MapOptions()
        ..zoom = 14
        ..center = LatLng(49.8716584, 8.6475092);

      // define html element to be rendered
      final elem = DivElement()
        ..id = htmlId
        ..style.width = "100%"
        ..style.height = "100%"
        ..style.border = 'none';
      final map = new GMap(elem, mapOptions);

      storage.locations.forEach((element) {
        Marker m = Marker(MarkerOptions()
          ..position = element.latLng
          ..map = map
          ..clickable = true
          ..icon = Icon(Icons.alarm)
          ..title = element.name);

        m.onClick.listen((mouseEvent) {
          Navigator.push(context, MaterialPageRoute(builder: (context) {
            return MarkerDetailMapPage(element);
          }));
        });
      });



      return elem;
    });

    return HtmlElementView(viewType: htmlId);
  }
}