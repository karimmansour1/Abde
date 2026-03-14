from app.schemas.agents import HumanitarianAgent

AGENTS: list[HumanitarianAgent] = [
    HumanitarianAgent(
        key="intake_triage_agent",
        name="Intake & Triage Agent",
        purpose="Classifies incoming beneficiary requests and sets urgency.",
        trigger="When a new beneficiary record is created.",
    ),
    HumanitarianAgent(
        key="consent_guardian_agent",
        name="Consent Guardian Agent",
        purpose="Checks consent status before data sharing or referral.",
        trigger="Before any external referral is initiated.",
    ),
    HumanitarianAgent(
        key="vulnerability_scoring_agent",
        name="Vulnerability Scoring Agent",
        purpose="Applies vulnerability scoring rubric to beneficiary households.",
        trigger="After intake updates or periodic reassessment.",
    ),
    HumanitarianAgent(
        key="case_assignment_agent",
        name="Case Assignment Agent",
        purpose="Matches cases to officers/volunteers by workload and skills.",
        trigger="When a case moves to assignment stage.",
    ),
    HumanitarianAgent(
        key="volunteer_readiness_agent",
        name="Volunteer Readiness Agent",
        purpose="Tracks onboarding, training, and readiness flags.",
        trigger="During volunteer onboarding and status changes.",
    ),
    HumanitarianAgent(
        key="followup_scheduler_agent",
        name="Follow-up Scheduler Agent",
        purpose="Creates follow-up tasks for unresolved or escalated cases.",
        trigger="On case stage updates or missed SLAs.",
    ),
    HumanitarianAgent(
        key="partner_referral_agent",
        name="Partner Referral Agent",
        purpose="Suggests partner organizations for specialized support pathways.",
        trigger="When case category requires external coordination.",
    ),
    HumanitarianAgent(
        key="donor_reporting_agent",
        name="Donor Reporting Agent",
        purpose="Compiles donor-facing impact summaries and KPI packets.",
        trigger="On reporting cycles and contribution milestones.",
    ),
]
