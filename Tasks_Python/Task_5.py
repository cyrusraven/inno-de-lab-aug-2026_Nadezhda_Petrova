system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online")
]

active_node_name = []  # list of node_name
cpu_loads = []  # list of cpu_load
ram_usages = []  # list of rum_usage
count = 0  # counter of active node_name
for node_name, cpu_load, ram_usage, status in system_telemetry:
    if status == 'online':  # only 'online'
        active_node_name.append(node_name)  # add node_names with status 'online'
        cpu_loads.append(cpu_load)  # add cpu_loads with status 'online'
        ram_usages.append(ram_usage)  # add rum_usages with status 'online'
        count += 1

telemetry_report = {  # creating a dict
    'active_nodes_count': count,
    'metrics': {
        'average_cpu': round(sum(cpu_loads) / len(cpu_loads), 2),
        'max_ram': max(ram_usages)
    }
}

print(f'Активные узлы в сети: {active_node_name}')

print('Итоговый отчет телеметрии:')
for k, v in telemetry_report.items():
    print(f'{k}: {v}')
