import mysql.connector
import bcrypt

def registrar_usuario(nombre_usuario, contraseña, rol, cedula, correo, telefono, direccion):
    db = mysql.connector.connect(
        host="34.70.72.185",
        user="root",
        password="Jhonr2005",
        database="veterinaria"
    )
    cursor = db.cursor()

    # Hashear la contraseña antes de guardarla
    hashed_password = bcrypt.hashpw(contraseña.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    try:
        # Insertar en la tabla Usuarios
        cursor.execute("""
            INSERT INTO Usuarios (NombreUsuario, Contraseña, Rol) 
            VALUES (%s, %s, %s)
        """, (nombre_usuario, hashed_password, rol))
        usuario_id = cursor.lastrowid  # Obtener el ID del usuario recién creado

        # Insertar en DatosUsuarios con la cédula
        cursor.execute("""
            INSERT INTO DatosUsuarios (UsuarioID, Cedula, CorreoElectronico, Telefono, Direccion)
            VALUES (%s, %s, %s, %s, %s)
        """, (usuario_id, cedula, correo, telefono, direccion))

        db.commit()
        print("Usuario registrado exitosamente.")
    except mysql.connector.Error as err:
        print("Error al registrar usuario:", err)
        db.rollback()
    finally:
        cursor.close()
        db.close()

# Prueba de creación de usuario con cédula
registrar_usuario("admin", "admin", "Administrador", "123456789", "jramirezm16@ucnetral.edu.co", "3001234567", "Calle Falsa 123")
