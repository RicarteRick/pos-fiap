-- 5. Import Table (Tabela de Importação)
CREATE TABLE export (
    id SERIAL PRIMARY KEY,
    grape_type_name grape_type NOT NULL,
    country VARCHAR(100) NOT NULL,
    quantity_kg NUMERIC(15,2),
    value_usd NUMERIC(15,2)
);
