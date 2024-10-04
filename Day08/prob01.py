import json

# Original JSON data
data = {
    "ingress_rules": [
        {
            "cidr_blocks": ["10.111.108.0/23", "10.111.110.0/23"],
            "description": "",
            "from_port": 8000,
            "protocol": "tcp",
            "security_groups": [],
            "self": False,
            "to_port": 8999
        },
        {
            "cidr_blocks": [],
            "description": "",
            "from_port": 8000,
            "protocol": "tcp",
            "security_groups": ["sg-08fcfdd7edc91011f"],
            "self": False,
            "to_port": 8999
        },
        {
            "cidr_blocks": [],
            "description": "",
            "from_port": 80,
            "protocol": "tcp",
            "security_groups": ["sg-08fcfdd7edc91011f"],
            "self": False,
            "to_port": 80
        },
        {
            "cidr_blocks": [],
            "description": "",
            "from_port": 80,
            "protocol": "tcp",
            "security_groups": ["sg-0ee24c8fc6c270768"],
            "self": False,
            "to_port": 80
        }
    ]
}

# Function to delete an ingress rule
def delete_ingress_rule(data, from_port):
    data['ingress_rules'] = [rule for rule in data['ingress_rules'] if rule['from_port'] != from_port]

# Delete the ingress rule with from_port 8000
delete_ingress_rule(data, 8000)

# Print the modified JSON
print(json.dumps(data, indent=4))