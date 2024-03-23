def take_magic_damage(health, resist, amp, spell_power):
    # Calculate total maximum damage
    total_damage = spell_power * amp
    
    # Subtract resist from total damage to get actual damage dealt
    actual_damage = max(0, total_damage - resist)
    
    # Apply damage to player's health
    new_health = health - actual_damage
    
    return new_health
