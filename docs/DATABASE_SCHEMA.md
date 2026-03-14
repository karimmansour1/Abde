# Database Schema (CRM Core)

## Tables

1. `beneficiaries`
   - Core person/household-facing record.
   - Includes vulnerability and consent fields plus workflow stage.

2. `volunteers`
   - Volunteer profile and readiness data.
   - Tracks onboarding and availability status.

3. `cases`
   - Operational case linked to beneficiary.
   - Optionally assigned to a volunteer.

4. `workflow_events`
   - Audit-like timeline of workflow transitions and actions.

## Relationships

- `cases.beneficiary_id -> beneficiaries.id` (many-to-one)
- `cases.assigned_volunteer_id -> volunteers.id` (many-to-one, nullable)
- `workflow_events.related_case_id -> cases.id` (many-to-one, nullable)

## Workflow-focused fields

- Beneficiary workflow: `workflow_stage`, `consent_status`, `vulnerability_status`
- Volunteer workflow: `onboarding_status`, `availability_status`
- Case workflow: `stage`, `priority`, `category`
