def calculate_energy(current_energy, energy_used):
    result = current_energy - energy_used

    if result < 0:
        return 0
    else:
        return result