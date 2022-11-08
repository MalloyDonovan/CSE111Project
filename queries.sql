DROP TABLE gameData;
DROP TABLE Games;
DROP TABLE indieDevs;
DROP TABLE ps4Sales;
DROP TABLE gameSales;
DROP TABLE gameDevs;
DROP TABLE windowsGames;
DROP TABLE xboxSales;

--CREATE TABLES

CREATE TABLE gameData(
    gd_name VARCHAR(32) not null,
    gd_platform VARCHAR(32) not null,
    gd_date DATE not null,
    gd_score DECIMAL(4,0) not null,
    gd_uscore DECIMAL(4,0) not null,
    gd_developer VARCHAR(32) not null,
    gd_genre VARCHAR(32) not null,
    gd_players VARCHAR(32) not null,
    gd_critics DECIMAL(4,0)not null,
    gd_users DECIMAL(4,0) not null
);

CREATE TABLE Games(
    g_id DECIMAL(5,0) not null,
    g_title VARCHAR(32) not null,
    g_mainStory DECIMAL(4,0) not null,
    g_mainPlus DECIMAL(4,0) not null,
    g_completionist DECIMAL(4,0) not null,
    g_allStyles DECIMAL(4,0) not null,
    g_coop VARCHAR(32) not null,
    g_versus VARCHAR(32) not null,
    g_type VARCHAR(32) not null,
    g_developers VARCHAR(32) not null,
    g_publishers VARCHAR(32) not null,
    g_platforms VARCHAR(32) not null,
    g_genres VARCHAR(32) not null,
    g_releaseNA DATE not null,
    g_releaseEU DATE not null,
    g_releaseJP DATE not null
);

CREATE TABLE indieDevs(
    ind_developer VARCHAR(32) not null,
    ind_city VARCHAR(32) not null,
    ind_autonomous_area VARCHAR(32) not null,
    ind_country VARCHAR(32) not null,
    ind_notable VARCHAR(64) not null,
    ind_notes VARCHAR(128) not null
);

CREATE TABLE gameSales(
    gs_name VARCHAR(32) not null,
    gs_platform VARCHAR(32) null,
    gs_release_year INTEGER(4) null,
    gs_genre VARCHAR(32) null,
    gs_publisher VARCHAR(32) null,
    gs_NA_sales DECIMAL(5,0) null,
    gs_EU_sales DECIMAL(5,0) null,
    gs_JP_sales DECIMAL(5,0) null,
    gs_other_sales DECIMAL(5,0) null,
    gs_global_sales DECIMAL(5,0) null,
    gs_critic_score DECIMAL(5,0) null,
    gs_critic_count INTEGER(8) null,
    gs_user_score DECIMAL(5,0) null,
    gs_user_count INTEGER(8) null,
    gs_developer VARCHAR(32) null,
    gs_rating VARCHAR(4) null
);

CREATE TABLE gameDevs(
    gdev_developer VARCHAR(32) not null,
    gdev_city VARCHAR(32) not null,
    gdev_administrative_division VARCHAR(32) null,
    gdev_country VARCHAR(32) null,
    gdev_est INTEGER(4) null,
    gdev_notable VARCHAR(32) null,
    --CONTAINS NULL VALUES
    gdev_notes VARCHAR(64) null
);

CREATE TABLE windowsGames(
    wg_titles VARCHAR(32) not null,
    wg_released INTEGER(4) not null,
    wg_developer VARCHAR(32) not null,
    wg_publisher VARCHAR(32) not null,
    wg_genre VARCHAR(32) not null
);


CREATE TABLE xboxSales(
    xbox_pos INTEGER(3) not null,
    xbox_game VARCHAR(32) not null,
    xbox_year INTEGER(4) not null,
    xbox_genre VARCHAR(32) not null,
    xbox_publisher VARCHAR(32) not null,
    xbox_NA DECIMAL(5,0) not null,
    xbox_EU DECIMAL(5,0) not null,
    xbox_JP DECIMAL(5,0) not null,
    xbox_rest_world DECIMAL(5,0) not null,
    xbox_global DECIMAL(5,0) not null
);

CREATE TABLE ps4Sales(
    ps4_game VARCHAR(32) not null,
    ps4_year INTEGER(4) not null,
    ps4_genre VARCHAR(32) not null,
    ps4_publisher VARCHAR(32) not null,
    ps4_NA DECIMAL(5,0) not null,
    ps4_EU DECIMAL(5,0) not null,
    ps4_JP DECIMAL(5,0) not null,
    ps4_rest_world DECIMAL(5,0) not null,
    ps4_global DECIMAL(5,0) not null
);

--LOAD DATA, REPLACE WITH A DEDICATED SQLITE DATABASE LATER

.mode "csv"
.separator ","
.headers off
.import Data/games-data.csv gameData
.import Data/games.csv Games
.import Data/indie-games-developers.csv indieDevs
.import Data/Video_Games_Sales_as_at_22_Dec_2016.csv gameSales
.import Data/video-games-developers.csv gameDevs
.import Data/Windows_Games_List.csv windowsGames
.import Data/PS4_GamesSales.csv ps4Sales
.import Data/XboxOne_GameSales.csv xboxSales


--OUTPUT TO FILE (To be modified for cleaner outputs)

.mode "list"
.separator |
.output results.out

--EXECUTE QUERIES (Examples, not Final)

.print "--------------------1---------------------"
.print "SELECT"
--1--

SELECT gd_name FROM gameData
WHERE gd_platform = 'Wii'
LIMIT 20;


.print "--------------------2---------------------"
.print "SELECT"
--2--

SELECT g_title FROM Games
WHERE strftime('%Y', g_releaseNA) = '2000' AND g_mainStory > 30
LIMIT 20;


.print "--------------------3---------------------"
.print "SELECT"
--3--

SELECT * FROM gameDevs
WHERE gdev_developer = 'Blizzard Entertainment';


.print "--------------------4---------------------"
.print "SELECT"
--4--

SELECT gs_name, gs_platform, gs_release_year FROM gameSales
WHERE gs_publisher = 'Nintendo' AND gs_release_year > '2000'
LIMIT 30;


.print "--------------------5---------------------"
.print "SELECT"
--5--

SELECT gdev_developer FROM gameDevs
WHERE gdev_city = 'Tokyo'
LIMIT 30;


.print "--------------------6---------------------"
.print "SELECT"
--6--

SELECT g_title FROM Games, gameData
WHERE g_title = gd_name AND gd_users > 10000
LIMIT 30;


.print "--------------------7---------------------"
.print "SELECT"
--7--

.print "Action games that are on both Xbox and PS4 published by Acivision"

SELECT Distinct xbox_game, gs_rating FROM xboxSales, ps4Sales, gameSales
WHERE xbox_game = ps4_game AND ps4_genre = 'Action' AND ps4_game = gs_name AND gs_publisher = 'Activision'
LIMIT 30;


.print "--------------------8---------------------"
.print "UPDATE"
--8--

SELECT * FROM windowsGames
WHERE wg_developer = 'Mojang';

UPDATE windowsGames
SET wg_titles = 'MINECRAFT IS GREAT'
WHERE wg_titles = 'Minecraft';

SELECT * FROM windowsGames
WHERE wg_developer = 'Mojang';


.print "--------------------9---------------------"
.print "UPDATE"
--9--

SELECT g_title, g_platforms, g_publishers FROM Games
WHERE g_publishers = 'Microsoft Game Studios' AND g_platforms LIKE 'Xbox%'
LIMIT 5;

UPDATE Games
SET g_publishers = 'Xbox Game Studios'
WHERE g_publishers = 'Microsoft Game Studios' AND g_platforms LIKE 'Xbox%';

.print ""

SELECT g_title, g_platforms, g_publishers FROM Games
WHERE g_publishers = 'Xbox Game Studios' AND g_platforms LIKE 'Xbox%'
LIMIT 5;


.print "--------------------10---------------------"
--10--

.print "UPDATE"
SELECT g_title, gd_uscore FROM Games, gameData
WHERE g_title = gd_name AND gd_users < 10 AND g_mainStory < 10 AND gd_uscore != 'tbd'
LIMIT 10;

UPDATE gameData
SET gd_uscore = Round(gd_uscore)
WHERE gd_name IN ( 
    SELECT g_title FROM Games, gameData 
    WHERE g_title = gd_name AND gd_users < 10 AND g_mainStory < 10 AND gd_uscore != 'tbd'
    LIMIT 10);

.print ""

SELECT g_title, gd_uscore FROM Games, gameData
WHERE g_title = gd_name AND gd_users < 10 AND g_mainStory < 10 AND gd_uscore != 'tbd'
LIMIT 10;


.print "--------------------11---------------------"
.print "UPDATE"
--11--

SELECT gd_name, gd_genre FROM gameData
WHERE gd_genre LIKE '%Role-Playing%' 
LIMIT 10;

UPDATE gameData
SET gd_genre = 'RPG'
WHERE gd_genre LIKE '%Role-Playing%' AND gd_date > 'December 31, 2010' ;
--operation is expensive so reduced for time sake--

.print ""

SELECT gd_name, gd_genre FROM gameData
WHERE gd_genre LIKE '%RPG%' AND gd_date > 'December 31, 2010' 
LIMIT 10;


.print "--------------------12---------------------"
.print "UPDATE"
--12--

SELECT ind_developer, ind_notes FROM indieDevs
WHERE ind_notes = ''
LIMIT 5;

UPDATE indieDevs
SET ind_notes = 'No Description Available'
WHERE ind_notes = '';

.print ""

SELECT ind_developer, ind_notes FROM indieDevs
WHERE ind_notes = 'No Description Available'
LIMIT 5;


.print "--------------------13---------------------"
.print "INSERT"
--13--

INSERT INTO gameSales (gs_name, gs_platform, gs_release_year, gs_genre, gs_publisher)
VALUES ('Pokemon Violet/Pokemon Scarlet','Switch','2022','Role-Playing','Nintendo');

SELECT * FROM gameSales
WHERE gs_name = 'Pokemon Violet/Pokemon Scarlet';


.print "--------------------14---------------------"
.print "INSERT"
--14--

.print "Print information on '3D Ultra MiniGolf Adventures 2' if it exists:"

SELECT * FROM windowsGames
WHERE wg_titles = '3D Ultra MiniGolf Adventures 2';

.print ""
.print "Insert title and then print:"

INSERT INTO windowsGames(wg_titles, wg_released, wg_developer, wg_publisher, wg_genre)
SELECT g_title, g_releaseNA, g_developers, g_publishers, g_genres FROM Games
WHERE g_title NOT IN (SELECT wg_titles FROM windowsGames) AND g_platforms LIKE '%PC';

SELECT * FROM windowsGames
WHERE wg_titles = '3D Ultra MiniGolf Adventures 2';


.print "--------------------15---------------------"
.print "INSERT"
--15--

SELECT * FROM gameDevs
WHERE gdev_developer = 'Type-Moon';

INSERT INTO gameDevs(gdev_developer, gdev_city, gdev_administrative_division, gdev_country, gdev_est, gdev_notable)
VALUES ('Type-Moon', 'Tokyo', '', 'Japan', '1998', (SELECT g_title FROM Games WHERE g_developers = 'Type-Moon' LIMIT 1));

SELECT * FROM gameDevs
WHERE gdev_developer = 'Type-Moon';


.print "--------------------16---------------------"
.print "INSERT"
--16--

INSERT INTO indieDevs (ind_developer, ind_city, ind_autonomous_area, ind_country, ind_notable, ind_notes)
VALUES ('Blendo Games', 'Culver City','', 'United States', 'Gravity Bones', '');

SELECT * FROM indieDevs
WHERE ind_developer = 'Blendo Games';


--Mostly like should have all delete statements near the end
--so they don't affect the other statements

.print "--------------------17---------------------"
.print "DELETE"
.print "Titles published by Activision with a Critic score less than 70"
--17--

SELECT g_title, gd_platform, gd_score FROM Games, gameData
WHERE g_title = gd_name AND g_publishers = 'Activision'
LIMIT 10;

DELETE FROM Games
WHERE g_title IN (SELECT gd_name FROM gameDATA WHERE gd_score < 70)
      AND g_publishers = 'Activision';

.print ""
.print "Delete and print"

SELECT g_title, gd_platform, gd_score FROM Games, gameData
WHERE g_title = gd_name AND g_publishers = 'Activision'
LIMIT 10;


.print "--------------------18---------------------"
.print "DELETE"
--18--

SELECT g_title FROM Games
WHERE g_title IN (SELECT gs_name FROM gameSales WHERE gs_NA_sales < 10000)
LIMIT 10;

DELETE FROM Games 
WHERE g_title IN (SELECT gs_name FROM gameSales WHERE gs_NA_sales < 10000);

.print ""
.print "Delete and print"

SELECT g_title FROM Games
WHERE g_title IN (SELECT gs_name FROM gameSales WHERE gs_NA_sales < 10000);


.print "--------------------19---------------------"
.print "DELETE"
.print "All Games without entries in the gameData table "
--19--

SELECT g_title FROM GAMES
WHERE g_title NOT IN(SELECT gd_name FROM gameData)
LIMIT 10 OFFSET 100;

.print ""
.print "Delete and print"
DELETE FROM GAMES
WHERE g_title NOT IN(SELECT gd_name FROM gameData);

SELECT g_title FROM GAMES
WHERE g_title NOT IN(SELECT gd_name FROM gameData)
LIMIT 10;


.print "--------------------20---------------------"
.print "DELETE"
.print "All COD games from Games table"
--20--

.print "PRINT FIRST"

SELECT g_title FROM Games
WHERE g_title LIKE 'Call Of Duty%'
LIMIT 5;

DELETE FROM Games
WHERE g_title LIKE 'Call Of Duty%';

.print ""
.print "DELETED!!! PRINT AGAIN"

SELECT g_title FROM Games
WHERE g_title LIKE 'Call Of Duty%';

.print ""
.print "END"