def export_file(alerts):
    with open('market_alerts.txt', "w") as file:

        if len(alerts) == 0:
            file.write('Market is stable today.')
        else:
            for alert in alerts:
                file.write(alert)
                if alert not in alerts[-1]:
                    file.write("\n"+"-"+"\n")
    print("market_alerts.txt is imported successfully.")