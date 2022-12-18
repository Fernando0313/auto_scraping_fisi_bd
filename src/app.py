import msvcrt
import conexion_bd
from models.user import UserModel
def run():
    print("hola")
    user = UserModel()
    user.userEmail="rojofernando296@gmail.com"
    user.userLastName="Rojo"
    user.userName="fernando0313"
    user.userPassword="1234"
    user.userFirstName="Fernando"
    conexion_bd.session.add(user)
    conexion_bd.session.commit()
    print(user.userId)
    msvcrt.getch()

    
if __name__ == '__main__':
    # conexion_bd.Base.metadata.create_all(conexion_bd.engine)
    run()