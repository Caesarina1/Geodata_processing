INSERT INTO geo_base_user (id, login, password, role)
VALUES ('7477d2a8-4401-4a20-8aa8-5cb04df87121', 'agent 001', '123456qwerty', 'Agent');

INSERT INTO geo_base_user (id, login, password, role)
VALUES ('7477d2a8-4401-4a20-8aa8-5cb04df87122', 'agent 002', '234567qwerty', 'Agent');

INSERT INTO geo_base_user (id, login, password, role)
VALUES ('7477d2a8-4401-4a20-8aa8-5cb04df87123', 'agent 003', '345678qwerty', 'Agent');

-- INSERT INTO geo_base_user (login, password, role)
-- VALUES ('agent 004', '456789qwerty', 'Agent');
--
-- INSERT INTO geo_base_user (login, password, role)
-- VALUES ('agent 005', '567890qwerty', 'Agent');

INSERT INTO geo_base_user (id, login, password, role)
VALUES ('7477d2a8-4401-4a20-8aa8-5cb04df87113', 'combat unit 001', '678901qwerty', 'Agent');

INSERT INTO geo_base_user (id, login, password, role)
VALUES ('d85a13d8-94fc-4936-b91f-7d006cce67c9', 'combat unit 002', '789012qwerty', 'Agent');

INSERT INTO geo_base_user (id, login, password, role)
VALUES ('1d5bb6e4-1818-4a24-919f-ba8085130e2c', 'combat unit 003', '890123qwerty', 'Agent');

-- INSERT INTO geo_base_user (login, password, role)
-- VALUES ('combat unit 004', '901234qwerty', 'Agent');
--
-- INSERT INTO geo_base_user (login, password, role)
-- VALUES ('combat unit 005', '012345qwerty', 'Agent');


INSERT INTO geo_base_target (target_id, type, latitude, longitude)
VALUES ('630898cd-d551-4ae3-94df-51950334a142', 'Особовий склад', '123456.01', '123456.02');



INSERT INTO geo_base_target_users (target_id, user_id)
    VALUES ('6412af20-a7f2-4317-b515-b037b2d28c1f', 'e8aeddfa-8596-4d7a-a50a-40fa859a0312');



INSERT INTO geo_base_target (target_id, type, latitude, longitude)
VALUES ('57748362-55a5-4483-a0ed-bb16d85d1c1c', 'Командний пункт', '234567.01', '234567.02');

INSERT INTO geo_base_target (target_id, type, latitude, longitude, users)
VALUES ('291b851b-284e-4bac-b1c5-d9d3d8e2cfd5', 'Техніка', '345678.01', '345678.02', '7477d2a8-4401-4a20-8aa8-5cb04df87121');


INSERT INTO geo_base_target (target_id, type, latitude, longitude)
VALUES ('aaaa851b-284e-4bac-b1c5-d9d3d8e21111', 'Інше', '345678.01', '345678.02');

-- INSERT INTO geo_base_target (type, latitude, longitude)
-- VALUES ('Інше', '456789.01', '456789.02');
