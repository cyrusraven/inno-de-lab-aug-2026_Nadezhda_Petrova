db_config = {
    "connection": {
        "host": "production-db.internal",
        "port": 5432,
        "user": "postgres"
    }
}

db_host = db_config["connection"].get("host")
db_port = db_config["connection"].get("port")

connections = db_config.get("connection", {})
if "ssl_settings" in connections and "ssl_mode" in connections.get("ssl_settings", {}):
    ssl_mode = connections["ssl_settings"]["ssl_mode"]
else:
    ssl_mode = "verify-full"

db_config["connection"]["user"] = "admin"
db_config["connection"]["max_connections"] = 100

print(f'SSL Mode: {ssl_mode}')

print("Параметры соединения: ")
for k, v in db_config["connection"].items():
    print(f"* {k}: {v}")
