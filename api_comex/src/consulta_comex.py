import pandas as pd
import requests

def consulta_comex(flow, ano_inicio, ano_fim):
    url = "https://api-comexstat.mdic.gov.br/cities?language=pt"
    payload = {
        "flow": flow,
        "monthDetail": True,
        "period": {
            "from": f"{ano_inicio}-01",
            "to": f"{ano_fim}-12"
        },
        "filters": [
            {
                "filter": "state",
                "values": [27]
            }
        ],
        "details": ["city", "country", "chapter", "economicBlock"],
        "metrics": ["metricFOB"]
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    response = requests.post(url, json=payload, headers=headers, verify=False)

    if response.status_code == 200:
        data = response.json()
        if data.get("data") and data["data"].get("list"):
            df = pd.DataFrame(data["data"]["list"])
            df["flow"] = flow
            return df
    return pd.DataFrame()

