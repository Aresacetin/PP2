
functions = [
    """
    CREATE OR REPLACE FUNCTION find_by_pattern(pattern VARCHAR(255))
    RETURNS TABLE (id INTEGER, name VARCHAR(255), phone VARCHAR(63))
    AS
    $$
    BEGIN
        RETURN QUERY
        SELECT * FROM contacts WHERE contacts.phone ILIKE pattern OR contacts.name ILIKE pattern;
    END;
    $$
    LANGUAGE plpgsql;
    """,

    """
    CREATE OR REPLACE FUNCTION select_with_pagination(lim INTEGER, offs INTEGER)
    RETURNS TABLE (id INTEGER, name VARCHAR(255), phone VARCHAR(63))
    AS
    $$
    BEGIN
        RETURN QUERY
        SELECT * FROM contacts LIMIT lim OFFSET offs;
    END;
    $$
    LANGUAGE plpgsql;
    """
]