ALTER SESSION set container="pdb1";
SHOW user
SHOW con_name

DROP USER apiTester CASCADE; 
ALTER USER apiTester ACCOUNT UNLOCK;
CREATE USER apiTester IDENTIFIED BY "apiTester1234"
DEFAULT TABLESPACE users
QUOTA UNLIMITED ON users;

-- REVOKE all privileges FROM apiTester;
GRANT create session TO apiTester;
GRANT RESOURCE TO apiTester;

SELECT *
FROM dba_users
WHERE username = UPPER('apiTester');

