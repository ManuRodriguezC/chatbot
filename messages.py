welcome_message = """
  Hola, te habla el asistente virtual Cootratiempo, ingresa el numero de tu solicitud.\n
  *1)* Información de servicios\n
  *2)* Horarios de atención\n
  *3)* Registrar PQRS\n
  *4)* Hablar con un asesor\n
"""

info_servicios = """
  *COOTRATIEMPO* es una cooperativa de aporte y crédito fundada en 1975, vinculada a más de 50 empresas de medios de comunicación en Colombia. Ofrece diversos servicios a sus asociados y a sus familias. A continuación, se resumen los principales servicios y beneficios que se prestan\n\n
  *Servicios Financieros:*\n
  •	Amplio portafolio de créditos con tasas de interés competitivas (desde el 0,5% mensual, sujeto a condiciones).\n
  •	Créditos de hasta 150% en aportes ahorrados\n
  •	Sin costo por estudio de crédito ni consulta en centrales de riesgo (en líneas preferenciales como motocicleta, óptico, salud Etc.).\n\n
  *Beneficios para Asociados:*\n
  •	Asociación gratuita.\n
  •	Protección exequial sin costo para el asociado y 12 personas mas sin importar grado de consanguinidad, Incluida mascotas.\n
  •	Convenios con descuentos especiales en productos y servicios.\n
  •	Actividades recreativas y culturales con hasta 40% de descuento.\n
  •	Posibilidad de continuar como asociado, incluso si se retira de la empresa.\n
  •	El grupo familiar puede acceder a los mismos beneficios.\n\n
  *Servicios Adicionales:*\n
  •	Capacitaciones en temas como cooperativismo, educación financiera y manejo del puntaje crediticio.\n
  •	Servicios de turismo y recreación\n
  •	Auxilios Optivos, Clinicos, Calamidad Doméstica.\n
  •	Convenios estudiantiles\n\n
  Pago de aportes entre el 3% hasta el 20% sobre el salario y Para asociados independientes a partir del 5% SMMLV.\n
  Canales de comunicación\n
  Línea de atención: 6017454745\n
  Cel. 320 322 1739\n
  atencionalasociado@cootratiempo.com.co\n
  COMERCIAL COOTRATIEMPO\n
  Cel. 311 858 7480\n
  comercial@cootratiempo.com.co\n
  redes sociales\n
  https://www.facebook.com/profile.php?id=100085403948147\n
  https://www.instagram.com/cootratiempo/\n\n

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