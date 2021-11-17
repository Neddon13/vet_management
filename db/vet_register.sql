DROP TABLE IF EXISTS pets;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;


CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    address VARCHAR(255) NOT NULL,
    mobile_num VARCHAR(255) NOT NULL
);

CREATE TABLE pets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    type_of_pet VARCHAR(255) NOT NULL,
    date_of_birth VARCHAR(255) NOT NULL,
    treatment_notes VARCHAR(255) NOT NULL,
    vet_id INT REFERENCES vets(id),
    owner_id INT REFERENCES owners(id)
);

