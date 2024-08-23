-- Set Up DWH , Database and Stage

CREATE or REPLACE warehouse normal_wh warehouse_size=XSMALL initially_suspended=true;
CREATE DATABASE leagues; 
CREATE STAGE "LEAGUES"."PUBLIC".demo_stage;

-------------------------------------------------------------------------------
-- CREATE NEW TABLE
-------------------------------------------------------------------------------

CREATE OR REPLACE TABLE football_leagues (
id         VARCHAR (30) NOT NULL,
equipo     VARCHAR (30) NOT NULL,
Jugados    INTEGER NOT NULL,
ganados    INTEGER NOT NULL,
empatados  INTEGER NOT NULL,
perdidos   INTEGER NOT NULL,
gf         INTEGER NOT NULL,
gc         INTEGER NOT NULL,
diff       INTEGER NOT NULL,
puntos     INTEGER NOT NULL,
liga       VARCHAR (30) NOT NULL,
created_at VARCHAR (30) NOT NULL
);

-------------------------------------------------------------------------------
-- LIST STAGE
-------------------------------------------------------------------------------

LIST @demo_stage;

-------------------------------------------------------------------------------
-- QUERY YOUR TABLE
-------------------------------------------------------------------------------

SELECT *
FROM "LEAGUES"."PUBLIC"."FOOTBALL_LEAGUES";