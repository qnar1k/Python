from flask import Flask, jsonify, request, abort
import json
import os

app = Flask(__name__)

DATA_FILE = "cars.json"

def load_cars():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump([], f)
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_cars(cars):
    with open(DATA_FILE, "w") as f:
        json.dump(cars, f, indent=4)

@app.route("/cars", methods=["GET"])
def get_cars():
    cars = load_cars()
    return jsonify(cars), 200

@app.route("/cars/<int:car_id>", methods=["GET"])
def get_car(car_id):
    cars = load_cars()
    car = next((c for c in cars if c["id"] == car_id), None)
    if car is None:
        abort(404, description="Car not found")
    return jsonify(car), 200

@app.route("/cars", methods=["POST"])
def add_car():
    cars = load_cars()
    new_car = request.get_json()
    if not new_car or "id" not in new_car or "make" not in new_car or "model" not in new_car or "year" not in new_car or "price" not in new_car:
        abort(400, description="Invalid car data")
    if any(c["id"] == new_car["id"] for c in cars):
        abort(400, description="Car with the same ID already exists")
    cars.append(new_car)
    save_cars(cars)
    return jsonify(new_car), 201

@app.route("/cars/<int:car_id>", methods=["PUT"])
def update_car(car_id):
    cars = load_cars()
    car = next((c for c in cars if c["id"] == car_id), None)
    if car is None:
        abort(404, description="Car not found")
    updated_data = request.get_json()
    if not updated_data:
        abort(400, description="Invalid car data")
    car.update(updated_data)
    save_cars(cars)
    return jsonify(car), 200

@app.route("/cars/<int:car_id>", methods=["DELETE"])
def delete_car(car_id):
    cars = load_cars()
    car = next((c for c in cars if c["id"] == car_id), None)
    if car is None:
        abort(404, description="Car not found")
    cars.remove(car)
    save_cars(cars)
    return jsonify({"message": f"Car with ID {car_id} deleted"}), 200

if __name__ == "__main__":
    app.run(debug=True)
