--docker run --name postgresql -v ~/dataFoot/persistence:/bitnami/postgresql -e POSTGRESQL_USERNAME=my_user -e POSTGRESQL_PASSWORD=password123 -e POSTGRESQL_DATABASE=datafoot_db -p 5432:5432 bitnami/postgresql:latest
--psql datafoot_db my_user
DROP TABLE IF EXISTS Odds;
DROP TABLE IF EXISTS Stats;
DROP TABLE IF EXISTS Matches;
DROP TABLE IF EXISTS Season;

CREATE TABLE IF NOT EXISTS Season (id varchar(9), init_year varchar(2), end_year varchar(2), number_of_teams int, completed boolean,
    CONSTRAINT PK_Season PRIMARY KEY (id),
    CONSTRAINT UK_Season UNIQUE (init_year, end_year));

CREATE TABLE IF NOT EXISTS Matches (
    match_id varchar(255) PRIMARY KEY,
    season_id varchar(9),
    match_date timestamp,
    local_team varchar(255),
    away_team varchar(255),
    half_time_local_team_goals int,
    half_time_away_team_goals int,
    local_team_goals int,
    away_team_goals int,
    CONSTRAINT FK_Season FOREIGN KEY (season_id) REFERENCES season(id));

CREATE TABLE IF NOT EXISTS Stats (
    season_id varchar(9) NOT NULL,
    stats_date timestamp NOT NULL,
    team varchar(255) NOT NULL,
    points int,
    table_position int,
    games_played int,
    games_won int,
    games_drawn int,
    games_lost int,
    goals_favour int,
    goals_against int,
    games_played_home int,
    games_won_home int,
    games_drawn_home int,
    games_lost_home int,
    goals_favour_home int,
    goals_against_home int,
    games_played_away int,
    games_won_away int,
    games_drawn_away int,
    games_lost_away int,
    goals_favour_away int,
    goals_against_away int,
    CONSTRAINT PK_Stats PRIMARY KEY (stats_date, season_id, team),
    CONSTRAINT FK_Season FOREIGN KEY (season_id) REFERENCES season(id));

CREATE TABLE IF NOT EXISTS Odds (
    odds_id SERIAL PRIMARY KEY,
    match_id varchar(255),
    bet_house varchar(255) NOT NULL,
    home_winner numeric(6,3)  NOT NULL,
    draw numeric(6,3) NOT NULL,
    away_winner numeric(6,3) NOT NULL,
    CONSTRAINT FK_Match FOREIGN KEY (match_id) REFERENCES matches(match_id)
);