-- script to record all scores

SELECT score, name FROM ${DB_NAME}.second_table WHERE score >= 10 ORDER BY score DESC;
