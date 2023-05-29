CREATE TABLE transport(
    data DATE,
    seq INT,
    departure VARCHAR(20),
    arrival VARCHAR(20),
    via VARCHAR(40),
    amount INT,
    PRIMARY KEY (data, seq)
)