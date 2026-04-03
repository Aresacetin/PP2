
procedures = [
    """
    CREATE OR REPLACE PROCEDURE delete_contact(pattern VARCHAR(255))
    AS
    $$
    BEGIN
        DELETE FROM contacts WHERE contacts.name ILIKE pattern OR contacts.phone ILIKE pattern;
    END;
    $$
    LANGUAGE plpgsql;
    """,

    """
    CREATE OR REPLACE PROCEDURE add_or_update(new_name VARCHAR(255), new_phone VARCHAR(255))
    AS
    $$
    BEGIN
        IF EXISTS (SELECT 1 FROM contacts WHERE name = new_name) THEN
            UPDATE contacts SET phone = new_phone
            WHERE name = new_name;
        ELSEIF EXISTS (SELECT 1 FROM contacts WHERE phone = new_phone) THEN
            UPDATE contacts SET name = new_name
            WHERE phone = new_phone;
        ELSE
            INSERT INTO contacts(name, phone)
            VALUES(new_name, new_phone);
        END IF;
    END;
    $$
    LANGUAGE plpgsql;
    """,

    r"""
    CREATE OR REPLACE PROCEDURE mass_insert(new_names VARCHAR(255)[], new_phones VARCHAR(255)[])
    AS
    $$
    DECLARE
        i INTEGER;
    BEGIN
        FOR i IN 1..array_length(new_names, 1) LOOP

            IF new_phones[i] ~ '^\+\d-\d{3}-\d{3}-\d{4}$' THEN
                INSERT INTO contacts(name, phone)
                VALUES(new_names[i], new_phones[i]);
            ELSE
                RAISE NOTICE 'Skipped invalid entry: name: % phone: %', new_names[i], new_phones[i];
            END IF;
        END LOOP;
    END;
    $$ LANGUAGE plpgsql;
    """
]