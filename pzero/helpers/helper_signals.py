# This function disconnect all the signals of a QObject
def disconnect_all_signals(signals):
    # for each signal inside the list, disconnect it
    for signal in signals:
        signal.disconnect()

    return
