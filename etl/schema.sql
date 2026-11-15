CREATE TABLE IF NOT EXISTS flights
(
fl_date	DATE,
month SMALLINT,
day_of_week	SMALLINT,
op_unique_carrier TEXT,
origin	TEXT,
dest	TEXT,
crs_dep_time SMALLINT,
crs_arr_time SMALLINT,
crs_elapsed_time SMALLINT,
distance	SMALLINT,
arr_delay	SMALLINT,
is_delayed	SMALLINT,
cancelled	SMALLINT,
diverted	SMALLINT,
dep_delay	SMALLINT

);