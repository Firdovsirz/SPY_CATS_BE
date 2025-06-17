# 🐾 Spy Cats Backend API

This is the backend for the **Spy Cats Mission Management System**, built with **FastAPI** and **SQLAlchemy**. It allows users to create and manage spy missions, assign cats to missions, and track targets.

---

## 🚀 Features

- ✅ Create and list missions
- ✅ Assign spy cats to missions
- ✅ Add and update mission targets
- ✅ Mark targets as complete
- ✅ Full CRUD operations with error handling
- ✅ Organized API routing
- ✅ Auto-generated Swagger docs (`/docs`)

---

## 🛠 Tech Stack

- **Python 3.10+**
- **FastAPI**
- **SQLAlchemy**
- **Pydantic**
- **Uvicorn**
- **PostgreSQL**

---

# 🐾 Spy Cats Backend API

This is the backend for the **Spy Cats Mission Management System**, built with **FastAPI** and **SQLAlchemy**. It allows users to create and manage spy missions, assign cats to missions, and track targets.

---

## 🚀 Features

- Create, list, update, and delete missions
- Assign spy cats to missions
- Manage mission targets and update their status
- Auto-generated API documentation with Swagger UI and ReDoc

---

## 🛠 Tech Stack

- Python 3.8+
- FastAPI
- SQLAlchemy
- Pydantic
- Uvicorn
- SQLite (default, can be changed)

---

## 📦 Installation and Running

### Prerequisites

- Python 3.8 or higher installed
- `pip` package manager
- (Optional) Virtual environment tool (`venv` or `virtualenv`)

### How to run
uvicorn app.main:app --reload


## 📁 Project Structure
Postman collecion as JSON:
{
	"info": {
		"_postman_id": "315f78f4-01b9-4cb0-b2f0-a5c02f51f383",
		"name": "spy_cats",
		"schema": "https://schema.getpostman.com/json/collection/v2.1.0/collection.json",
		"_exporter_id": "40413547",
		"_collection_link": "https://restless-moon-798980.postman.co/workspace/6f77a486-7d6a-4b5b-8154-4f3d6ee85166/collection/40413547-315f78f4-01b9-4cb0-b2f0-a5c02f51f383?action=share&source=collection_link&creator=40413547"
	},
	"item": [
		{
			"name": "Get all cats",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/cats/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"cats",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Get cat by cats_id",
			"protocolProfileBehavior": {
				"disableBodyPruning": true
			},
			"request": {
				"method": "GET",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{ \n    \"salary\": 85000.00\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/cats/6",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"cats",
						"6"
					]
				}
			},
			"response": []
		},
		{
			"name": "Update cat salary",
			"request": {
				"method": "PATCH",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/cats/6/salary",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"cats",
						"6",
						"salary"
					]
				}
			},
			"response": []
		},
		{
			"name": "Delete cat by cats_id",
			"request": {
				"method": "DELETE",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{ \n    \"salary\": 85000.00\n}"
				},
				"url": {
					"raw": "http://127.0.0.1:8000/cats/6",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"cats",
						"6"
					]
				}
			},
			"response": []
		},
		{
			"name": "Add cat",
			"request": {
				"method": "POST",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n  \"name\": \"Shadow\",\n  \"years_experience\": 4,\n  \"breed\": \"Persian\",\n  \"salary\": 2500.75\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/cats/",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"cats",
						""
					]
				}
			},
			"response": []
		},
		{
			"name": "Get all missions",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/missions",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"missions"
					]
				}
			},
			"response": []
		},
		{
			"name": "Get mission by mission_id",
			"request": {
				"method": "GET",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/missions/7",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"missions",
						"7"
					]
				}
			},
			"response": []
		},
		{
			"name": "Delete mission by mission_id",
			"request": {
				"method": "DELETE",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/missions/7",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"missions",
						"7"
					]
				}
			},
			"response": []
		},
		{
			"name": "Assign cat to the mission",
			"request": {
				"method": "PUT",
				"header": [],
				"url": {
					"raw": "http://127.0.0.1:8000/missions/7/assign-cat/4",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"missions",
						"7",
						"assign-cat",
						"4"
					]
				}
			},
			"response": []
		},
		{
			"name": "Update the notes in targets",
			"request": {
				"method": "PATCH",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": "{\n    \"notes\": \"New test note\"\n}",
					"options": {
						"raw": {
							"language": "json"
						}
					}
				},
				"url": {
					"raw": "http://127.0.0.1:8000/missions/targets/7/notes",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"missions",
						"targets",
						"7",
						"notes"
					]
				}
			},
			"response": []
		},
		{
			"name": "Complete the target",
			"request": {
				"method": "PATCH",
				"header": [],
				"body": {
					"mode": "raw",
					"raw": ""
				},
				"url": {
					"raw": "http://127.0.0.1:8000/missions/targets/7/complete",
					"protocol": "http",
					"host": [
						"127",
						"0",
						"0",
						"1"
					],
					"port": "8000",
					"path": [
						"missions",
						"targets",
						"7",
						"complete"
					]
				}
			},
			"response": []
		}
	]
}


