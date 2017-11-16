drop table if exists transcripts;
create table transcripts (
  id integer primary key autoincrement,
  url text not null,
  title text not null
);