-- Create Dimension Tables:
-- 1. Create table dim_user
create table dim_user (
    user_sk SERIAL primary key,
    source_user_id integer not null,
    username varchar(100) not null,
    country varchar(50),
    registration_date date,
    created_at timestamp default current_timestamp 
);

-- 2. Create tavle dim_track
create table dim_track (
    track_sk SERIAL primary key,
    source_track_id integer not null,
    title varchar(200) not null,
    duration_sec integer not null,
    -- Is the track a single?
    is_single boolean default false,         
    album_title varchar(200),
    created_at timestamp default current_timestamp
);

-- 3. Create table dim_artist
create table dim_artist (
    artist_sk serial primary key,
    source_artist_id integer not null,
    name varchar(150) not null,
    genre varchar(50),
    country varchar(50),
    created_at timestamp default current_timestamp
);

-- 4. Create table dim_data
create table dim_date (
    date_sk serial primary key,
    full_date date not null,
    year integer not null,
    month integer not null,
    created_at timestamp default current_timestamp
);

-- 5. Create table dim_subscription
create table dim_subscription (
    subscription_sk serial primary key,
    -- 'Free' or 'Premium'
    subscription_type_name varchar(50) not null,  
    is_premium boolean not null,
    created_at timestamp default current_timestamp
);

-- Create Fact Table (fact_listening)
create table fact_listening (
    listening_sk serial primary key,
    
    -- External keys to measurements:
    user_sk integer references dim_user(user_sk),
    track_sk integer references dim_track(track_sk),
    artist_sk integer references dim_artist(artist_sk),
    date_sk integer references dim_date(date_sk),
    subscription_sk integer references dim_subscription(subscription_sk),
    
    -- Metrics:
    duration_listened_sec integer not null,
    is_completed boolean not null,
    
    listening_timestamp timestamp not null,
    created_at timestamp default current_timestamp
);


-- QUERY 1: Top 5 most popular artists
-- Which artists are listened to most often?
select 
    a.name as artist_name,
    count(*) as total_plays
from fact_listening as f
join dim_artist as a 
	on f.artist_sk = a.artist_sk
group by a.name
order by total_plays desc
limit 5;

-- QUERY 2: Number of listens by subscription type
-- How many tracks in total have users with Free and Premium subscriptions listened to?
select 
    s.subscription_type_name,
    count(*) as total_plays
from fact_listening as f
join dim_subscription as s 
	on f.subscription_sk = s.subscription_sk
group by s.subscription_type_name;

-- QUERY 3: Total listening time by country
-- In which country do users spend the most time listening to music?
select 
    u.country,
    sum(f.duration_listened_sec) as total_time_sec
from fact_listening as f
join dim_user as u 
	on f.user_sk = u.user_sk
group by u.country
order by total_time_sec desc 
limit 10;

-- QUERY 4: Singles vs. album tracks
-- What percentage of the total listening time was devoted to singles and what percentage to album tracks?
select 
    t.is_single,
    sum(f.duration_listened_sec) as total_time_sec
from fact_listening as f
join dim_track as t 
	on f.track_sk = t.track_sk
group by t.is_single;

-- QUERY 5: Monthly listening trends
-- How did the total listening time change from month to month?
select 
    d.year,
    d.month,
    sum(f.duration_listened_sec) as total_time_sec
from fact_listening as f
join dim_date as d 
	on f.date_sk = d.date_sk
group by d.year, d.month
order by d.year, d.month;