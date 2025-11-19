from flask import Flask, request, jsonify, render_template
from sqlalchemy.orm import Session
from database import init_db, get_db, Property, PropertyType, Operation, Location, Image
from sqlalchemy import or_
import os





app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()



# Initialize the database when the app starts
with app.app_context():
    init_db()
    
    db = next(get_db())
    # Check if PropertyType table is empty to avoid duplicate data on every run
    if not db.query(PropertyType).first():
        print("Inserting sample data...")
        # Add Property Types
        depa_type = PropertyType(name="Departamento")
        casa_type = PropertyType(name="Casa")
        ph_type = PropertyType(name="PH")
        oficina_type = PropertyType(name="Oficina")
        local_type = PropertyType(name="Local")
        terreno_type = PropertyType(name="Terreno")
        db.add_all([depa_type, casa_type, ph_type, oficina_type, local_type, terreno_type])

        # Add Operations
        venta_op = Operation(name="Venta")
        alquiler_op = Operation(name="Alquiler")
        alquiler_temp_op = Operation(name="Alquiler temporal")
        db.add_all([venta_op, alquiler_op, alquiler_temp_op])

        # Add Locations
        caballito_loc = Location(city="Buenos Aires", neighborhood="Caballito", province="CABA", country="Argentina", latitude=-34.6165, longitude=-58.4475)
        palermo_loc = Location(city="Buenos Aires", neighborhood="Palermo", province="CABA", country="Argentina", latitude=-34.5870, longitude=-58.4120)
        recoleta_loc = Location(city="Buenos Aires", neighborhood="Recoleta", province="CABA", country="Argentina", latitude=-34.5900, longitude=-58.3900)
        db.add_all([caballito_loc, palermo_loc, recoleta_loc])
        db.commit() # Commit types, ops, locations first to get their IDs

        # Refresh objects to get their IDs
        db.refresh(depa_type)
        db.refresh(casa_type)
        db.refresh(venta_op)
        db.refresh(alquiler_op)
        db.refresh(alquiler_temp_op)
        db.refresh(caballito_loc)
        db.refresh(palermo_loc)
        db.refresh(recoleta_loc)

        # Add Sample Properties
        prop1 = Property(
            code="UF000-1", title="Moderno Departamento en Caballito", description="Luminoso 3 ambientes con balcón",
            price=155000.00, currency="US$", surface_area_m2=77.79, num_rooms=3, num_bathrooms=1,
            status="available", property_type=depa_type, operation=venta_op, location=caballito_loc
        )
        prop2 = Property(
            code="UF000-2", title="Casa Amplia en Palermo", description="Casa con jardín y piscina",
            price=2500.00, currency="US$", surface_area_m2=180.00, num_rooms=4, num_bathrooms=2,
            status="available", property_type=casa_type, operation=alquiler_op, location=palermo_loc
        )
        prop3 = Property(
            code="UF000-3", title="PH en Recoleta", description="PH reciclado a nuevo, excelente ubicación",
            price=220000.00, currency="US$", surface_area_m2=90.00, num_rooms=3, num_bathrooms=1,
            status="available", property_type=ph_type, operation=venta_op, location=recoleta_loc
        )
        prop4 = Property(
            code="UF004-1", title="Oficina en Microcentro", description="Oficina moderna, ideal para startups",
            price=1200.00, currency="US$", surface_area_m2=50.00, num_rooms=2, num_bathrooms=1,
            status="available", property_type=oficina_type, operation=alquiler_op, location=caballito_loc
        )
        prop5 = Property(
            code="UF004-2", title="Local Comercial en Palermo", description="Local a la calle, alto tránsito",
            price=3500.00, currency="US$", surface_area_m2=100.00, num_rooms=0, num_bathrooms=1,
            status="available", property_type=local_type, operation=alquiler_op, location=palermo_loc
        )
        prop6 = Property(
            code="UF004-3", title="Terreno en Zona Norte", description="Ideal para desarrollo inmobiliario",
            price=500000.00, currency="US$", surface_area_m2=500.00, num_rooms=0, num_bathrooms=0,
            status="available", property_type=terreno_type, operation=venta_op, location=recoleta_loc
        )
        prop7 = Property(
            code="UF004-4", title="Departamento Temporal en Recoleta", description="Monoambiente amoblado, corta estadía",
            price=80.00, currency="US$", surface_area_m2=30.00, num_rooms=1, num_bathrooms=1,
            status="available", property_type=depa_type, operation=alquiler_temp_op, location=recoleta_loc
        )
        db.add_all([prop1, prop2, prop3, prop4, prop5, prop6, prop7])
        db.commit() # Commit properties

        # Refresh properties to get their IDs
        db.refresh(prop1)
        db.refresh(prop2)
        db.refresh(prop3)
        db.refresh(prop4)
        db.refresh(prop5)
        db.refresh(prop6)
        db.refresh(prop7)

        # Add Images for properties
        img1_prop1 = Image(property=prop1, url="UF000/UF000-1.jpg", description="Frente del departamento", order=1)
        img2_prop1 = Image(property=prop1, url="UF000/UF000-2.jpg", description="Living comedor", order=2)
        img1_prop2 = Image(property=prop2, url="UF000/UF000-3.jpg", description="Jardín de la casa", order=1)
        img2_prop2 = Image(property=prop2, url="UF000/UF000-4.jpg", description="Piscina", order=2)
        img1_prop3 = Image(property=prop3, url="UF000/UF000-5.jpg", description="Fachada del PH", order=1)
        img1_prop4 = Image(property=prop4, url="UF004/UF004-1.jpg", description="Interior oficina", order=1)
        img1_prop5 = Image(property=prop5, url="UF004/UF004-2.jpg", description="Frente local", order=1)
        img1_prop6 = Image(property=prop6, url="UF004/UF004-3.jpg", description="Vista aérea terreno", order=1)
        img1_prop7 = Image(property=prop7, url="UF004/UF004-4.jpg", description="Monoambiente", order=1)
        db.add_all([img1_prop1, img2_prop1, img1_prop2, img2_prop2, img1_prop3, img1_prop4, img1_prop5, img1_prop6, img1_prop7])
        db.commit()
        print("Sample data inserted successfully.")
    db.close()


@app.route("/api/dinamica")
def dinamica_properties():
    image_folder = 'DINAMICA'
    try:
        image_files = [f for f in os.listdir(image_folder) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]
        
        properties = []
        for i, image_file in enumerate(image_files):
            properties.append({
                "property_id": f"dinamica_{i}",
                "title": "Propiedad Dinámica",
                "description": f"Imagen {i+1} de la carpeta DINAMICA",
                "price": None,
                "currency": "",
                "surface_area_m2": None,
                "num_rooms": None,
                "num_bathrooms": None,
                "status": "available",
                "property_type": "Imagen",
                "operation": "Dinamica",
                "location": {
                    "city": "DINAMICA",
                    "neighborhood": "Carpeta local"
                },
                "images": [{"url": os.path.join(image_folder, image_file).replace('\\', '/'), "description": "Imagen dinámica"}]
            })
        return jsonify(properties)
    except FileNotFoundError:
        return jsonify({"error": "La carpeta 'DINAMICA' no fue encontrada."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/api/properties/search", methods=["GET"])
def search_properties():
    db: Session = next(get_db())
    
    ope = request.args.get("ope")
    tipo = request.args.get("tipo")
    loc = request.args.get("loc")
    cod = request.args.get("cod")

    query = db.query(Property)

    if ope:
        query = query.join(Operation).filter(Operation.name == ope)
    if tipo:
        query = query.join(PropertyType).filter(PropertyType.name == tipo)
    if loc:
        # Search in both city and neighborhood
        query = query.join(Location).filter(or_(
            Location.city.ilike(f"%{loc}%"),
            Location.neighborhood.ilike(f"%{loc}%")
        ))
    if cod:
        query = query.filter(Property.code == cod)

    properties = query.all()

    results = []
    for prop in properties:
        results.append({
            "property_id": prop.property_id,
            "code": prop.code,
            "title": prop.title,
            "description": prop.description,
            "price": float(prop.price),
            "currency": prop.currency,
            "surface_area_m2": float(prop.surface_area_m2),
            "num_rooms": prop.num_rooms,
            "num_bathrooms": prop.num_bathrooms,
            "status": prop.status,
            "property_type": prop.property_type.name if prop.property_type else None,
            "operation": prop.operation.name if prop.operation else None,
            "location": {
                "city": prop.location.city if prop.location else None,
                "neighborhood": prop.location.neighborhood if prop.location else None,
            },
            "images": [
                {"url": img.url, "description": img.description} 
                for img in sorted(prop.images, key=lambda x: x.order)
            ]
        })
    
    db.close()
    return jsonify(results)

@app.route("/")
def index():
    return "Welcome to the Property Search API. Use /api/properties/search to query."

if __name__ == "__main__":
    app.run(debug=True)