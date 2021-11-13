DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE pets (
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    type VARCHAR(255) NOT NULL,
    date_of_birth VARCHAR(255), NOT NULL,
    contact INT,
    vet_id INT REFERENCES vets(id)
);