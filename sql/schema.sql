CREATE TABLE IF NOT EXISTS beneficiaries (
    id INTEGER PRIMARY KEY,
    registration_code VARCHAR(40) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(30),
    location VARCHAR(120),
    household_size INTEGER DEFAULT 1,
    date_of_birth DATE,
    vulnerability_status VARCHAR(50) DEFAULT 'unknown',
    consent_status VARCHAR(30) DEFAULT 'pending',
    workflow_stage VARCHAR(30) DEFAULT 'intake',
    notes TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS volunteers (
    id INTEGER PRIMARY KEY,
    volunteer_code VARCHAR(40) UNIQUE NOT NULL,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone VARCHAR(30),
    email VARCHAR(120),
    skills TEXT,
    onboarding_status VARCHAR(30) DEFAULT 'screening',
    availability_status VARCHAR(30) DEFAULT 'available',
    branch VARCHAR(80),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS cases (
    id INTEGER PRIMARY KEY,
    case_code VARCHAR(40) UNIQUE NOT NULL,
    beneficiary_id INTEGER NOT NULL REFERENCES beneficiaries(id),
    assigned_volunteer_id INTEGER REFERENCES volunteers(id),
    category VARCHAR(50) DEFAULT 'general_support',
    priority VARCHAR(20) DEFAULT 'medium',
    stage VARCHAR(30) DEFAULT 'new',
    summary TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS workflow_events (
    id INTEGER PRIMARY KEY,
    entity_type VARCHAR(30) NOT NULL,
    entity_id INTEGER NOT NULL,
    action VARCHAR(60) NOT NULL,
    actor VARCHAR(120),
    details TEXT,
    related_case_id INTEGER REFERENCES cases(id),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
