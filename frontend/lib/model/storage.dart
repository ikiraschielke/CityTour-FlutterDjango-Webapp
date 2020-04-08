library storage;

import 'package:flutter/material.dart';

import 'location.dart';
import 'package:google_maps/google_maps.dart' hide Icon;

List<Location> locations = new List();
List<Marker> markers = new List();
//Map<Marker,Location> markerToLocation = <Marker,Location>{};