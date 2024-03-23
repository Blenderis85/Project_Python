def unlock_achievement(before_xp, ach_xp, ach_name):
    # Calculate player's xp after the achievement is unlocked
    after_xp = before_xp + ach_xp
    
    # Generate the alert message
    alert_message = f"Achievement Unlocked: {ach_name}"
    
    return after_xp, alert_message
