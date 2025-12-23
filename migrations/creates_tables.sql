 -- create table user --

create table if not exists "users"(
    id serial primary key,
    username varchar(100) not null unique,
    email varchar(255) not null unique,
    hashed_password varchar(255) not null,
    full_name varchar(255),
    role varchar(50) default 'viewer',
    is_active boolean default true,
    created_at timestamp with time zone default current_timestamp,
    updated_at timestamp with time zone
 );

  -- create table domain --

create table if not exists "domain"(
    id serial primary key,
    name varchar(255) not null unique,
    description text,
    status varchar(50) default 'active',
    created_by integer references "users"(id),
    created_at timestamp with time zone default current_timestamp,
    updated_at timestamp with time zone
);

  -- table monitoring data --

create table if not exists "monitoring_data"(
    id serial primary key,
    domain_id integer references "domain"(id) on delete cascade,
    platform varchar(100) not null,
    post_id varchar(100) unique not null,
    content text,
    author varchar(100),
    url varchar(1000) not null,
    likes integer default 0,
    comments integer default 0,
    shares integer default 0,
    view integer default 0,
    sentiment varchar(100),  
    sentiment_score float,
    metadata jsonb,
    posted_at timestamp with time zone,
    collected_at timestamp with time zone default current_timestamp
 );

 -- index created --

create index idx_monitoring_platform on monitoring_data(platform);
create index idx_monitoring_domain on monitoring_data(domain_id);
create index idx_monitoring_collected on monitoring_data(collected_at);
create index idx_monitoring_sentiment on monitoring_data(sentiment);