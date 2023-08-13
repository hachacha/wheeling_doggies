# wheeling doggies

this is all made very specifically for the wheeling dog race [program guide](http://www.trackinfo.com/trakdocs/?trackcode=gsn$) (click dropdown and then the program guide there.) that is released every day there are races. 
the goal is to take the table that is presented as pdf and turn it into a database that can be queried to figure out the probability for any race for a winner or odds for that based on attributes of the dogs.

pdfs are annoying as hell and nothing makes sense but these are made consistently the same way so it should be tedious but once it's done it should work until they change something. 
i am hoping to do this in order to also better understand how pdfs works and be good at extracting textual data from them to assess larger data sets. 
and also make some money off the dog races.

### notes for me for now

- understanding the program fields https://www.amwager.com/blog/how-to-read-greyhound-racing-program/
- the dog names are in images so you gotta save the images, then use tesseract to ocr the names out of the images in order to turn them into text.
- 


```
dog
    - name
    - weight
        -weight history function
    - kennel
    - trainer
    - parentA
    - parentB
    - birthday
        -age function
    - breeder
    - best time
        -best time history

race
    - date
    - track
    - track conditions
    - time (morning, evening)
    - time of winner
    - distance
    - race grade

performance
    - fk race
    - fk dog
    - starting position
    - break position
    - eigth mile position
    - far turn position
    - finish position
    - lengths lost by
    - time (actual running time - ART)
    - speed figure
    - weight when started
    - odds to $1
    - 

 ```