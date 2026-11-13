#HU-1: Como empresa, quiero rechazar transferencias con monto inválido o mayor al saldo, 
#      para que nadie envíe dinero que no posee.
#HU-2: Como empresa, quiero un límite diario de $200.000 por usuario, 
#      para reducir el riesgo de fraude.     
#LISTADO DE CRITERIOS DE ACEPTACION HU-1:
#- Dado un acumulado de 100000 $ cuando intento transferir 40000 $ la transferencia se APRUEBA

MONTO_INVALIDO = "Rechazada: monto inválido" 
SALDO_INSUFICIENTE = "Rechazada: saldo insuficiente"   
LIMITE_DIARIO=200000  
LIMITE_EXCEDIDO= "Rechazada: límite diario excedido"  
APROBADA= "Transferencia exitosa" 
def transferir(saldo,monto,monto_acumulado):
    if monto<=0:
        return MONTO_INVALIDO
    if monto>saldo:
        return SALDO_INSUFICIENTE
    if monto_acumulado+monto>LIMITE_DIARIO:
        return LIMITE_EXCEDIDO
    return APROBADA  

#test_transferencias.py
import unittest
from transferencias import(transferir, MONTO_INVALIDO,SALDO_INSUFICIENTE,LIMITE_DIARIO,LIMITE_EXCEDIDO,APROBADA)
class TestTransferir(unittest.TestCase):
    # HU001
    def test_aprobada_por_envio_normal(self):
        self.assertEqual(transferir(50000,40000,100000),APROBADA)
    def test_monto_cero(self):
        self.assertEqual(transferir(50000,0,100000),MONTO_INVALIDO)
    def test_limite_excedido(self):
        self.assertEqual(transferir(50000,50000,200000),LIMITE_EXCEDIDO)
if __name__ == "__main__":
    unittest.main()    