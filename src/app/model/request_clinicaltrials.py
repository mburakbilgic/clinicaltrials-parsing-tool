from pydantic import BaseModel


class RequestParamsClinicalTrial(BaseModel):

    request_params = {
        "pageSize": 10,  # Sayfa başına sonuç sayısı
        "pageToken": None,  # İlk sayfada bu parametre boş olmalıdır
        "query.cond": "cancer",
        "filter.overallStatus": "RECRUITING"
    }


class RequestStudiesClinicalTrial(BaseModel):
    """
    studies: list of dictionaries
             each studies had 3 dictionaries
             these key of main dictionaries is
                protocolSection, data type is dictionary had nested 12 dictionaries
                derivedSection, data type is dictionary  had nested 3 dictionaries
                hasResults, data type is bool

                in protocolSection,
                    identification module
                        studies[each]["protocolSection"]["identificationModule"]["nctId"]: str
                        studies[each]["protocolSection"]["identificationModule"]["briefTitle"]: str
                        studies[each]["protocolSection"]["identificationModule"]["officialTitle"]: str

                    status module
                        studies[each]["protocolSection"]["statusModule"]["statusVerifiedDate"]: str
                        studies[each]["protocolSection"]["statusModule"]["overallStatus"]: str

                    description module
                        studies[each]["protocolSection"]["descriptionModule"]["briefSummary"]: str
                        studies[each]["protocolSection"]["descriptionModule"]["detailedDescription"]: str

                    conditional module
                        studies[each]["protocolSection"]["conditionalModule"]["conditions"]: list
                        studies[each]["protocolSection"]["descriptionModule"]["detailedDescription"]: str

                    design module
                        studies[each]["protocolSection"]["designModule"]["studyType"]: str
                        studies[each]["protocolSection"]["designModule"]["phases"]: list
                        studies[each]["protocolSection"]["designModule"]["designInfo"]["allocation"]: str
                        studies[each]["protocolSection"]["designModule"]["designInfo"]["interventionModel"]: str
                        studies[each]["protocolSection"]["designModule"]["designInfo"]["primaryPurpose"]: str
                        studies[each]["protocolSection"]["designModule"]["designInfo"]["maskingInfo"]["masking"]: str
                        studies[each]["protocolSection"]["designModule"]["designInfo"]["enrollmentInfo"]["count"]: int
                        studies[each]["protocolSection"]["designModule"]["designInfo"]["enrollmentInfo"]["type"]: str

                    eligibilty module
                        studies[each]["protocolSection"]["eligibilityModule"]["eligibilityCriteria"]: str
                        studies[each]["protocolSection"]["eligibilityModule"]["healthyVolunteers"]: bool
                        studies[each]["protocolSection"]["eligibilityModule"]["sex"]: bool
                        studies[each]["protocolSection"]["eligibilityModule"]["minimumAge"]: str
                        studies[each]["protocolSection"]["eligibilityModule"]["stdAges"]: list
    """
    studies: list
