welcome_message = """
  Hola, te habla el asistente virtual Cootratiempo, ingresa el numero de tu solicitud.\n
  *1)* Información de servicios\n
  *2)* Horarios de atención\n
  *3)* Registrar PQRS\n
  *4)* Hablar con un asesor\n
"""

info_servicios = """
  *Información de servicios:*\n\n
  Cootratiempo ofrece una variedad de servicios para satisfacer tus necesidades. Aquí tienes un resumen de nuestros servicios más destacados:\n
  *Ahorros Programados:* Planifica tu futuro con nuestros planes de ahorro flexibles y adaptados a tus objetivos financieros.\n
  *Créditos Personales:* Obtén el financiamiento que necesitas para tus proyectos personales con tasas competitivas y condiciones accesibles.\n
  *Servicios Financieros:* Accede a una amplia gama de servicios financieros, incluyendo transferencias, pagos y más.\n
  *Asesoría Financiera:* Nuestro equipo de expertos está disponible para brindarte asesoría personalizada y ayudarte a tomar decisiones informadas.\n\n
  Si deseas más información sobre alguno de estos servicios, no dudes en preguntar. Estamos aquí para ayudarte.
  Si necesitas asistencia adicional, puedes escribir *asesor* en cualquier momento.
  Si deseas volver al menú principal, escribe *menu*.
  Si deseas salir, escribe *salir*.
  """
  
horarios_atencion = """
  Nuestros horarios de atención son los siguientes:\n
  *Lunes a Viernes:* 8:00 AM - 5:00 PM\n
  *Sábados:* 9:00 AM - 1:00 PM\n
  Si necesitas asistencia adicional, puedes escribir *asesor* en cualquier momento.
  Si deseas volver al menú principal, escribe *menu*.
  Si deseas salir, escribe *salir*.
  """

pqrs = """
  Para registrar una PQRS (Petición, Queja, Reclamo o Sugerencia), por favor ingrese sus datos y seleccione su tipo de requerimiento\n\n
  Ingrese su numero de documento:\n
  """

def optionsPqrs():
  import requests
  import os
  from dotenv import load_dotenv

  load_dotenv()
  
  API_URL = os.getenv("API_URL")
  API_TOKEN = os.getenv("API_TOKEN")
  
  tipos_pqrs = requests.get(API_URL, 
                            headers={"Authorization": API_TOKEN})
  options = tipos_pqrs.json()
  setOptions = [
    {
      'index': index + 1,
      'option': option['name'],
      'id': option['id']
    }
    for index, option in enumerate(options)]
  text = """*Tipos de Solicitudes:*\n\n"""
  text += "Por favor, selecciona el numero del tipo de solicitud que deseas registrar:\n\n"
  for option in setOptions:
    text += f"*{option['index']})*  {option['option']}\n"
  
  successOptions = [str(option['index']) for option in setOptions]
  return text, successOptions, setOptions

def getBadWords():
    """
    Retorna una lista de malas palabras y groserías en español.
    Esta lista puede ser ampliada según el caso de uso.
    """
    return [
        "puta", "puto", "mierda", "malparido", "gonorrea", "hp",
        "pendejo", "idiota", "imbécil", "hijo de puta", "estúpido",
        "cabron", "culiao", "coño", "chinga", "jodido", "perra", "marica",
        "verga", "culo", "mierdero", "maldito", "chingada", "carajo", "cojones",
        "zorra", "cabrón", "gilipollas", "pelotudo", "pajero", "putita"
    ]

def createPqrs(session, phone_number):
    """
    Crea una PQRS (Petición, Queja, Reclamo o Sugerencia) a partir de la sesión del usuario.
    """
    import requests
        
    createdPqrs = {
        "name": session.get("name", ""),
        "asociado": session.get("document", ""),
        "email": session.get("email", ""),
        "phone": session.get("phone", phone_number),
        "description": session.get("description", ""),
        "userCreated": "whatsapp",
        "typePQRS": session.get("pqrs", ""),
    }

    # Aquí podrías enviar la PQRS a un endpoint o guardarla en una base de datos
    response = requests.post(
        "https://pqrscootratiempo.pythonanywhere.com/api/api-pqrs/",
        json=createdPqrs,
        headers={"Authorization": "TOKEN 5992587b2057001b8a752f141ccf435997497e32"}
    )
    
    if response.status_code == 201:
        return True, response.json()
    else:
        return False, response.json()