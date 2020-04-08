import 'package:FrontendPrototype/commonWidgets/DssMap.dart';
import 'package:FrontendPrototype/commonWidgets/Images.dart';
import 'package:FrontendPrototype/commonWidgets/PicturesPreview.dart';
import 'package:FrontendPrototype/commonWidgets/VideoPlayerScreen.dart';
import 'package:FrontendPrototype/model/location.dart';
import 'package:flutter/material.dart';

class MarkerDetailPage extends StatelessWidget {
  static const String route = "/markerDetail";

  Location loc;

  MarkerDetailPage(this.loc);

  @override
  Widget build(BuildContext context) {
    var pheight = MediaQuery.of(context).size.height;

    return Column(
      children: <Widget>[
        Text(loc.name,
            style: TextStyle(fontSize: 30, fontWeight: FontWeight.w300)),
        SizedBox(height: 10),
        Text(loc.text,
            style: TextStyle(fontSize: 14, fontWeight: FontWeight.w100)),
        SizedBox(height: 30),
        Expanded(
            child: ListView(
          scrollDirection: Axis.horizontal,
          children: <Widget>[
            FlatButton(
              onPressed: () {
                Navigator.push(context, MaterialPageRoute(builder: (context) {
                  return Images(loc);
                }));
              },
              padding: EdgeInsets.all(0),
              child: Card(
                child: PicturesPreview(loc),
              ),
            ),

            Card(
                child: Column(
              children: <Widget>[
                Center(
                  child: Text(
                    'Videos',
                    style: TextStyle(fontSize: 25, fontWeight: FontWeight.w200),
                  ),
                ),
                Expanded(
                  child:  Stack(
                    alignment: AlignmentDirectional.center,
                    children: <Widget>[
                      Image.asset('assets/img/preview.jpg'),
                      FloatingActionButton(
                        onPressed: () {
                          Navigator.push(context,
                              MaterialPageRoute(builder: (context) {
                                return VideoPlayerScreen();
                              }));
                        },
                        child: Icon(Icons.play_arrow),
                      )
                    ],
                  ),
                )

              ],
            )),

            Container(
              width: 600,
              child: Card(
                  child: Column(
                    children: <Widget>[
                      Center(
                        child: Text(
                          'Texte',
                          style: TextStyle(fontSize: 25, fontWeight: FontWeight.w200),
                        ),
                      ),
                      Text('Weit hinten, hinter den Wortbergen, fern der Länder Vokalien und Konsonantien leben die Blindtexte. Abgeschieden wohnen sie in Buchstabhausen an der Küste des Semantik, eines großen Sprachozeans. Ein kleines Bächlein namens Duden fließt durch ihren Ort und versorgt sie mit den nötigen Regelialien. Es ist ein paradiesmatisches Land, in dem einem gebratene Satzteile in den Mund fliegen. Nicht einmal von der allmächtigen Interpunktion werden die Blindtexte beherrscht – ein geradezu unorthographisches Leben. Eines Tages aber beschloß eine kleine Zeile Blindtext, ihr Name war Lorem Ipsum, hinaus zu gehen in die weite Grammatik. Der große Oxmox riet ihr davon ab, da es dort wimmele von bösen Kommata, wilden Fragezeichen und hinterhältigen Semikoli, doch das Blindtextchen ließ sich nicht beirren. Es packte seine sieben Versalien, schob sich sein Initial in den Gürtel und machte sich auf den Weg. Als es die ersten Hügel des Kursivgebirges erklommen hatte, warf es einen letzten Blick zurück auf die Skyline seiner Heimatstadt Buchstabhausen, die Headline von Alphabetdorf und die Subline seiner eigenen Straße, der Zeilengasse. Wehmütig lief ihm eine rhetorische Frage über die Wange, dann setzte es seinen Weg fort. Unterwegs traf es eine Copy. Die Copy warnte das Blindtextchen, da, wo sie herkäme wäre sie')
                    ],
                  )),
            )

          ],
        )),

        /*Expanded(
              child: ListView.builder(
                padding: EdgeInsets.fromLTRB(0, 30, 0, 30),
                scrollDirection: Axis.horizontal,
                itemCount: loc.images.length,
                itemBuilder: (context, index) {
                  return Padding(
                    padding: EdgeInsets.all(8),
                    child: Image(
                      image: NetworkImage(loc.images[index]),
                      fit: BoxFit.contain,
                    ),
                  );
                },
              ),
            ),*/

        /*child: GridView.builder(
                            itemCount: loc.images.length,
                            scrollDirection: Axis.horizontal,
                            gridDelegate: SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 1),
                            itemBuilder: (context, index){
                              return Image(image: NetworkImage(loc.images[index]),);
                        }),*/
      ],
    );
  }
}
