CREATE TABLE ml (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company_id VARCHAR(50),
    pros TEXT,
    cons TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

