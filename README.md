# JNRCS CRM

JNRCS CRM scaffold with a production-ready direction for humanitarian operations: beneficiary and volunteer workflows, case handling, Supabase-ready database connectivity, and API-first design.

## Delivered in this commit

- Full backend folder architecture with modular API/routes/services/integrations.
- Expanded database schema for beneficiaries, volunteers, cases, and workflow events.
- **8 humanitarian CRM agents** registry exposed by API.
- FastAPI backend endpoints for volunteer and beneficiary workflows.
- Supabase connection configuration and health exposure endpoint.
- SQL schema documentation and standalone SQL script.

## Quick start

```bash
docker compose up --build
```

- Frontend: http://localhost:5173
- Backend: http://localhost:8000
- API docs: http://localhost:8000/docs

## API highlights

### Beneficiary workflow
- `POST /api/v1/beneficiaries` → create intake record.
- `POST /api/v1/beneficiaries/{id}/stage` → move workflow stage (`intake`, `assessment`, `approved`, etc.).

### Volunteer workflow
- `POST /api/v1/volunteers` → create volunteer record.
- `POST /api/v1/volunteers/{id}/status` → update onboarding/availability status.

### Case workflow
- `POST /api/v1/cases` → open case for beneficiary.
- `POST /api/v1/cases/{id}/assign` → assign volunteer.
- `POST /api/v1/cases/{id}/stage` → update case stage.

### Agents and workflow telemetry
- `GET /api/v1/agents` → list 8 humanitarian CRM agents.
- `GET /api/v1/workflows/events` → workflow event stream.

### Supabase connection
- Configure in `backend/.env`:
  - `DATABASE_URL`
  - `SUPABASE_URL`
  - `SUPABASE_ANON_KEY`
  - `SUPABASE_SERVICE_ROLE_KEY`
- Check config visibility (safe metadata only):
  - `GET /api/v1/integrations/supabase`

## Schema and structure docs

- Full folder map: `docs/FOLDER_STRUCTURE.md`
- Schema explainer: `docs/DATABASE_SCHEMA.md`
- SQL DDL script: `sql/schema.sql`

## Local backend testing

```bash
cd backend
python -m pytest -q
```
