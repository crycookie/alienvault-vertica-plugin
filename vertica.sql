INSERT INTO plugin (id, type, name, description) VALUES (10017, 1, 'vertica', 'Vertica DB events');
INSERT INTO plugin_sid (plugin_id, sid, category_id, class_id, name, priority, reliability) VALUES (10017, 001, NULL, NULL, 'vertica: Login Failed' ,3, 2);
