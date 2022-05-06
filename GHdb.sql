DROP TABLE IF EXISTS user;
DROP TABLE IF EXISTS email_status;

CREATE TABLE user (
    user_id             integer  primary key AUTOINCREMENT,
    primary_contact     VARCHAR(35) NOT NULL,
    primary_status_id   integer NOT NULL,
    primary_timestamp   DATETIME NOT NULL,
    secondary_contact   VARCHAR(35) NOT NULL,
    secondary_status_id integer NOT NULL,
    secondary_timestamp DATETIME NOT NULL,
    first_name          VARCHAR(50) NOT NULL,
    last_name           VARCHAR(50) NOT NULL
    
);

CREATE TABLE email_status (
    status_id        integer primary key AUTOINCREMENT,
    email_status     VARCHAR(45) NOT NULL
    
);

.mode csv
.separator ","


-- searching for unconfirmed primary email
select * from user where primary_status_id = 2;

-- searching for unconfirmed secondary emails
select * from user where secondary_status_id = 2;

-- searching for confirmed primary emails and unconfirmed secondary emails
select * from user where primary_status_id = 1 and secondary_status_id =2;

-- show person id and when primary email was last updated
select user_id, primary_timestamp from user;

-- show accounts that were updated in the last year (example time frame)
select *
from user
where primary_timestamp  between '2021-01-01:01:01:01' and '2021-12-31:11:59:59'
group by user_id;

-- update primary email 
update user
set primary_contact = 'newName@domain.tld'

-- update secondary email 
update user 
set secondary_contact = 'newSecondaryEmail@domain.tld'
where user_id = 1;

-- inserting new user information
insert into user(user_id,primary_contact,primary_status_id,primary_timestamp,secondary_contact,secondary_status_id,secondary_timestamp,first_name,last_name)
values (51,'p51@domain.tld',27,'2022-07-01:04:52:39', 's51@domain.tld',27,'2022-07-01:04:52:39','FN51','LN51'),
(52,'p52@domain.tld',27,'1999-04-05:20:38:30', 's52@domain.tld',27,'1999-04-05:20:38:30','FN52','LN52');

