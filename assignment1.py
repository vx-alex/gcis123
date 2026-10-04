def get_normal_range(device_name):

    if device_name == "LED Light":
        return "0.01 0.10"
    elif device_name == "Television":
        return "0.05 0.50"
    elif device_name == "Refrigerator":
        return "0.10 1.50"
    elif device_name == "Washing Machine":
        return "0.30 2.50"
    elif device_name == "Air Conditioner":
        return "0.50 5.00"
    else:
        return ""


def get_energy_status(device_name, energy):

    normal_range = get_normal_range(device_name)

    if normal_range == "":
        return "Unknown"

    normal_range = normal_range.split()

    low = float(normal_range[0])
    high = float(normal_range[1])

    if energy < 0:
        return "Invalid"

    if energy >= low and energy <= high:
        return "Normal"
    elif energy <= high * 1.5:
        return "High"
    else:
        return "Critical"


def requires_attention(status):

    if status == "High" or status == "Critical":
        return True
    else:
        return False


def calculate_cost(energy, rate):

    if energy < 0:
        return 0.0

    cost = energy * rate
    return cost


def main():

    readings = "LED Light,0.06/LED Light,0.18/"
    readings = readings + "Television,0.32/Television,1.20/"
    readings = readings + "Refrigerator,0.80/Refrigerator,2.20/"
    readings = readings + "Washing Machine,1.40/Washing Machine,4.50/"
    readings = readings + "Air Conditioner,2.80/Air Conditioner,7.50"
    rate = 0.30
    readings = readings.split("/")

    # TASK 4 """Checks each reading and prints its energy details, status, attention, and cost."""

    for reading in readings:

        data = reading.split(",")

        device = data[0]
        energy = float(data[1])

        status = get_energy_status(device, energy)
        attention = requires_attention(status)
        cost = calculate_cost(energy, rate)

        print("Device:", device)
        print("Energy:", energy, "kWh")
        print("Status:", status)
        print("Requires Attention:", attention)
        print("Estimated Cost:", cost)
        print()

    # TASK 5 """Calculates totals, counts the different statuses, and finds the highest energy reading."""

    total_readings = 0
    total_energy = 0
    total_cost = 0

    normal = 0
    high = 0
    critical = 0
    attention_count = 0

    highest_energy = 0
    highest_device = ""

    for reading in readings:

        data = reading.split(",")

        device = data[0]
        energy = float(data[1])

        status = get_energy_status(device, energy)
        attention = requires_attention(status)
        cost = calculate_cost(energy, rate)

        total_readings = total_readings + 1
        total_energy = total_energy + energy
        total_cost = total_cost + cost

        if status == "Normal":
            normal = normal + 1
        elif status == "High":
            high = high + 1
        elif status == "Critical":
            critical = critical + 1

        if attention == True:
            attention_count = attention_count + 1

        if energy > highest_energy:
            highest_energy = energy
            highest_device = device


    print("Total Readings:", total_readings)
    print("Total Energy:", total_energy, "kWh")
    print("Total Cost:", total_cost)
    print("Normal:", normal)
    print("High:", high)
    print("Critical:", critical)
    print("Requires Attention:", attention_count)
    print("Highest Consumption:", highest_device, highest_energy, "kWh")

    # TASK 6 """Prints the final summary report for all the energy readings."""

    print()
    print("========== HomeSense Report ==========")
    print("Readings analyzed:", total_readings)
    print()
    print("Normal:", normal)
    print("High:", high)
    print("Critical:", critical)
    print()
    print("Readings requiring attention:", attention_count)
    print()
    print("Total energy:", total_energy, "kWh")
    print("Estimated cost: AED", total_cost)
    print()
    print("Highest consumption:")
    print(highest_device, "-", highest_energy, "kWh")

main()