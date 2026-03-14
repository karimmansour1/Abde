# Full Folder Structure

```text
.
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── agents.py
│   │   │   ├── beneficiaries.py
│   │   │   ├── cases.py
│   │   │   ├── integrations.py
│   │   │   ├── volunteers.py
│   │   │   └── workflows.py
│   │   ├── core/
│   │   │   └── config.py
│   │   ├── db/
│   │   │   ├── base.py
│   │   │   └── session.py
│   │   ├── integrations/
│   │   │   └── supabase.py
│   │   ├── models/
│   │   │   ├── beneficiary.py
│   │   │   ├── case.py
│   │   │   ├── volunteer.py
│   │   │   └── workflow_event.py
│   │   ├── schemas/
│   │   │   ├── agents.py
│   │   │   ├── beneficiary.py
│   │   │   ├── case.py
│   │   │   ├── volunteer.py
│   │   │   └── workflow_event.py
│   │   ├── services/
│   │   │   ├── agents.py
│   │   │   └── workflow.py
│   │   └── main.py
│   ├── tests/
│   │   ├── test_health.py
│   │   └── test_workflows.py
│   ├── .env.example
│   ├── Dockerfile
│   └── requirements.txt
├── docs/
│   ├── DATABASE_SCHEMA.md
│   └── FOLDER_STRUCTURE.md
├── frontend/
│   ├── src/
│   ├── Dockerfile
│   ├── package.json
│   └── vite.config.ts
├── sql/
│   └── schema.sql
├── docker-compose.yml
├── Makefile
└── README.md
```
