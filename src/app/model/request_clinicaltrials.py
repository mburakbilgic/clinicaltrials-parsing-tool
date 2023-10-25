from pydantic import BaseModel


class RequestClinicalTrial(BaseModel):
    # T ODO.1
    """
    from clinicaltrials.gov/data-about-studies section
    PieceName and their related request params defined
    for api/v2/studies,
    each related params should be define under that.
    took their reference from response body
    """
