import 'dart:ui';

import 'package:flutter/cupertino.dart';
import 'package:google_maps/google_maps.dart';

class Location{
  final String id;
  final String name;
  final LatLng latLng;
  String spoiler;
  String text;
  List<String> images = new List();

  Location(this.id,this.name, this.latLng, this.spoiler, this.text);
  
  void addImage(String url){
    images.add(url);
  }



}