requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]
required_admin_roles = {"admin", "audit_manager", "security_officer"}
set_requested_roles = set(requested_roles)

print(f'Уникальные запрошенные роли: {set_requested_roles}')

print(f'Общие административные роли: {set_requested_roles.intersection(required_admin_roles)}')

print(f'Недостающие административные роли: {required_admin_roles.difference(set_requested_roles)}')

if 'security_officer' in set_requested_roles:
    print('Наличие роли security_officer в запросе: True')
else:
    print('Наличие роли security_officer в запросе: False')
