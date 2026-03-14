from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_beneficiary_and_case_volunteer_workflow():
    beneficiary = client.post(
        "/api/v1/beneficiaries",
        json={
            "registration_code": "BEN-001",
            "first_name": "Aisha",
            "last_name": "Khaled",
            "location": "Amman",
            "vulnerability_status": "high",
        },
    )
    assert beneficiary.status_code == 201
    beneficiary_id = beneficiary.json()["id"]

    stage_move = client.post(
        f"/api/v1/beneficiaries/{beneficiary_id}/stage",
        json={"workflow_stage": "assessment", "actor": "case.officer"},
    )
    assert stage_move.status_code == 200
    assert stage_move.json()["workflow_stage"] == "assessment"

    volunteer = client.post(
        "/api/v1/volunteers",
        json={
            "volunteer_code": "VOL-001",
            "first_name": "Omar",
            "last_name": "Nasser",
            "skills": "First aid, community outreach",
        },
    )
    assert volunteer.status_code == 201
    volunteer_id = volunteer.json()["id"]

    case = client.post(
        "/api/v1/cases",
        json={
            "case_code": "CASE-001",
            "beneficiary_id": beneficiary_id,
            "category": "cash_assistance",
            "priority": "high",
        },
    )
    assert case.status_code == 201
    case_id = case.json()["id"]

    assignment = client.post(
        f"/api/v1/cases/{case_id}/assign",
        json={"volunteer_id": volunteer_id, "actor": "assignment.agent"},
    )
    assert assignment.status_code == 200
    assert assignment.json()["assigned_volunteer_id"] == volunteer_id
    assert assignment.json()["stage"] == "assigned"


def test_agents_list_has_8_items():
    response = client.get("/api/v1/agents")
    assert response.status_code == 200
    payload = response.json()
    assert len(payload) == 8
