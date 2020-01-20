CREATE DATABASE fail_over;
CREATE USER sushil WITH PASSWORD 'sushil';
ALTER ROLE sushil SET client_encoding TO 'utf8'; 
ALTER ROLE sushil SET fail_over TO 'read committed'; 
ALTER ROLE sushil SET timezone TO 'Asia/Kolkata';

GRANT ALL PRIVILEGES ON DATABASE fail_over TO sushil;


CREATE DATABASE Release;
CREATE USER sushil WITH PASSWORD 'sushil';
ALTER ROLE sushil SET client_encoding TO 'utf8'; 
ALTER ROLE sushil SET Release TO 'read committed'; 
ALTER ROLE sushil SET timezone TO 'Asia/Kolkata';

GRANT ALL PRIVILEGES ON DATABASE Release TO sushil;


CREATE DATABASE Universal;
CREATE USER sushil WITH PASSWORD 'sushil';
ALTER ROLE sushil SET client_encoding TO 'utf8'; 
ALTER ROLE sushil SET Universal TO 'read committed'; 
ALTER ROLE sushil SET timezone TO 'Asia/Kolkata';

GRANT ALL PRIVILEGES ON DATABASE Universal TO sushil;


CREATE DATABASE 2.3.0;
CREATE USER sushil WITH PASSWORD 'sushil';
ALTER ROLE sushil SET client_encoding TO 'utf8'; 
ALTER ROLE sushil SET 2.3.0 TO 'read committed'; 
ALTER ROLE sushil SET timezone TO 'Asia/Kolkata';

GRANT ALL PRIVILEGES ON DATABASE 2.3.0 TO sushil;


CREATE DATABASE master;
CREATE USER sushil WITH PASSWORD 'sushil';
ALTER ROLE sushil SET client_encoding TO 'utf8'; 
ALTER ROLE sushil SET master TO 'read committed'; 
ALTER ROLE sushil SET timezone TO 'Asia/Kolkata';

GRANT ALL PRIVILEGES ON DATABASE master TO sushil;
