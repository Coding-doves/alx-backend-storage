-- SQL script that creates an index on the table names and score
CREATE INDEX idx_name_first_score ON names (name(1), score);
