CREATE DATABASE ml_financial;
USE ml_financial;
CREATE TABLE ml (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_id VARCHAR(50),
    pros TEXT,
    cons TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO ml (company_id, pros, cons)
VALUES (
    'TCS',
    'High ROE, Debt free',
    'Low dividend'
);
INSERT INTO ml (company_id, pros, cons)

