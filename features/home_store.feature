Feature: Registro de formulario de contacto
    Scenario: Registro de formulario de contacto exitoso
        Given usuario está en página formulario contacto
        When ingresa campos "margot@dominio.com" "1171233" "El pedido me llego roto"
        And click en boton enviar
        Then obtiene mensaje confirmacion exitosa



