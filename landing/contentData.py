def landing(lanId):
    propertyId = ""
    agentId = ""
    if lanId == "001":
        landingData = {
            "propertyId": "001",
            "agentId": "001",
        }
    else:
        landingData = {
            "propertyId": "000",
            "agentId": "000",
        }

    return landingData

def property(propertyId):
    if propertyId == "001":
        propertyData = {
            "mainTitle": "Terreno 2Ha en zona urbana San Javier",
            "shortDescription": "Hermoso terreno en zona urbana de San Javier, especial para quinta o emprendimiento tur&iacute;stico",
            "features": [
                "Zona urbana de San Javier",
                "21,380mts<sup>2</sup> de superficie",
                "Documentos al d&#xed;a"
            ],
            "id": propertyId,
            "price": "128,280",
            "locationX": "-16.26787005",
            "locationY": "-62.50489984",
            "mainText": "./properties/maintext001.html",
            "mainimg": "p001i000.jpg",
            "images": [
                "p001i002.jpg",
                "p001i001.jpg",
                "p001i003.jpg"
            ]
        }
    else:
        propertyData = {
            "mainTitle": "Property Template",
            "shortDescription": "Descripci&#xf3;n corta del inmueble",
            "features": [
                "Feature 1",
                "Feature 2",
                "Feature 3"
            ],
            "id": propertyId,
            "price":"0",
            "locationX": "",
            "locationY": "",
            "mainText": "./properties/maintext000.html",
            "mainimg": "empty.jpg",
            "images": [
            ]
        }
    
    return propertyData

def agent(agentId):
    if agentId == "001":
        agentData = {
            "id": agentId,
            "name": "Juan Oroza",
            "whatsapp": "+591 78078880",
            "facebook": "eexplorainmob",
            "instagram": "eexplorainmob",
            # "phone": "+591 78078880",
            "profilepic": "a001p001.jpg"
        }
    else:
        agentData = {
            "id": agentId,
            "name": "none",
            "whatsapp": "none",
            "facebook": "none",
            "instagram": "none",
            "phone": "none",
            "profilepic": "a000p001.svg"
        }
    
    return agentData