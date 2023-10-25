from pydantic import BaseModel


class ResponseClinicalTrial(BaseModel):
    nct_id: str  # in response; protocolSection.identificationModule.nctId
    brief_title: str  # in response; protocolSection.identificationModule.briefTitle
    official_title: str  # in response; protocolSection.identificationModule.officialTitle
    verification_date: str  # in response; protocolSection.statusModule.statusVerifiedDate
    overall_status: str  # in response; protocolSection.statusModule.overallStatus
    brief_summary: str  # in response; protocolSection.descriptionModule.briefSummary
    detailed_description: str  # in response; protocolSection.descriptionModule.detailedDescription
    conditions: str  # in response; protocolSection.conditionalModule.conditions.[in integer number key].conditions
    study_type: str  # in response; protocolSection.designModule.studyType
    eligibility_criteria: str  # in response; protocolSection.eligibilityModule.eligibilityCriteria

    # T ODO:2
    """
    new arm interventions section should be investigate
    other module also had additional information these areas should be investigate
    """
