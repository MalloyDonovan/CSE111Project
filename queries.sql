DROP TABLE gameData;
DROP TABLE Games;
DROP TABLE indieDevs;

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
    ind_notes VARCHAR(64) not null,
);

--LOAD DATA, REPLACE WITH A DEDICATED SQLITE DATABASE LATER

.mode "csv"
.separator ","
.headers off
.import Data/games-data.csv gameData
.import Data/games.csv Games
.import Data/indie-games-developers.csv indieDevs
--.import PS4_GameSales.csv ps4Sales
--.import Video_Games_Sales_as_at_22_Dec_2016.csv gameSales
--.import video-games-developers.csv gameDevs
--.import Windows_Games_List.csv windowsGames
--.import XboxOne_GameSales.csv xboxSales


--OUTPUT TO FILE (To be modified for cleaner outputs)

.mode "list"
.separator |
.output results.out

--EXECUTE QUERIES (Examples, not Final)

.print "--------------------1---------------------"
--1--
SELECT gd_name FROM gameData
WHERE gd_platform = 'Wii'
LIMIT 20;
;

.print "--------------------2---------------------"
--2--

SELECT g_title FROM Games
WHERE strftime('%Y', g_releaseNA) = '2000' AND g_mainStory > 30
LIMIT 20;


