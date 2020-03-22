import 'package:FrontendPrototype/model/location.dart';
import 'package:flutter/material.dart';

class Images extends StatelessWidget{
  
  Location loc;
  
  Images(this.loc);
  
  @override
  Widget build(BuildContext context) {
    // TODO: implement build
    return Scaffold(
        appBar: AppBar(
          title: Text(loc.name + ' Bilder'),
        ),
        body: GridView.builder(gridDelegate: new SliverGridDelegateWithFixedCrossAxisCount(crossAxisCount: 3),
            itemCount: loc.images.length,
            itemBuilder: (BuildContext context, int index){
          return GestureDetector(
            onTap: (){
              Navigator.push(context, MaterialPageRoute(builder: (context) {

                return Scaffold(
                    appBar: AppBar(
                      title: Text('Bilder'),
                    ),
                    body: Center(
                      child: Image(
                        image: NetworkImage(loc.images[index]),
                      ),
                    )
                );
              }));
            },
            child: Image(
              image: NetworkImage(loc.images[index]),
              fit: BoxFit.fitHeight,
            ),
          );
            })
    );
  }
  
}