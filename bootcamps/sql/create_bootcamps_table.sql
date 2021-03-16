CREATE TABLE IF NOT EXISTS bootcamps
(
  bootcamp_id int,
  name text,
  identifying_str text,
  PRIMARY KEY (bootcamp_id)
);


INSERT or ignore INTO bootcamps values (1 , 'Overview of Statistics for Data Science' , 'statistics');
INSERT or ignore INTO bootcamps values (2 , 'Introduction to Python For Data Science' , 'python');
INSERT or ignore INTO bootcamps values (3 , 'Introduction to R For Data Science' , 'r for data science');
