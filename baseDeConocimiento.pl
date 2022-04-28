%juegos(nombre,genero,duracion,categoriaSpeed,decada)
%generos(genero,experiencia)
%adicional(genero,extra,nombreJuego)

%######################## Decada de los 90 #########################################################

%GENERO: PLATAFORMA
juegos('Super mario world', 'Plataforma', 'Media', '96exit', 90, 'Habil').
juegos('Sonic the hedgehog', 'Plataforma', 'Corta', 'beat the game', 90, 'Habil').
juegos('Super metroid', 'Plataforma', 'Media', 'any%', 90, 'Habil').

%GENERO: FPS
juegos('Ultimate doom', 'FPS', 'Corta', 'knee deep in the dead', 90, 'Experto').
juegos('Wolfenstein', 'FPS', 'Larga', 'Episode1: escape from wolfenstein', 90, 'Experto').
juegos('Half-life', 'FPS', 'Corta', 'Won', 90, 'Habil').

%GENERO: ARCADE
juegos('Street fighter II-the world warrior', 'Arcade', 'Corta', 'Normal', 90, 'Inexperto').
juegos('Mortal kombat', 'Arcade', 'Corta', 'Arcade', 90, 'Inexperto').
juegos('Metal slug', 'Arcade', 'Corta', 'Medium', 90, 'Habil').


%######################## Decada de los 2000 ##########################################################

%GENERO: CARRERAS
juegos('Forza Moto Sport','Carreras','Corta','individualLevels', 2000,'Inexperto').
juegos('Grand Turismo 4','Carreras','Larga','any%',2000, 'Inexperto').
juegos('Need For Speed Carbon','Carreras','Larga','any%',2000, 'Habil'). 

%GENERO: DEPORTES
juegos('Tony hawks pro skater 4','Deportes','Media','any%',2000, 'Habil').
juegos('Fifa2006','Deportes','Corto','career mode-season%',2000, 'Inexperto').
juegos('Winnig eleven: pro evolution soccer 2007','Deportes','Corto','any cup title in the shortest possible any%', 2000, 'Inexperto').

%GENERO: ACCION-AVENTURA
juegos('Zelda Majoras Mask','Accion-Avetura','Medio','any%',2000, 'Habil').
juegos('God Of War II','Accion-Avetura','Medio','anyng%',2000, 'Habil').
juegos('Resident Evil 4 (Console)' ,'Accion-Avetura','Largo','NewGame',2000, 'Habil').


%############################################# Decada de los 2010 ######################################

%GENERO: RPG
juegos('Sekiro shadow of the die twice','RPG','Corta','shura',2010,'Experto').
juegos('Dark souls','RPG','Corta','any%',2010,'Experto').
juegos('Bloodborne' ,'RPG','Corta' ,'any%',2010,'Experto').

%GENERO: PELICULA INTERACTIVA
juegos('Beyone two soul','Pelicula interactiva', 'Larga', 'any%', 2010, 'Inexperto').
juegos('Until dawn','Pelicula interactiva', 'Larga', 'any%', 2010, 'Habil').
juegos('Detroid become human','Pelicula interactiva', 'largo' , 'any%', 2010, 'Inexperto').

%GENERO: MUSICA
juegos('Just dance 2018','Musica', 'Larga' ,'5stars%',2010,'Inexperto').
juegos('Guitar hero warrios of rock','Musica', 'Larga', 'quest mode any% co-op',2010,'Habil').
juegos('Rock band 4','Musica', 'Larga' , 'full game full combo',2010,'Habil').


%################################ Decada de los 2020 ######################################################

%GENERO: FPS
juegos('Doom eternal', 'FPS', 'Corta', 'any%', 2020, 'Habil').
juegos('Call of duty cold war', 'FPS', 'Media','any%', 2020, 'Inexperto').
juegos('Far cry 6','FPS', 'Media','any%', 2020, 'Habil').

%GENERO: RPG
juegos('Mortal shell', 'RPG', 'Corta','any%', 2020, 'Experto').
juegos('Elden ring', 'RPG', 'Corta', 'any%', 2020, 'Experto').
juegos('Persona 5 royal', 'RPG', 'Larga','hard,true ending', 2020, 'Experto').

%GENERO: DEPORTES
juegos('Nba 2k22', 'Deportes', 'Corta','play now', 2020, 'Inexperto').
juegos('Fifa 2020', 'Deportes', 'Corta', 'champions league', 2020, 'Inexperto').
juegos('Mario golf super rush', 'Deportes', 'Media','all courses', 2020, 'Inexperto').

%###################### Generos ##########################################################################
generos('Plataforma', 'Inexperto').
generos('FPS', 'Experto').
generos('Arcade', 'Habil').
generos('Carreras', 'Habil').
generos('Deportes', 'Inexperto').
generos('Accion-Avetura', 'Habil').
generos('RPG', 'Experto').
generos('Pelicula interactiva', 'Inexperto').
generos('Musica', 'Inexperto').

%############################################# Adicionales ###############################################
adicional('Plataforma', '2D').
adicional('FPS', 'Precisión').
adicional('Carreras', 'Simulación').
adicional('Deportes', 'Competitivo').
adicional('Accion-Aventura', 'Exploración').
adicional('RPG', 'Ingenio').
adicional('Pelicula interactiva', 'Toma de decisiones').
adicional('Musica', 'Reflejos').
