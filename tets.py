from xxlimited import Null

respuesta = {
  "data": {
    "domain": "intercom.com",
    "disposable": False,
    "webmail": False,
    "accept_all": True,
    "pattern": "{first}",
    "organization": "Intercom",
    "description": "Faster resolutions, higher CSAT, and lighter support volumes with the only platform to combine the power of automation and human customer support.",
    "industry": "Software Development",
    "twitter": Null,
    "facebook": Null,
    "linkedin": Null,
    "instagram": Null,
    "youtube": Null,
    "technologies": ["amazon-web-services", "facebook", "intercom", "marketo", "node-js", "react", "recaptcha", "sentry"],
    "country": Null,
    "state": Null,
    "city": Null,
    "postal_code": Null,
    "street": Null,
    "headcount": "501-1000",
    "company_type": "Educational Institution",
    "emails": [
      {
        "value": "ciaran@intercom.com",
        "type": "personal",
        "confidence": 92,
        "sources": [
          {
            "domain": "github.com",
            "uri": "http://github.com/ciaranlee",
            "extracted_on": "2015-07-29",
            "last_seen_on": "2017-07-01",
            "still_on_page": True
          },
          {
            "domain": "blog.intercom.com",
            "uri": "http://blog.intercom.com/were-hiring-a-support-engineer/",
            "extracted_on": "2015-08-29",
            "last_seen_on": "2017-07-01",
            "still_on_page": True
          },
          ...
        ],
        "first_name": "Ciaran",
        "last_name": "Lee",
        "position": "Support Engineer",
        "seniority": "senior",
        "department": "it",
        "linkedin": Null,
        "twitter": "ciaran_lee",
        "phone_number": Null,
        "verification": {
          "date": "2019-12-06",
          "status": "valid"
        }
      },
      ...
    ],
    "linked_domains": []
  },
  "meta": {
    "results": 35,
    "limit": 10,
    "offset": 0,
    "params": {
      "domain": "intercom.com",
      "company": Null,
      "type": Null,
      "seniority": Null,
      "department": Null
    }
  }
}

print(respuesta['data']['emails'][0]['value'])