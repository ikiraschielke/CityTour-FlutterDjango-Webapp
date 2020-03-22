import 'package:flutter/material.dart';
import 'package:FrontendPrototype/model/location.dart';

class PicturesPreview extends StatelessWidget {
  Location loc;

  PicturesPreview(this.loc);

  @override
  Widget build(BuildContext context) {
    return Column(
      children: <Widget>[
        Center(child: Text('Bilder', style: TextStyle(fontSize: 25, fontWeight: FontWeight.w200),),),
        Expanded(
          child: Align(
            alignment: Alignment.bottomCenter,
            child: Row(
              children: <Widget>[
                Image(
                    image: NetworkImage(loc.images[0]),
                    fit: BoxFit.contain,
                  ),

             Image(
                    image: NetworkImage(loc.images[1]),
                    fit: BoxFit.contain,
                  ),

              ],
            ),
    )
        ),
        Expanded(
          child: Align(
            alignment: Alignment.topCenter,
            child: Row(
              children: <Widget>[
                Image(
                  image: NetworkImage(loc.images[2]),
                  fit: BoxFit.contain,
                ),

                Image(
                  image: NetworkImage(loc.images[3]),
                  fit: BoxFit.contain,
                ),

              ],
            ),
          ),
        )


      ],
    );
  }
}
