# 📸 GUÍA PARA CAPTURAS DE PANTALLA

## INSTRUCCIONES PARA TOMAR LAS CAPTURAS

### **PREPARACIÓN**
1. Asegúrate de que el servidor esté corriendo: `python manage.py runserver`
2. Ten abierto un navegador web
3. Ten creado un usuario de prueba

---

## **CAPTURA 1: PÁGINA PRINCIPAL PÚBLICA**

### **URL**: `http://127.0.0.1:8000/`

### **QUÉ CAPTURAR**:
- Página completa del landing page
- Mostrar que es accesible sin login
- Enlace "Login" en la navegación visible

### **ELEMENTOS CLAVE A MOSTRAR**:
- Título "Bienvenido a Sabor Casero"
- Navegación superior
- Botón/enlace para ir al login
- URL visible en la barra del navegador

---

## **CAPTURA 2: FORMULARIO DE LOGIN**

### **URL**: `http://127.0.0.1:8000/accounts/login/`

### **QUÉ CAPTURAR**:
- Formulario completo de login
- Todos los campos visibles y vacíos
- Diseño profesional

### **ELEMENTOS CLAVE A MOSTRAR**:
- Campo "Email o Usuario"
- Campo "Contraseña"
- Checkbox "Recordar mis datos"
- Botón "Iniciar Sesión"
- Títulos e iconos
- URL visible: `/accounts/login/`

---

## **CAPTURA 3: REDIRECCIÓN AUTOMÁTICA**

### **PASOS**:
1. **SIN ESTAR LOGUEADO**, ir directamente a: `http://127.0.0.1:8000/dashboard/`
2. Observar que automáticamente te redirige a la página de login

### **QUÉ CAPTURAR**:
- La página de login después de la redirección
- URL que muestre la redirección: `http://127.0.0.1:8000/accounts/login/?next=/dashboard/`

### **ELEMENTOS CLAVE A MOSTRAR**:
- Formulario de login (resultado de la redirección)
- URL con parámetro `?next=/dashboard/` (esto demuestra la redirección automática)

---

## **CAPTURA 4: ERROR DE CREDENCIALES**

### **PASOS**:
1. En el formulario de login, ingresar credenciales incorrectas
2. Hacer clic en "Iniciar Sesión"

### **QUÉ CAPTURAR**:
- Formulario con mensaje de error visible
- Campos completados con datos incorrectos

### **ELEMENTOS CLAVE A MOSTRAR**:
- Mensaje de error: "Credenciales inválidas"
- Formulario con datos incorrectos visibles
- Styling de error (color rojo, etc.)

---

## **CAPTURA 5: LOGIN EXITOSO - DASHBOARD**

### **PASOS**:
1. Ingresar credenciales correctas en el formulario
2. Hacer clic en "Iniciar Sesión"
3. Ser redirigido al dashboard

### **URL**: `http://127.0.0.1:8000/dashboard/`

### **QUÉ CAPTURAR**:
- Dashboard completo después del login exitoso
- Información del usuario logueado visible
- Navegación de usuario autenticado

### **ELEMENTOS CLAVE A MOSTRAR**:
- Título del dashboard
- Información del usuario en la esquina (avatar, nombre)
- Menú lateral de usuario autenticado
- URL: `/dashboard/`
- Contenido que demuestra que es una página protegida

---

## **CAPTURA 6: MENÚ DE USUARIO AUTENTICADO**

### **QUÉ CAPTURAR**:
- Menú dropdown del usuario (si existe)
- O sidebar con opciones de usuario logueado
- Opción "Cerrar Sesión" visible

### **ELEMENTOS CLAVE A MOSTRAR**:
- Nombre del usuario logueado
- Opciones disponibles para usuarios autenticados
- Botón/enlace "Cerrar Sesión"

---

## **CAPTURA 7: GESTIÓN DE PLATILLOS (PÁGINA PROTEGIDA)**

### **URL**: `http://127.0.0.1:8000/platillos/platillos/`

### **PASOS**:
1. Estando logueado, acceder a la gestión de platillos
2. Mostrar que es una página que requiere autenticación

### **QUÉ CAPTURAR**:
- Lista de platillos o formulario de gestión
- Demostrar que es contenido protegido

### **ELEMENTOS CLAVE A MOSTRAR**:
- Interfaz de gestión de platillos
- Usuario logueado visible en la interfaz
- URL de la página protegida

---

## **CAPTURA OPCIONAL: LOGOUT**

### **PASOS**:
1. Estando logueado, hacer clic en "Cerrar Sesión"
2. Ser redirigido a la página principal

### **QUÉ CAPTURAR**:
- Página principal después del logout
- Demostrar que ya no está logueado (no hay información de usuario)

---

## 📋 **CHECKLIST PARA CAPTURAS**

### **Antes de tomar cada captura:**
- [ ] Servidor Django corriendo
- [ ] Navegador con zoom al 100%
- [ ] URL visible en barra de direcciones
- [ ] Página completamente cargada
- [ ] Imagen clara y legible

### **Elementos técnicos a incluir:**
- [ ] URL completa visible
- [ ] Tiempo de respuesta del servidor
- [ ] Estado de la sesión (logueado/no logueado)
- [ ] Mensajes de error cuando corresponda

### **Para el PDF:**
- [ ] Tamaño de imagen apropiado
- [ ] Calidad de imagen alta
- [ ] Descripción clara debajo de cada captura
- [ ] Orden lógico de las capturas

---

## 🖼️ **FORMATO SUGERIDO PARA EL PDF**

### **Por cada captura incluir:**

**CAPTURA X: [TÍTULO]**
- **URL**: `http://127.0.0.1:8000/...`
- **Descripción**: [Qué muestra la captura]
- **Elementos clave**: [Lista de elementos importantes]
- **Estado del usuario**: [Logueado/No logueado]

**[IMAGEN DE LA CAPTURA]**

---

*Esta guía te ayudará a tomar todas las capturas necesarias para demostrar el funcionamiento completo del sistema de autenticación.*