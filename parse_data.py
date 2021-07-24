def fahrenheit_to_celsius(temp_in_fahrenheit: float):
    return (temp_in_fahrenheit - 32) * (5 / 9)


def mph_to_kmh(speed_in_mph):
    return speed_in_mph * 1.609344


def inch_to_mm(rain_in_inch):
    return rain_in_inch * 25.4


def parse_ecowitt_data(data):
    key_value_strings = data.split("&")
    parsed_data = dict()
    for key_value_string in key_value_strings:
        if not key_value_string:
            continue
        if "=" not in key_value_string:
            print(f"no value for the key {key_value_string}")
            continue
        key, value = key_value_string.split("=")
        key = key.strip()
        value = value.strip()
        if key == "dateutc":
            # pkt["timestamp"] = datetime.datetime.strptime(
            #    value, "%Y-%m-%d+%H:%M:%S"
            # ).isoformat()
            parsed_data["timestamp"] = f"'{value.replace('+', ' ')}'"
        elif key == "tempf":
            parsed_data["temp_outdoor_C"] = fahrenheit_to_celsius(float(value))
        elif key == "baromrelin":
            parsed_data["barometer"] = float(value)
        elif key == "baromabsin":
            parsed_data["pressure"] = float(value)
        elif key == "humidity":
            parsed_data["humidity_outdoor"] = float(value)
        elif key == "windspeedmph":
            parsed_data["wind_speed_kmh"] = mph_to_kmh(float(value))
        elif key == "windgustmph":
            parsed_data["wind_gust_kmh"] = mph_to_kmh(float(value))
        elif key == "maxdailygust":
            parsed_data["wind_gust_max_daily_kmh"] = mph_to_kmh(float(value))
        elif key == "winddir":
            parsed_data["wind_direction"] = float(value)
        elif key == "rainratein":
            parsed_data["rain_rate_mmph"] = inch_to_mm(float(value))
        elif key == "totalrainin":
            parsed_data["rain_total_mm"] = inch_to_mm(float(value))
        elif key == "eventrainin":
            parsed_data["rain_event_mm"] = inch_to_mm(float(value))
        elif key == "hourlyrainin":
            parsed_data["rain_hourly_mm"] = inch_to_mm(float(value))
        elif key == "dailyrainin":
            parsed_data["rain_daily_mm"] = inch_to_mm(float(value))
        elif key == "weeklyrainin":
            parsed_data["rain_weekly_mm"] = inch_to_mm(float(value))
        elif key == "monthlyrainin":
            parsed_data["rain_monthly_mm"] = inch_to_mm(float(value))
        elif key == "tempinf":
            parsed_data["temp_indoor_C"] = fahrenheit_to_celsius(float(value))
        elif key == "humidityin":
            parsed_data["humidity_indoor"] = float(value)
        elif key == "solarradiation":
            parsed_data["radiation"] = float(value)
        elif key == "uv":
            parsed_data["uv"] = float(value)
        elif key in [
            "PASSKEY",
            "stationtype",
            "model",
            "wh65batt",
            "freq",
        ]:
            # ignore those keys
            pass
        else:
            raise ValueError(f"unknown key '{key}'")
    return parsed_data


if __name__ == "__main__":
    parsed = parse_ecowitt_data(DATA)
    print(parsed)
